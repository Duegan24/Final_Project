from DatabaseConfig import *

# Configuration for FlightDelayPredictor object
FlightDataConfig = {
    "host":host,
    "port":"5432", 
    "user":user, 
    "password":password, 
    "database":"flightsdata",
    "database_type":"postgresql",
# --------------------------------
    "sql_select_orig_states":
"""
SELECT DISTINCT state 
FROM   airports
ORDER BY state
""",
# --------------------------------
    "sql_select_orig_airports":
"""
SELECT city, code
FROM   airports
WHERE  state = '{origin_state}'
""",
# --------------------------------
    "sql_select_dest_states":
"""
SELECT 	DISTINCT b.state 
FROM 	airports_routes a 
INNER JOIN 
		airports b 
ON 		a.dest_code = b.code 
WHERE 	a.origin_code = '{origin_airport_code}'
ORDER BY b.state
""",
# --------------------------------
    "sql_select_dest_airports":
"""
SELECT DISTINCT b.city, b.code 
FROM   airports_routes a 
INNER JOIN 
       airports b 
ON     a.dest_code = b.code 
WHERE  a.origin_code = '{origin_airport_code}' 
AND    b.state = '{dest_state}' 
ORDER BY b.city
""",
# --------------------------------
    "sql_select_dest_airlines":
"""
SELECT DISTINCT a.op_carrier_name, a.op_unique_carrier 
FROM   airlines a 
INNER JOIN 
       airline_routes b 
ON     a.op_carrier_airline_id = b.op_carrier_airline_id 
WHERE  b.origin_code = '{origin_airport_code}' 
AND    b.dest_code = '{dest_airport_code}' 
ORDER BY op_carrier_name
""",
}

# Configuration for FlightDelayPredictor machine learning model
ModelConfig = {
    "origin_encode_file":"pickle_files/Origin_encoder.pkl",
    "dest_encode_file":"pickle_files/Dest_encoder.pkl",
    "scaler_file":"pickle_files/scaler.pkl",
    "model_file":"pickle_files/model_dt.pkl"
}

# Configuration for airport weather object
AirportWeatherConfig = {
    "host":host,
    "port":"5432", 
    "user":user, 
    "password":password, 
    "database":"flightsdata",
    "database_type":"postgresql",
# --------------------------------
    "sql_select_airport_hourly_weather":
"""
SELECT cloudcover, precipitation, windspeed, humidity, visibility
FROM   airport_weather
WHERE  code = '{airport_code}'
AND    date = '{date}'
ORDER BY HOUR
""",

}
