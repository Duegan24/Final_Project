import psycopg2
from FlightDelayPredictorConfig import *

class FDPDatabasePsycopg2:

    def __init__(self):
        self.connection = psycopg2.connect(
                                            user=databaseConfig["user"], 
                                            password=databaseConfig["password"], 
                                            host=databaseConfig["host"], 
                                            port=databaseConfig["port"], 
                                            database=databaseConfig["database"]
                                          )

    def get_origin_states(self):

        return self.execute_select(databaseConfig["sql_select_orig_states"])


    def get_origin_airports(self, origin_state):

        return self.execute_select(databaseConfig["sql_select_orig_airports"], {"origin_state":origin_state})


    def get_dest_states(self, origin_airport_code):

        return self.execute_select(databaseConfig["sql_select_dest_states"], {"origin_airport_code":origin_airport_code})


    def get_dest_airports(self, origin_airport_code, dest_state):

        return self.execute_select(databaseConfig["sql_select_dest_airports"], {"origin_airport_code":origin_airport_code, "dest_state":dest_state})


    def get_dest_airlines(self, origin_airport_code, dest_airport_code):

        return self.execute_select(databaseConfig["sql_select_dest_airlines"], {"origin_airport_code":origin_airport_code, "dest_airport_code":dest_airport_code})

    def execute_select(self, sql, params_dict = {}):

        try:
            
            cursor = self.connection.cursor()

            for param_name in params_dict:
            
                sql = sql.replace("{" + param_name + "}", params_dict[param_name])

            cursor.execute(sql)

            return cursor.fetchall()

        except (Exception, psycopg2.Error) as error:

            error_message = f"Error occured while getting select informaion. Query SQL:{sql} parameters:{params_dict}"

            print(error_message, error)
        
        finally:

            cursor.close()
