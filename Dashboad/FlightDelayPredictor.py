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

    def get_dest_state_airports(self, date, origin_state_code, dest_state_code):
        
        return []

    def get_dest_flight_info(self, date, origin_airport, dest_airport_code):

        return []
