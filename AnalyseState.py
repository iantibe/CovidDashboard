import sqlite3
from sqlite3 import Error
import pandas as pd

databaseName = "statedata"

class AnalyseState:
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

    def analyse_state(self, state):
        max_death = -1
        min_death = -1
        max_cases = -1
        min_cases = -1
        average_cases = -1
        average_deaths = -1


        conn = self.init_connection()
        item_to_search = [state]
        data = conn.cursor()

        results = data.execute("Select state, cases, deaths from statedata where state=?", item_to_search).fetchall()



        new_list = []

        previous_case = 0
        previous_death = 0

        for x in results:
            """x is touble"""

            previous_case = x[1] - previous_case
            previous_death = x[2] - previous_death

            new_touple = (x[0], previous_case, previous_death)
            new_list.append(new_touple)

            previous_case = x[1]
            previous_death = x[2]

        print(new_list)
        print(results)

        data_frame = pd.DataFrame(new_list, columns=['State', "New Cases", "New Deaths"])
        print(data_frame)
        average_data_frame = data_frame.mean()
        print(data_frame.max())
        print(data_frame.min())
        print(average_data_frame)

if __name__ == '__main__':
    instance = AnalyseState()
    instance.analyse_state("Iowa")