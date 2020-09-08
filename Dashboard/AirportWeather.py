from AirportWeatherDS import AirportWeatherDS

class AirportWeather:

    def __init__(self, datasourceConfig):
        
        self.airportWeatherDataSource = AirportWeatherDS(datasourceConfig)

    def get_airport_weather_data(self, airport_code, date):
        
        return self.airportWeatherDataSource.get_airport_weather(airport_code, date)
