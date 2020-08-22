-- View: public.dash_v_origin_state_airports

-- DROP VIEW public.dash_v_origin_state_airports;

CREATE OR REPLACE VIEW public.dash_v_origin_state_airports
AS
SELECT DISTINCT
 	   airports.state  AS origin_state,
       airports.city   AS airport_option_name,
       airports.code   AS airport_option_value
FROM airports
ORDER BY airports.city;

ALTER TABLE public.dash_v_origin_state_airports
    OWNER TO postgres;

