
from  sqlalchemy import create_engine

class DatabaseDataSource:

    def __init__(self, databaseConfig):

        # Get database configuration parameters
        user          = databaseConfig["user"]
        password      = databaseConfig["password"]
        host          = databaseConfig["host"]
        port          = databaseConfig["port"]
        database      = databaseConfig["database"]
        database_type = databaseConfig["database_type"]

        # Generate database connection url
        url = "{}://{}:{}@{}:{}/{}".format(database_type, user, password, host, port, database)

        # create SQLAlcheme engine
        self.engine = create_engine(url)


    # Execute parameterized database select statement
    def execute_select(self, sql, params_dict = {}):

        try:

            # Populate select string parameters
            for param_name in params_dict:
                sql = sql.replace("{" + param_name + "}", params_dict[param_name])
           
            
            # Get connection
            connection = self.engine.connect()

            # Execute select statment and get results
            result = connection.execute(sql)

            # Convert results 
            return self.convert_from_sql_alch_result(result.fetchall())
 
        except (Exception) as error:

            error_message = f"Error occured while getting select informaion. Query SQL:{sql} parameters:{params_dict}"

            print(error_message, error)
        
        finally:

            connection.close()

    # Convert results from SQLAlcheme result set 
    # to a list of tuple rows result set
    def convert_from_sql_alch_result(self, sql_alch_result):
        
        convert_from_sql_alch_result_list = []

        # Iterate through SQLAlchemy result set rows
        for row in sql_alch_result:

            convert_from_sql_alch_row = []

            # Iterate through SQLAlchemy row field
            for field in row:
            
                convert_from_sql_alch_row.append(str(field))

            # Covvert row field list to a tuple (read only)
            convert_from_sql_alch_result_list.append(tuple(convert_from_sql_alch_row))

        return convert_from_sql_alch_result_list
