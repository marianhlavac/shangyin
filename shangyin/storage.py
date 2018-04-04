import sqlite3

db = sqlite3.connect(':memory:')

def close():
    db.close()

def commit():
    db.commit()

def initialized():
    c = db.cursor()
    c.execute('select name from sqlite_master where type=\'table\'')
    return len(c.fetchall()) > 0

def initialize():
    create_table('coffees', 'date text, user text, type text, quantity text')
    commit()

def create_table(name, columns):
    c = db.cursor()
    c.execute('create table {} ({})'.format(name, columns)) # FIXME: security risk

def insert(table, values):
    c = db.cursor()
    c.execute('insert into {} values ({})'.format(table, values)) # FIXME: security risk