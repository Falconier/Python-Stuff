import sqlite3
from contextlib import closing
from sqlite3 import Error

def create_database(db_file):
    try:
        con = sqlite3.connect(db_file)
        print("created")
    except:
        print("Failed")
        con = None
    return con

con = create_database("hr.sqlite")

def create_table(connection, table_name):
    cur = connection.cursor()
    cur.execute("CREATE TABLE "
                + table_name +
                "(id integer PRIMARY KEY, name text,"
                " department text, title text, hireDate text)")
    connection.commit()
def get_all_table_names(connection):
    '''
    query tables in a database
    :param connection:
    :return: list of table names
    '''
    if connection:
        query = "select name from sqlite_master where type == 'table'"
        with closing(connection.cursor()) as cur:
            cur.execute(query)
            tables = cur.fetchall()
            return tables

print(get_all_table_names(con))

def get_column_info(connection, table_name):
    '''

    :param connection to a database,
           table_name: table name
    :return: all columns
    '''
    if connection:
        query = "pragma table_info( " + table_name + ")"
                #"from sqlite_master " \
                #"where type == 'table'" \
                #"and name == ?"
        with closing(connection.cursor()) as cur:
            cur.execute(query)#, ("employee", ))
            sql_command = cur.fetchall()
            print(sql_command)

            #generate column list
            columns = []

            return

get_column_info(con, "employee")
#create_table(con, "employee")


