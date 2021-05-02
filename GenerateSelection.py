import json
import sqlite3
from sqlite3 import Error

country_databasename = "countrydata"
state_databasename = "statedata"
class GenerateSelection:

    def init_connection(self, database):
        """
        creates connection to database
        :return: connection object
        """
        try:
            conn = None
            conn = sqlite3.connect(database)
            return conn
        except Error:
            print(Error)


    def get_states(self):
        conn = self.init_connection(state_databasename)
        query = conn.cursor()
        results = query.execute("select distinct state from statedata;").fetchall()

        resultlist = []

        for x in results:
            resultlist.append(x[0])

        conn.close()
        return json.dumps(resultlist)

    def get_countries(self):
        conn = self.init_connection(country_databasename)
        query = conn.cursor()
        results = query.execute("select distinct country from countrydata;")

        result_list = []

        for x in results:
            result_list.append(x[0])

        conn.close()
        return json.dumps(result_list)

    def get_state_dates(self):
        conn = self.init_connection(state_databasename)
        query = conn.cursor()
        results = query.execute("select distinct date from statedata;")

        results_list = []

        for x in results:
            results_list.append(x[0])

        conn.close()
        return json.dumps(results_list)

    def get_country_dates(self):
        conn = self.init_connection(country_databasename)
        query = conn.cursor()
        results = query.execute("select distinct date from countrydata;")

        result_list = []

        for x in results:
            result_list.append(x[0])

        conn.close()
        return json.dumps(result_list)
