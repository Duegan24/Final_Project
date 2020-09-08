
from  sqlalchemy import create_engine

class DatabaseDataSource:

    def __init__(self, databaseConfig):

        user          = databaseConfig["user"]
        password      = databaseConfig["password"]
        host          = databaseConfig["host"]
        port          = databaseConfig["port"]
        database      = databaseConfig["database"]
        database_type = databaseConfig["database_type"]

        url = "{}://{}:{}@{}:{}/{}".format(database_type, user, password, host, port, database)

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
