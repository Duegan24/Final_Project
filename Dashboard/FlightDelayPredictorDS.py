from DatabaseDataSource import DatabaseDataSource

class FlightDelayPredictorDS(DatabaseDataSource):

    def __init__(self, datasourceConfig):

        DatabaseDataSource.__init__(self, datasourceConfig)
        self.sql_select_orig_states   = datasourceConfig["sql_select_orig_states"]
        self.sql_select_orig_airports = datasourceConfig["sql_select_orig_airports"]
        self.sql_select_dest_states   = datasourceConfig["sql_select_dest_states"]
        self.sql_select_dest_airports = datasourceConfig["sql_select_dest_airports"]
        self.sql_select_dest_airlines = datasourceConfig["sql_select_dest_airlines"]


    def get_origin_states(self):

        return self.execute_select(self.sql_select_orig_states)


    def get_origin_airports(self, origin_state):

        return self.execute_select(self.sql_select_orig_airports, {"origin_state":origin_state})


    def get_dest_states(self, origin_airport_code):

        return self.execute_select(self.sql_select_dest_states, {"origin_airport_code":origin_airport_code})


    def get_dest_airports(self, origin_airport_code, dest_state):

        return self.execute_select(self.sql_select_dest_airports, {"origin_airport_code":origin_airport_code, "dest_state":dest_state})


    def get_dest_airlines(self, origin_airport_code, dest_airport_code):

        return self.execute_select(self.sql_select_dest_airlines, {"origin_airport_code":origin_airport_code, "dest_airport_code":dest_airport_code})
