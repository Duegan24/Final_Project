from DatabaseDataSource import DatabaseDataSource

class AirportWeatherDS(DatabaseDataSource):

    def __init__(self, datasourceConfig):

        DatabaseDataSource.__init__(self, datasourceConfig)
        
        # Initialize select query string properties
        self.sql_select_airport_hourly_weather = datasourceConfig["sql_select_airport_hourly_weather"]


    def get_airport_hourly_weather(self, hours_list, airport_code, date):
        
        # The hour_list parameter not used at this time. The database hourly weather table
        # only has weather for 5 AM to 8 PM.This is for performance reasons. If additional hourly 
        # weather data is needed it will be added to the databaase weather table.  
        
        return self.execute_select(self.sql_select_airport_hourly_weather, {"airport_code":airport_code, "date":date})