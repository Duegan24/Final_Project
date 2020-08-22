databaseConfig = {
    "host":"localhost", 
    "port":"5432", 
    "user":"postgres", 
    "password":"password", 
    "database":"dashboard",
    "sql_select_orig_states": "SELECT DISTINCT state FROM airports ORDER BY state",
    "sql_select_orig_airports":"SELECT city, code FROM airports WHERE state = '{origin_state}'",
    "sql_select_dest_states": "SELECT DISTINCT c.state FROM airports a INNER JOIN flight_data b ON a.code = b.origin INNER JOIN airports c ON b.dest = c.code WHERE a.code = '{origin_airport_code}'  ORDER BY c.state"
}