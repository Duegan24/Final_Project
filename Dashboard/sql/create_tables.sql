-- Table: public.airlines

-- DROP TABLE public.airlines;

CREATE TABLE public.airlines
(
    op_carrier_airline_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    op_unique_carrier character(2) COLLATE pg_catalog."default" NOT NULL,
    op_carrier_name character varying(30) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT airlines_pkey PRIMARY KEY (op_carrier_airline_id)
);

	
-- Table: public.airports

-- DROP TABLE public.airports;

CREATE TABLE public.airports
(
    code character(3) COLLATE pg_catalog."default" NOT NULL,
    city text COLLATE pg_catalog."default" NOT NULL,
    state character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT airports_pkey PRIMARY KEY (code, city)
);

	
-- Table: public.flight_data

-- DROP TABLE public.flight_data;

CREATE TABLE public.flight_data
(
    day_of_month text COLLATE pg_catalog."default",
    day_of_week text COLLATE pg_catalog."default",
    op_unique_carrier text COLLATE pg_catalog."default",
    op_carrier_airline_id text COLLATE pg_catalog."default",
    op_carrier text COLLATE pg_catalog."default",
    tail_num text COLLATE pg_catalog."default",
    op_carrier_fl_num text COLLATE pg_catalog."default",
    origin_airport_id text COLLATE pg_catalog."default",
    origin_airport_seq_id text COLLATE pg_catalog."default",
    origin text COLLATE pg_catalog."default",
    dest_airport_id text COLLATE pg_catalog."default",
    dest_airport_seq_id text COLLATE pg_catalog."default",
    dest text COLLATE pg_catalog."default",
    dep_time text COLLATE pg_catalog."default",
    dep_del15 text COLLATE pg_catalog."default",
    dep_time_blk text COLLATE pg_catalog."default",
    arr_time text COLLATE pg_catalog."default",
    arr_del15 text COLLATE pg_catalog."default",
    cancelled text COLLATE pg_catalog."default",
    diverted text COLLATE pg_catalog."default",
    distance text COLLATE pg_catalog."default",
    blank text COLLATE pg_catalog."default"
);