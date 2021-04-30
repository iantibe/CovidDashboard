import sqlite3
from sqlite3 import Error

databaseName = "countrydata"

class SearchCountry:

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

    def convert_to_dict(self, case, death):
        return {"cases": case, "deaths": death}

    def search(self, date, country):
        connn = self.init_connection()
        connn.cursor()
        item_to_find = [country, date]
        result = connn.execute("SELECT cases, deaths from countrydata "
                               "where country=? and date=?", item_to_find).fetchone()
        return self.convert_to_dict(result[0], result[1])
