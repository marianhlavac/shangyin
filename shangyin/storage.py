import sqlite3
import os

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

def quote(string, quotes = '"'):
    return '{}{}{}'.format(quotes, string, quotes)

class Storage:
    def __init__(self, path=DEFAULT_PATH):
        self.db = sqlite3.connect(path, check_same_thread=False) # FIXME: DO THREAD LOCKS!
        self.cur = self.db.cursor()

    def __del__(self):
        self.db.close()

    def q(self, query):
        self.cur.execute(query)

    def need_setup(self):
        self.q('select name from sqlite_master where type="table"') # TODO: This is not enough
        return len(self.cur.fetchall()) <= 0

    def setup(self):
        if self.need_setup():
            with open('schema.sql') as schema:
                self.cur.executescript(schema.read())

    def commit(self):
        self.db.commit()

    def rows(self):
        return self.cur.fetchall()

    def select(self, what, fromwhere, params = ''):
        self.q('SELECT {} FROM {} {}'.format(what, fromwhere, params))
        return self.rows()

    def select_last_id(self):
        self.q('SELECT last_insert_rowid()')
        return self.rows()[0][0]

    def insert(self, into, data, params = '', quotes = '"'):
        columns = ','.join(data.keys())
        values = ','.join(map(lambda x: quote(x, quotes), data.values()))
        self.q('INSERT INTO {} ({}) VALUES ({}) {}'.format(into, columns, values, params))

    def update(self, table, data, where, params = ''):
        sets = ','.join(map(lambda x : '{} = "{}"'.format(x[0], x[1]), data.items()))
        self.q('UPDATE {} SET {} WHERE {} {}'.format(table, sets, where, params))

    def upsert(self, into, id, data, params = ''):
        whereid = 'WHERE id = "{}"'.format(id)
        if self.get_count('into', whereid) > 0:
            self.update(into, data, whereid)
        else:
            self.insert(into, data)

    def get_count(self, of, params = ''):
        return self.select('COUNT(*)', of, params)[0][0]

    def get_by_id(self, what, id, select='*'):
        fetch = self.select(select, what, 'WHERE id = "{}"'.format(id))
        return fetch[0] if len(fetch) > 0 else None

    def exists_with_id(self, what, id):
        return self.get_count(what, 'WHERE id = "{}"'.format(id)) > 0

    # ---

    def create_user(self, email, fullname, department, password):
        self.insert('user', { 
            'email': email, 
            'fullname': fullname, 
            'department': department, 
            'password': password
        })
        self.commit()
        return self.select_last_id()

    def card_exists(self, id):
        return self.get_count('card', 'WHERE id = "{}"'.format(id)) > 0

    def create_card(self, id):
        self.insert('card', { 
            'id': id
        })
        self.commit()
        return self.select_last_id()

    def assign_card(self, id, userid):
        self.update('card', { 'user_id': userid }, 'id = "{}"'.format(id))
        self.commit()

    def create_coffee(self, cardid, milk = 0):        
        self.insert('coffee', { 
            'card_id': quote(cardid),
            'logged': 'CURRENT_TIMESTAMP',
            'milk': quote(milk)
        }, quotes='')

        self.commit()
    