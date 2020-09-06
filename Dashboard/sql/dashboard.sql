--***** Table: public.airports_total_flights *****

CREATE TABLE public.airports_total_flights
(
    code character(3) COLLATE pg_catalog."default",
    total_flights integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.airports_total_flights
    OWNER to postgres;

CREATE INDEX fki_fk_code
    ON public.airports_total_flights USING btree
    (code COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

--***** Table: public.airports *****

CREATE TABLE public.airports
(
    code character(3) COLLATE pg_catalog."default" NOT NULL,
    city text COLLATE pg_catalog."default" NOT NULL,
    state character varying(200) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT airports_pk_code PRIMARY KEY (code)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.airports
    OWNER to postgres;

CREATE UNIQUE INDEX airports_clidx_code
    ON public.airports USING btree
    (code COLLATE pg_catalog."default" ASC NULLS FIRST)
    TABLESPACE pg_default;

ALTER TABLE public.airports
    CLUSTER ON airports_clidx_code;

CREATE INDEX airports_idx_state
    ON public.airports USING btree
    (state COLLATE pg_catalog."default" ASC NULLS FIRST)
    TABLESPACE pg_default;


-- This query should return 0 rows
SELECT *
FROM   airports
WHERE  code NOT IN (SELECT code FROM airports_total_flights)

--***** Table: public.airports_origin_dest *****

CREATE TABLE public.airports_routes
(
    origin_code character(3) COLLATE pg_catalog."default" NOT NULL,
    dest_code character(3) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT airports_routes_pk_origin_dest PRIMARY KEY (origin_code, dest_code),
    CONSTRAINT airports_routes_fk_dest_code FOREIGN KEY (dest_code)
        REFERENCES public.airports (code) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT airports_routes_fk_origin_code FOREIGN KEY (origin_code)
        REFERENCES public.airports (code) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.airports_routes
    OWNER to postgres;

CREATE INDEX airports_routes_clidx_origin_code
    ON public.airports_routes USING btree
    (origin_code COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE public.airports_routes
    CLUSTER ON airports_routes_clidx_origin_code;

CREATE INDEX airports_routes_fki_dest_code
    ON public.airports_routes USING btree
    (dest_code COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX airports_routes_fki_origin_code
    ON public.airports_routes USING btree
    (origin_code COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

TRUNCATE TABLE airports_routes

INSERT 	INTO public.airports_routes
SELECT 	DISTINCT origin, dest
FROM 	public.flight_data_2019
WHERE 	origin IN (SELECT code FROM public.airports)
AND   	dest   IN (SELECT code FROM public.airports)

UNION

SELECT 	DISTINCT origin, dest
FROM 	public.flight_data_2020
WHERE 	origin IN (SELECT code FROM public.airports)
AND   	dest   IN (SELECT code FROM public.airports)


-- This queries should return 0 rows
SELECT 	*
FROM 	public.airports_routes
WHERE 	origin_code NOT IN (SELECT code FROM public.airports)
AND   	dest_code   NOT IN (SELECT code FROM public.airports)

--***** Table: public.airlines *****

CREATE TABLE public.airlines
(
    op_carrier_airline_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    op_unique_carrier character(2) COLLATE pg_catalog."default" NOT NULL,
    op_carrier_name character varying(30) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT airlines_pk_const_op_carrier_airline_id PRIMARY KEY (op_carrier_airline_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.airlines
    OWNER to postgres;

CREATE UNIQUE INDEX airline_clidx_op_carrier_airline_id
    ON public.airlines USING btree
    (op_carrier_airline_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE public.airlines
    CLUSTER ON airline_clidx_op_carrier_airline_id;
	
	
--***** Table: public.airline_routes *****

CREATE TABLE public.airlines
(
    op_carrier_airline_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    op_unique_carrier character(2) COLLATE pg_catalog."default" NOT NULL,
    op_carrier_name character varying(30) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT airlines_pk_const_op_carrier_airline_id PRIMARY KEY (op_carrier_airline_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.airlines
    OWNER to postgres;

CREATE UNIQUE INDEX airline_clidx_op_carrier_airline_id
    ON public.airlines USING btree
    (op_carrier_airline_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

ALTER TABLE public.airlines
    CLUSTER ON airline_clidx_op_carrier_airline_id;


TRUNCATE TABLE public.airline_routes

INSERT 	INTO public.airline_routes
SELECT 	DISTINCT op_carrier_airline_id, origin, dest
FROM 	public.flight_data_2019
WHERE	op_carrier_airline_id IN (SELECT op_carrier_airline_id FROM public.airlines) 	
AND 	origin IN (SELECT code FROM public.airports)
AND   	dest   IN (SELECT code FROM public.airports)

UNION

SELECT 	DISTINCT op_carrier_airline_id, origin, dest
FROM 	public.flight_data_2020
WHERE	op_carrier_airline_id IN (SELECT op_carrier_airline_id FROM public.airlines) 	
AND 	origin IN (SELECT code FROM public.airports)
AND   	dest   IN (SELECT code FROM public.airports)


