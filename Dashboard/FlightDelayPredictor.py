from FlightDelayPredictorDS import FlightDelayPredictorDS
from AirportWeather import AirportWeather
from application_config import *
from model_import import *

class FlightDelayPredictor:

    def __init__(self):
        self.flightDataSource = FlightDelayPredictorDS(FlightDataConfig)
        self.airportWeatherDataSource = AirportWeather(AirportWeatherConfig)

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

    def get_flight_predict_data(self, origin_airport_code, dest_airport_code, airline_id, travel_date):
        
        airport_hourly_weather_list = self.airportWeatherDataSource.get_airport_hourly_weather(origin_airport_code, travel_date)

        df = flight_delay_model(airline_id, origin_airport_code, dest_airport_code, 20, .1)

        #print(df)

        flight_delay_predict_by_hours_list = []
        flight_hour_data_dict = {}
        
        index = 0

        while index < 16:

            flight_hour_data_dict = {}

            flight_hour_data_dict["status"] = 0

            flight_hour_data_dict["cloudiness"] = airport_hourly_weather_list[index][0]

            flight_hour_data_dict["precipitation"] = airport_hourly_weather_list[index][1]

            flight_hour_data_dict["wind"] = airport_hourly_weather_list[index][2]

            flight_hour_data_dict["humidity"] = airport_hourly_weather_list[index][3]

            flight_hour_data_dict["visibility"] = airport_hourly_weather_list[index][4]

            flight_delay_predict_by_hours_list.append(flight_hour_data_dict)

            index += 1

        return flight_delay_predict_by_hours_list
