create table flight_data (
	DAY_OF_MONTH text null,
	DAY_OF_WEEK text null,
	OP_UNIQUE_CARRIER text null,
	OP_CARRIER_AIRLINE_ID text null,
	OP_CARRIER text null,
	TAIL_NUM text null,
	OP_CARRIER_FL_NUM text null,
	ORIGIN_AIRPORT_ID text null,
	ORIGIN_AIRPORT_SEQ_ID text null,
	ORIGIN text null,
	DEST_AIRPORT_ID text null,
	DEST_AIRPORT_SEQ_ID text null,
	DEST text null,
	DEP_TIME text null,
	DEP_DEL15 text null,
	DEP_TIME_BLK text null,
	ARR_TIME text null,
	ARR_DEL15 text null,
	CANCELLED text null,
	DIVERTED text null,
	DISTANCE text null,
	BLANK text
);

delete from flight_data
where DAY_OF_MONTH is null
or DAY_OF_WEEK is null
or OP_UNIQUE_CARRIER is null
or OP_CARRIER_AIRLINE_ID is null
or OP_CARRIER is null
or TAIL_NUM is null
or OP_CARRIER_FL_NUM is null
or ORIGIN_AIRPORT_ID is null
or ORIGIN_AIRPORT_SEQ_ID is null
or ORIGIN is null
or DEST_AIRPORT_ID is null
or DEST_AIRPORT_SEQ_ID is null
or DEST is null
or DEP_TIME is null
or DEP_DEL15 is null
or DEP_TIME_BLK is null
or ARR_TIME is null
or ARR_DEL15 is null
or CANCELLED is null
or DIVERTED is null
or DISTANCE is null

select count(*) from flight_data