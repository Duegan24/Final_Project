-- View: public.dash_v_dest_states

-- DROP VIEW public.dash_v_dest_states;

CREATE OR REPLACE VIEW public.dash_v_dest_states
AS
SELECT DISTINCT 
	   a.code  AS origin_airport_code,
       c.state AS state_option_name,
	   c.state AS state_option_value
FROM airports a
JOIN flight_data b ON a.code::text = b.origin
JOIN airports c    ON b.dest = c.code::text
ORDER BY c.state;

ALTER TABLE public.dash_v_dest_states
    OWNER TO postgres;

