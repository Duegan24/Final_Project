SELECT DISTINCT state 
FROM   airports
ORDER BY state

SELECT city, code
FROM   airports
WHERE  state = '{origin_state}'

SELECT 	DISTINCT b.state 
FROM 	airports_routes a 
INNER JOIN 
		airports b 
ON 		a.dest_code = b.code 
WHERE 	a.origin_code = '{origin_airport_code}'
ORDER BY b.state

SELECT DISTINCT b.city, b.code 
FROM   airports_routes a 
INNER JOIN 
       airports b 
ON     a.dest_code = b.code 
WHERE  a.origin_code = '{origin_airport_code}' 
AND    b.state = '{dest_state}' 
ORDER BY b.city

SELECT DISTINCT a.op_carrier_name, a.op_unique_carrier 
FROM   airlines a 
INNER JOIN 
       airline_routes b 
ON     a.op_carrier_airline_id = b.op_carrier_airline_id 
WHERE  b.origin_code = '{origin_airport_code}' 
AND    b.dest_code = '{dest_airport_code}' 
ORDER BY op_carrier_name

SELECT cloudcover, precipitation, windspeed, humidity, visibility
FROM   airport_weather
WHERE  code = '{airport_code}'
AND    date = '{date}'
ORDER BY HOUR
