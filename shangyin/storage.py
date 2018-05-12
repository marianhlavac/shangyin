import sqlite3
import os

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

class Storage:
    def __init__(self, path=DEFAULT_PATH):
        self.db = sqlite3.connect(path) 
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

    def add_user(self, email, fullname, department, password):
        self.q(
            'INSERT INTO user (email, fullname, department, password) VALUES ("{}", "{}", "{}", "{}")'.format(
                email, fullname, department, password
            ))
        self.commit()

    def get_users(self):
        self.q('SELECT * FROM user')
        return self.rows()


    def add_coffee(self, user, milk = 0):
        pass
    