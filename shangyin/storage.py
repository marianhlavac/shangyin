import sqlite3

db_model = {
    'coffees': [ 'date text', 'user text', 'type text', 'quantity text' ],
    'users': [ 'name text', 'fullname text', 'cardid text' ]
}

db = sqlite3.connect(':memory:')

def close():
    db.close()

def commit():
    db.commit()

def initialized():
    c = db.cursor()
    c.execute('select name from sqlite_master where type=\'table\'')
    return len(c.fetchall()) >= len(db_model.values())

def initialize():
    for table in db_model:
        create_table(table, ', '.join(db_model[table]))
    commit()

def create_table(name, columns):
    c = db.cursor()
    c.execute('create table {} ({})'.format(name, columns)) # FIXME: security risk

def insert(table, values):
    c = db.cursor()
    c.execute('insert into {} values ({})'.format(table, ','.join(map(lambda x: '\'' + x + '\'', values)))) # FIXME: security risk