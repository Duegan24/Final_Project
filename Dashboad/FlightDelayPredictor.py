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
        
        flight_time_delay_predict_list = []
        
        am_pm = ""
        display_hour = 0

        for hour in range(5, 20):
            if hour < 12:
                am_pm = "AM"
                display_hour = hour
            elif hour == 12:
                am_pm = "PM"
                display_hour = hour
            else:
                am_pm = "PM"
                display_hour = hour - 12

            flight_time_delay_predict_list.append([str(display_hour) + ":00 " + am_pm, 0])
            flight_time_delay_predict_list.append([str(display_hour) + ":30 " + am_pm, 1])

        return flight_time_delay_predict_list

