import sqlite3
from sqlite3 import Error
import pandas as pd

databaseName = "countrydata"

class AnalyseCountry:
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

    def create_dict(self, max_case, min_case, max_death, min_death, average_case, average_death):
        return {"maxcase": max_case, "mincase": min_case, "maxdeath": max_death, "mindeath":min_death,
                "averagecase": average_case, "averagedeath": average_death}

    def analyse_country(self, country):
        max_death = -1
        min_death = -1
        max_cases = -1
        min_cases = -1
        average_cases = -1
        average_deaths = -1

        conn = self.init_connection()
        item_to_search = [country]
        data = conn.cursor()

        results = data.execute("Select country, cases, deaths from countrydata where country=?", item_to_search).fetchall()

        new_list_of_data = []

        previous_case = 0
        previous_death = 0

        for x in results:
            previous_case = x[1] - previous_case
            previous_death = x[2] - previous_death

            new_touple = (x[0], previous_case, previous_death)
            new_list_of_data.append(new_touple)

            previous_case = x[1]
            previous_death = x[2]

        data_frame = pd.DataFrame(new_list_of_data, columns=['Country', "New Cases", "New Deaths"])
        average_data_frame = data_frame.mean()
        max_data_frame = data_frame.max()
        min_data_frame = data_frame.min()

        print(results)
        print(new_list_of_data)


        max_cases = max_data_frame[1]
        max_death = max_data_frame[2]

        average_cases = average_data_frame[0]
        average_deaths = average_data_frame[1]

        min_cases = min_data_frame[1]
        min_death = min_data_frame[2]
        conn.close()
        return  self.create_dict(str(max_cases),str(min_cases), str(max_death), str(min_death), str(average_cases),str(average_deaths))


