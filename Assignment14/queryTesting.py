import sqlite3
from contextlib import closing
from sqlite3 import Error

def createConnection(dbFile):
    try:
        conx = sqlite3.connect(dbFile)
        print('connected\n')
    except:
        print('connection faied')
        conx = None
    return conx



createConnection('movies.sqlite')

