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
    return len(result.fetchall())

reqes = requests.get("https://energ.ee/covid19-us-api/states.json")


conn = init_connection()
selectconnect = init_connection()

req = json.loads(reqes.text)
for state in req:
    """req[state] list of data"""

    """state state"""

    for datapoint in req[state]:

        """datapoint["date"] date fir state
        datapoint["deaths"] deaths
        datapoint["confirmed"]cases"""
        """state """
        if check_content(selectconnect,state, datapoint["date"]) == 0:
            print("not in there")
        else:
            print("in there")



conn.close()
selectconnect.close()

"""add_item(conn, state, datapoint["date"], datapoint["deaths"], datapoint["confirmed"])"""