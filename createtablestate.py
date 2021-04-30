import sqlite3
from sqlite3 import Error

databaseName = "statedata"
create_table_statedata_sql = """CREATE TABLE IF NOT EXISTS statedata (
                        id integer primary key autoincrement,
                        state text,
                        date  text,
                        cases integer,
                        deaths integer
                        );"""




def init_connection():
    """
    creates connection to database
    :return: connection object
    """
    try:
        conn = None
        conn = sqlite3.connect(databaseName)
        return conn
    except Error:
        print(Error)


def create_table(connection, sql_statement):
    """
    Creates tables for stock data
    :param connection: connection object
    :param sql_statement: sql statement to execute
    :return: none
    """
    try:
        query = connection.cursor()
        query.execute(sql_statement)
    except Error:
        print(Error)


def create_database():
    conn = init_connection()
    create_table(conn, create_table_statedata_sql)

    conn.close()

if __name__ == '__main__':
    create_database()