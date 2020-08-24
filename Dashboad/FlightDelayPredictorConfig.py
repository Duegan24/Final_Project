databaseConfig = {
    "host":"localhost", 
    "port":"5432", 
    "user":"postgres", 
    "password":"password", 
    "database":"dashboard",
    "sql_select_orig_states": "SELECT DISTINCT state FROM airports ORDER BY state",
    "sql_select_orig_airports":"SELECT city, code FROM airports WHERE state = '{origin_state}'",
    "sql_select_dest_states": "SELECT DISTINCT c.state FROM airports a INNER JOIN flight_data b ON a.code = b.origin INNER JOIN airports c ON b.dest = c.code WHERE a.code = '{origin_airport_code}'  ORDER BY c.state",
    "sql_select_dest_airports": "SELECT DISTINCT b.city, b.code FROM flight_data a INNER JOIN airports b ON a.dest = b.code WHERE a.origin = '{origin_airport_code}' AND b.state = '{dest_state}' ORDER BY b.city",
    "sql_select_dest_airlines": "SELECT DISTINCT a.op_carrier_name, a.op_unique_carrier FROM airlines a INNER JOIN flight_data b ON a.op_carrier_airline_id = b.op_carrier_airline_id WHERE b.origin = '{origin_airport_code}' AND b.dest = '{dest_airport_code}' ORDER BY op_carrier_name",
}