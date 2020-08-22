-- View: public.dash_v_origin_states

-- DROP VIEW public.dash_v_origin_states;

CREATE OR REPLACE VIEW public.dash_v_origin_states
AS
SELECT DISTINCT 
       airports.state AS state_option_name,
       airports.state AS state_option_value
FROM airports
ORDER BY airports.state;

ALTER TABLE public.dash_v_origin_states
    OWNER TO postgres;

