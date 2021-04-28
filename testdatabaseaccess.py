import json
import sqlite3
from sqlite3 import Error

import requests

databaseName = "statedata"


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


def add_item(conn, state_info, date, deaths, cases):
    conn.cursor()
    items_to_insert = [state_info, date, cases, deaths]
    conn.execute("Insert into statedata (state, date, cases, deaths) values (?, ?, ?, ?)", items_to_insert)
    conn.commit()


def check_content(conn, state_inf, date):
    conn.cursor()
    data_to_check = [state_inf, date]
    result = conn.execute("Select state, date from statedata WHERE state = ? and date=? ", data_to_check)
    print(len(result.fetchall()))




conn = init_connection()
selectconnect = init_connection()

check_content(conn,"Iowa","2021-06-13")

conn.close()
selectconnect.close()