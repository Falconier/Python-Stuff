import sqlite3
from sqlite3 import Error

def create_database(db_file):
    try:
        con = sqlite3.connect(db_file)
        print('created')
    except:
        print('failed')
        con = None
    return con

create_database(".sqlite")
