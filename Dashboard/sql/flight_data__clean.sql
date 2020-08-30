-- Table: public.flight_data

-- DROP TABLE public.flight_data;

DELETE FROM public.flight_data
WHERE day_of_month IS NULL
OR day_of_week IS NULL
OR op_unique_carrier IS NULL
OR op_carrier_airline_id IS NULL
OR op_carrier IS NULL
OR tail_num IS NULL
OR op_carrier_fl_num IS NULL
OR origin_airport_id IS NULL
OR origin_airport_seq_id IS NULL
OR origin IS NULL
OR dest_airport_id IS NULL
OR dest_airport_seq_id IS NULL
OR dest IS NULL
OR dep_time IS NULL
OR dep_del15 IS NULL
OR dep_time_blk IS NULL
OR arr_time IS NULL
OR arr_del15 IS NULL
OR cancelled IS NULL
OR diverted IS NULL
OR distance IS NULL
