from FlightDelayPredictorDS import FlightDelayPredictorDS
from AirportWeather import AirportWeather
from FlightDelayPredictorModel import FlightDelayPredictorModel
from application_config import FlightDataConfig, AirportWeatherConfig, ModelConfig


class FlightDelayPredictor:

    def __init__(self):

        # Initalize data source objects
        self.flightDataSource = FlightDelayPredictorDS(FlightDataConfig)
        self.airportWeatherDataSource = AirportWeather(AirportWeatherConfig)

        #Initalize machine learning model
        self.FlightDelayPredictorModel = FlightDelayPredictorModel(ModelConfig)

    def get_origin_states(self):

        return self.flightDataSource.get_origin_states()

    def get_origin_airports(self, origin_state):

        return self.flightDataSource.get_origin_airports(origin_state)

    def get_dest_states(self, origin_airport_code):
   
        return self.flightDataSource.get_dest_states(origin_airport_code)

    def get_dest_state_airports(self, origin_airport_code, dest_state):
        
        return self.flightDataSource.get_dest_airports(origin_airport_code, dest_state)

    def get_dest_airlines(self, origin_airport_code, dest_airport_code):

        return self.flightDataSource.get_dest_airlines(origin_airport_code, dest_airport_code)

    def get_flight_predict_data(self, hours_list, origin_airport_code, dest_airport_code, airline_id, travel_date):
        
        # Get hourly weather data for origin airport and travel date
        airport_hourly_weather_list = self.airportWeatherDataSource.get_airport_hourly_weather(hours_list, origin_airport_code, travel_date)

        windspeed_list = []

        precipitation_list = []
        
        # Extract hourly windspeed and precipitation weather data to 
        # input into the flight delay predictor, machine learning model
        for hourly_weather in airport_hourly_weather_list:

            precipitation_list.append(hourly_weather[1])

            windspeed_list.append(hourly_weather[2])

        # Get hourly flight delay predictions for
        #   5 AM to 8 PM
        #   Airline
        #   Origin airport
        #   Destination airport
        #   Hourly windspeed 
        #   Hourly precipitation
        delay_df = self.FlightDelayPredictorModel.predict_hourly_delays(hours_list, airline_id, origin_airport_code, dest_airport_code, windspeed_list, precipitation_list)

        # Get hourly delay prediction column
        flight_delay_hourly_predict_list = delay_df["delayed"].to_list()

        # Generate flight delay result set
        # Containing hourly
        #   Delay status
        #   Cloud cover
        #   Precipitation
        #   Wind speed
        #   Humidity
        #   Visibility
        flight_hourly_data_list = []

        flight_hour_data_dict = {}
        
        index = 0

        while index < 16:

            flight_hour_data_dict = {}

            flight_hour_data_dict["status"] = flight_delay_hourly_predict_list[index]

            flight_hour_data_dict["cloudiness"] = airport_hourly_weather_list[index][0]

            flight_hour_data_dict["precipitation"] = airport_hourly_weather_list[index][1]

            flight_hour_data_dict["wind"] = airport_hourly_weather_list[index][2]

            flight_hour_data_dict["humidity"] = airport_hourly_weather_list[index][3]

            flight_hour_data_dict["visibility"] = airport_hourly_weather_list[index][4]

            flight_hourly_data_list.append(flight_hour_data_dict)

            index += 1

        return flight_hourly_data_list
