from AirportWeatherDS import AirportWeatherDS

class AirportWeather:

    def __init__(self, datasourceConfig):
        
        self.airportWeatherDataSource = AirportWeatherDS(datasourceConfig)

    def get_airport_hourly_weather(self, airport_code, date):
        
        return self.airportWeatherDataSource.get_airport_hourly_weather(airport_code, date)
