from FlightDelayPredictorDB import FlightDelayPredictorDB

class FlightDelayPredictor:

    def __init__(self):
        self.datasource = FlightDelayPredictorDB() #= create_engine('sqlite:///bookstore.db')

    def get_origin_states(self):

        return self.datasource.get_origin_states()

    def get_origin_airports(self, origin_state):

        return self.datasource.get_origin_airports(origin_state)

    def get_dest_states(self, origin_airport_code):
   
        return self.datasource.get_dest_states(origin_airport_code)

    def get_dest_state_airports(self, origin_airport_code, dest_state):
        
        return self.datasource.get_dest_airports(origin_airport_code, dest_state)

    def get_dest_airlines(self, origin_airport_code, dest_airport_code):

        return self.datasource.get_dest_airlines(origin_airport_code, dest_airport_code)

    def get_flight_predict_data(self, origin_airport_code, dest_airport_code, travel_date):
        
        flight_predict_list = []
        flight_hour_data_dict = {}
        
        import random
        
        index = 0

        while index < 16:

            flight_hour_data_dict = {}

            flight_hour_data_dict["status"] = random.randint(0,1)

            flight_hour_data_dict["cloudiness"] = random.randint(0,100)

            flight_hour_data_dict["precipitation"] = random.randint(0,20)

            flight_hour_data_dict["wind"] = random.randint(0,50)

            flight_hour_data_dict["humidity"] = random.randint(0,50)

            flight_hour_data_dict["visibility"] = random.randint(0,25)

            flight_predict_list.append(flight_hour_data_dict)

            index += 1

        return flight_predict_list
