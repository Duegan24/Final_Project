from DatabaseDataSource import DatabaseDataSource

class AirportWeatherDS(DatabaseDataSource):

    def __init__(self, datasourceConfig):

        DatabaseDataSource.__init__(self, datasourceConfig)
        
        self.sql_select_airport_weather = datasourceConfig["sql_select_airport_weather"]


    def get_airport_weather(self, irport_code, date):
        
        return self.execute_select(self.sql_select_airport_weather)