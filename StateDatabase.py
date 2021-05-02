import json
import sqlite3
from sqlite3 import Error
import requests

databaseName = "statedata"

class StateDatabase:

    def init_connection(self):
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


    def add_item(self, conn, state_info, date, deaths, cases):
        conn.cursor()
        items_to_insert = [state_info, date, cases, deaths]
        conn.execute("Insert into statedata (state, date, cases, deaths) values (?, ?, ?, ?)", items_to_insert)
        conn.commit()

    def check_content(self, conn, state_inf, date):
        conn.cursor()
        data_to_check = [state_inf, date]
        result = conn.execute("Select state, date from statedata WHERE state = ? and date=? ", data_to_check)
        return len(result.fetchall())

    def update(self):
        print("in update state")
        reqes = requests.get("https://energ.ee/covid19-us-api/states.json")

        conn = self.init_connection()
        selectconnect = self.init_connection()

        req = json.loads(reqes.text)
        for state in req:
            """req[state] list of data"""

            """state state"""

            for datapoint in req[state]:

                """datapoint["date"] date fir state
                datapoint["deaths"] deaths
                datapoint["confirmed"]cases"""
                """state """
                if self.check_content(selectconnect, state, datapoint["date"]) == 0:
                    print("not in there")
                    self.add_item(conn, state, datapoint["date"], datapoint["deaths"], datapoint["confirmed"])

        conn.close()
        selectconnect.close()
        return {"status": "done"}
