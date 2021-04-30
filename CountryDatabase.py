import json
import sqlite3
from sqlite3 import Error
import requests

databasename = "countrydata"

class CountryDatabase:
    def init_connection(self):
        """
        creates connection to database
        :return: connection object
        """
        try:
            conn = None
            conn = sqlite3.connect(databasename)
            return conn
        except Error:
            print(Error)


    def add_item(self, conn, country, date, deaths, cases):
        conn.cursor()
        items_to_insert = [country, date, cases, deaths]
        conn.execute("Insert into countrydata (country, date, cases, deaths) values (?, ?, ?, ?)", items_to_insert)
        conn.commit()

    def check_content(self, conn, country_inf, date):
        conn.cursor()
        data_to_check = [country_inf, date]
        result = conn.execute("Select country, date from countrydata WHERE country = ? and date=? ", data_to_check)
        return len(result.fetchall())

    def update(self):

        reqes = requests.get("https://pomber.github.io/covid19/timeseries.json")

        conn = self.init_connection()
        selectconnect = self.init_connection()

        req = json.loads(reqes.text)
        for country in req:
            """req[country] list of data"""

            """country country"""

            for datapoint in req[country]:

                """datapoint["date"] date for country
                datapoint["deaths"] deaths
                datapoint["confirmed"]cases
                datapoint["recovered"] recovered """

                if self.check_content(selectconnect, country, datapoint["date"]) == 0:
                    self.add_item(conn, country, datapoint["date"], datapoint["deaths"], datapoint["confirmed"])
                    print(country)

        conn.close()
        selectconnect.close()

if __name__ == '__main__':
    item = CountryDatabase()
    item.update()
