import sys
from flask import Flask, render_template, request, jsonify
from FlightDelayPredictor import FlightDelayPredictor

for param in sys.argv:
   if param == "-logoutput":
      log_output = True
   else:
      log_output = False


app = Flask(__name__)

predictor = FlightDelayPredictor()

@app.route("/")
def flight_delay_predictor():
   return render_template("FlightDelayPredictor.html")

@app.route("/get_select_opts_origin_states")
def get_select_opt_origin_states():

   select_option_list = predictor.get_origin_states()

   select_option_list = convert_to_opt_name_value_list(select_option_list)

   select_option_list.insert(0, ("",""))

   return convert_to_JSON(select_option_list)


@app.route("/get_select_opts_origin_airports")
def get_origin_state_airports():

   origin_state = request.args.get("origin_state")

   select_option_list = predictor.get_origin_airports(origin_state)

   select_option_list.insert(0, ("",""))

   return convert_to_JSON(select_option_list)

@app.route("/get_select_opts_dest_states")
def get_dest_states():

   origin_airport_code = request.args.get("origin_airport_code")
   dest_states_list = predictor.get_dest_states(origin_airport_code)
   
   select_option_list = convert_to_opt_name_value_list(dest_states_list)

   select_option_list.insert(0, ("",""))

   return convert_to_JSON(select_option_list)

@app.route("/get_select_opts_dest_airports")
def get_dest_state_airports():

   origin_airport_code = request.args.get("origin_airport_code")
   dest_state = request.args.get("dest_state")

   select_option_list = predictor.get_dest_state_airports(origin_airport_code, dest_state)

   select_option_list.insert(0, ("",""))

   return convert_to_JSON(select_option_list)

@app.route("/get_select_opts_dest_airlines")
def get_dest_flight_info():

   origin_airport_code = request.args.get("origin_airport_code")
   dest_airport_code = request.args.get("dest_airport_code")

   select_option_list = predictor.get_dest_airlines(origin_airport_code, dest_airport_code)

   select_option_list.insert(0, ("",""))

   return convert_to_JSON(select_option_list)

@app.route("/get_flight_predict_data")
def get_flight_predict_data():

   origin_airport_code = request.args.get("origin_airport_code")
   dest_airport_code   = request.args.get("dest_airport_code")
   travel_date         = request.args.get("travel_date")

   flight_predict_data = predictor.get_flight_predict_data(origin_airport_code, dest_airport_code, travel_date)

   return convert_to_JSON(flight_predict_data)

def convert_to_JSON(list):
   

   if log_output == True:
      print(list)

   json = jsonify(list)

   if log_output:
      print(json)

   return json

def convert_to_opt_name_value_list(singleList): 
      
    return [(singleList[i][0], singleList[i][0]) for i in range(0, len(singleList))] 

if __name__ == "__main__":
    app.run(debug=True)