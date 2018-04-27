import sqlite3
import os

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

def connect(path=DEFAULT_PATH):
    return sqlite3.connect(path) 

def need_setup(cur):
    cur.execute('select name from sqlite_master where type=\'table\'') # TODO: This is not enough
    return len(cur.fetchall()) <= 0

def setup(cur):
    with open('schema.sql') as schema:
        cur.executescript(schema.read())

def uid_exists(cur, uid):
    cur.execute('''
        select * from users where id=?
    ''', uid)
    return len(cur.fetchall()) > 0

def create_uid(cur, uid):
    cur.execute('''
        insert into users values (?, ?, ?)
    ''', (uid, 'Unnammed', 'Untitled'))

def log_coffee_to_uid(cur, uid):
    cur.execute('''
        insert into users values (NOW(), ?, ?, ?)
    ''', (uid, 0, 'Untitled'))