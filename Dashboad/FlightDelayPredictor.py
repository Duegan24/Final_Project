from FDPDatabasePsycopg2 import FDPDatabasePsycopg2


class FlightDelayPredictor:

    def __init__(self):
        self.database = FDPDatabasePsycopg2()

    def get_origin_states(self):

        return self.database.get_origin_states()

    def get_origin_airports(self, origin_state):

        return self.database.get_origin_airports(origin_state)

    def get_dest_states(self, origin_airport_code):
   
        return self.database.get_dest_states(origin_airport_code)

    def get_dest_state_airports(self, origin_airport_code, dest_state):
        
        return self.database.get_dest_airports(origin_airport_code, dest_state)

    def get_dest_airlines(self, origin_airport_code, dest_airport_code):

        return self.database.get_dest_airlines(origin_airport_code, dest_airport_code)

    def get_flight_predict_data(self, origin_airport_code, dest_airport_code, travel_date):
        
        flight_predict_list = []
        
        import random
        
        index = 0

        while(index < 32):

            flight_predict_list.append(random.randint(0,1))

            index += 1

        return flight_predict_list
