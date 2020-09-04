
from  sqlalchemy import create_engine
from FlightDelayPredictorConfig import *

class FlightDelayPredictorDB:

    def __init__(self):

        user        = databaseConfig["user"]
        password    = databaseConfig["password"]
        host        = databaseConfig["host"]
        port        = databaseConfig["port"]
        database    = databaseConfig["database"]

        url = "postgresql://{}:{}@{}:{}/{}".format(user, password, host, port, database)

        self.engine = create_engine(url)

    def execute_select(self, sql, params_dict = {}):

        try:
            for param_name in params_dict:
                sql = sql.replace("{" + param_name + "}", params_dict[param_name])
           
            connection = self.engine.connect()

            result = connection.execute(sql)

            return self.convert_from_sql_alch_result(result.fetchall())
 
        except (Exception) as error:

            error_message = f"Error occured while getting select informaion. Query SQL:{sql} parameters:{params_dict}"

            print(error_message, error)
        
        finally:

            connection.close()

    def convert_from_sql_alch_result(self, sql_alch_result):
        
        convert_from_sql_alch_result_list = []

        for row in sql_alch_result:
            
            convert_from_sql_alch_row = []

            for field in row:
            
                convert_from_sql_alch_row.append(str(field))

            convert_from_sql_alch_result_list.append(tuple(convert_from_sql_alch_row))

        return convert_from_sql_alch_result_list

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
