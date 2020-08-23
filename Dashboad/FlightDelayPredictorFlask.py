from flask import Flask, render_template, request, jsonify
from FlightDelayPredictor import FlightDelayPredictor


app = Flask(__name__)

predictor = FlightDelayPredictor()

@app.route("/")
def flight_delay_predictor():
   return render_template("FlightDelayPredictor.html")

@app.route("/get_select_opts_origin_states")
def get_select_opt_origin_states():

   origin_states_list = predictor.get_origin_states()

   select_option_list = convert_to_opt_name_value_list(origin_states_list)

   select_option_list.insert(0, ["",""])

   return jsonify(select_option_list)

@app.route("/get_select_opts_origin_airports")
def get_origin_state_airports():

   origin_state = request.args.get("origin_state")

   select_option_list = predictor.get_origin_airports(origin_state)

   select_option_list.insert(0, ["",""])

   return jsonify(select_option_list)

@app.route("/get_select_opts_dest_states")
def get_dest_states():

   origin_airport_code = request.args.get("origin_airport_code")
   dest_states_list = predictor.get_dest_states(origin_airport_code)
   
   select_option_list = convert_to_opt_name_value_list(dest_states_list)

   select_option_list.insert(0, ["",""])

   return jsonify(select_option_list)

@app.route("/get_select_opts_dest_airports")
def get_dest_state_airports():

   origin_airport_code = request.args.get("origin_airport_code")
   dest_state = request.args.get("dest_state")

   select_option_list = predictor.get_dest_state_airports(origin_airport_code, dest_state)

   select_option_list.insert(0, ["",""])

   return jsonify(select_option_list)

@app.route("/get_select_opts_dest_airlines")
def get_dest_flight_info():

   origin_airport_code = request.args.get("origin_airport_code")
   dest_airport_code = request.args.get("dest_airport_code")

   select_option_list = predictor.get_dest_airlines(origin_airport_code, dest_airport_code)

   select_option_list.insert(0, ["",""])

   return jsonify(select_option_list)


def convert_to_opt_name_value_list(singleList): 
      
    return [[singleList[i], singleList[i]] for i in range(0, len(singleList))] 

if __name__ == "__main__":
    app.run(debug=True)