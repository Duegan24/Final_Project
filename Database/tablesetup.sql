-- Create 2018 weather table
CREATE TABLE weather_2018 (
	location CHAR(40),
	date_time DATE,
	precipMM float,
	visibility int,
	cloudcover int,
	windspeedKmph int,
	humidity int
);

-- Create 2019 weather table
CREATE TABLE weather_2019 (
	location CHAR(40),
	date_time DATE,
	precipMM float,
	visibility int,
	cloudcover int,
	windspeedKmph int,
	humidity int
);

-- Create 2020 weather table
CREATE TABLE weather_2020 (
	location CHAR(40),
	date_time DATE,
	precipMM float,
	visibility int,
	cloudcover int,
	windspeedKmph int,
	humidity int
);

-- Drop flight_data to import the new flight data
DROP TABLE flight_data

-- Create a new flight data table for 2019 data
CREATE TABLE flight_data_2019(
	ORIGIN CHAR(3),
	ORIGIN_CITY CHAR(40),
	DAY_OF_MONTH DATE,
	DAY_OF_WEEK INT,
	OP_CARRIER_AIRLINE_ID VARCHAR(5),
	OP_CARRIER CHAR(2),
	TAIL_NUM VARCHAR(6),
	OP_CARRIER_FL_NUM VARCHAR(4),
	ORIGIN_AIRPORT_ID VARCHAR(5),
	ORIGIN_AIRPORT_SEQ_ID VARCHAR(7),
	DEST_AIRPORT_ID VARCHAR(5),
	DEST_AIRPORT_SEQ_ID VARCHAR(7),
	DEST CHAR(3),
	DEP_TIME FLOAT,
	DEP_DEL15 FLOAT,
	DEP_TIME_BLK VARCHAR(9),
	ARR_TIME FLOAT,
	ARR_DEL15 FLOAT,
	CANCELLED FLOAT,
	DIVERTED FLOAT,
	DISTANCE INT,
	DEST_CITY CHAR(40)
);

-- Create a new flight data table for 2020 data
CREATE TABLE flight_data_2020(
	ORIGIN CHAR(3),
	ORIGIN_CITY CHAR(40),
	DAY_OF_MONTH DATE,
	DAY_OF_WEEK INT,
	OP_CARRIER_AIRLINE_ID VARCHAR(5),
	OP_CARRIER CHAR(2),
	TAIL_NUM VARCHAR(6),
	OP_CARRIER_FL_NUM VARCHAR(4),
	ORIGIN_AIRPORT_ID VARCHAR(5),
	ORIGIN_AIRPORT_SEQ_ID VARCHAR(7),
	DEST_AIRPORT_ID VARCHAR(5),
	DEST_AIRPORT_SEQ_ID VARCHAR(7),
	DEST CHAR(3),
	DEP_TIME FLOAT,
	DEP_DEL15 FLOAT,
	DEP_TIME_BLK VARCHAR(9),
	ARR_TIME FLOAT,
	ARR_DEL15 FLOAT,
	CANCELLED FLOAT,
	DIVERTED FLOAT,
	DISTANCE INT,
	DEST_CITY CHAR(40)
);

--Full join flight_data and airlines to get a complete dataset
SELECT 
	ORIGIN,
	ORIGIN_CITY,
	DAY_OF_MONTH,
	flight_data_2019.OP_CARRIER_AIRLINE_ID,
	op_carrier_name	
	OP_CARRIER,
	TAIL_NUM,
	OP_CARRIER_FL_NUM,
	ORIGIN_AIRPORT_ID,
	ORIGIN_AIRPORT_SEQ_ID,
	DEST_AIRPORT_ID,
	DEST_AIRPORT_SEQ_ID,
	DEST,
	DEP_TIME,
	DEP_DEL15,
	DEP_TIME_BLK,
	ARR_TIME,
	ARR_DEL15,
	CANCELLED,
	DIVERTED,
	DISTANCE,
	DEST_CITY
INTO full_flight_data_2019
FROM flight_data_2019
FULL JOIN	airlines ON flight_data_2019.OP_CARRIER_AIRLINE_ID = airlines.op_carrier_airline_id;

--Full join flight_data and airlines to get a complete dataset
SELECT 
	ORIGIN,
	ORIGIN_CITY,
	DAY_OF_MONTH,
	flight_data_2020.OP_CARRIER_AIRLINE_ID,
	op_carrier_name	
	OP_CARRIER,
	TAIL_NUM,
	OP_CARRIER_FL_NUM,
	ORIGIN_AIRPORT_ID,
	ORIGIN_AIRPORT_SEQ_ID,
	DEST_AIRPORT_ID,
	DEST_AIRPORT_SEQ_ID,
	DEST,
	DEP_TIME,
	DEP_DEL15,
	DEP_TIME_BLK,
	ARR_TIME,
	ARR_DEL15,
	CANCELLED,
	DIVERTED,
	DISTANCE,
	DEST_CITY
INTO full_flight_data_2020
FROM flight_data_2020
FULL JOIN	airlines ON flight_data_2020.OP_CARRIER_AIRLINE_ID = airlines.op_carrier_airline_id;

-- Rename thne full flight data table
ALTER TABLE full_flight_data
RENAME TO full_flight_2019
