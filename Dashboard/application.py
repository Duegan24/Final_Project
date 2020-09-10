
import sys
from flask import Flask, render_template, request, jsonify
from FlightDelayPredictor import FlightDelayPredictor

for param in sys.argv:
   if param == "-logoutput":
      log_output = True
   else:
      log_output = False


application = Flask(__name__)

predictor = FlightDelayPredictor()

predict_delay_hours_list = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,19]

@application.route("/")
def flight_delay_predictor():
   return render_template("FlightDelayPredictor.html")


# Gets list of states for all the airports
@application.route("/get_select_opts_origin_states")
def get_select_opt_origin_states():

   select_option_list = predictor.get_origin_states()

   select_option_list = convert_to_opt_name_value_list(select_option_list)

   select_option_list.insert(0, ("",""))

   return convert_to_JSON(select_option_list)

# Get a list of origin airports for the state specified
@application.route("/get_select_opts_origin_airports")
def get_origin_state_airports():

   origin_state = request.args.get("origin_state")

   select_option_list = predictor.get_origin_airports(origin_state)

   select_option_list.insert(0, ("",""))

   return convert_to_JSON(select_option_list)

# Gets a list of destination states for the origin airport specified
@application.route("/get_select_opts_dest_states")
def get_dest_states():

   origin_airport_code = request.args.get("origin_airport_code")
   dest_states_list = predictor.get_dest_states(origin_airport_code)
   
   select_option_list = convert_to_opt_name_value_list(dest_states_list)

   select_option_list.insert(0, ("",""))

   return convert_to_JSON(select_option_list)

# Gets a list of airports for the destination state specified
# accessable from a origin airport
@application.route("/get_select_opts_dest_airports")
def get_dest_state_airports():

   origin_airport_code = request.args.get("origin_airport_code")
   dest_state = request.args.get("dest_state")

   select_option_list = predictor.get_dest_state_airports(origin_airport_code, dest_state)

   select_option_list.insert(0, ("",""))

   return convert_to_JSON(select_option_list)

# Get a list of airline with flight from the origin to the destination airport specified
@application.route("/get_select_opts_dest_airlines")
def get_dest_flight_info():

   origin_airport_code = request.args.get("origin_airport_code")
   dest_airport_code = request.args.get("dest_airport_code")

   select_option_list = predictor.get_dest_airlines(origin_airport_code, dest_airport_code)

   select_option_list.insert(0, ("",""))

   return convert_to_JSON(select_option_list)

# Gets the hourly weather data and delay prediction for the 
# origin airport, destination airport, airline, and travel date specified
@application.route("/get_flight_predict_data")
def get_flight_predict_data():

   origin_airport_code = request.args.get("origin_airport_code")
   dest_airport_code   = request.args.get("dest_airport_code")
   airline_id          = request.args.get("airline_id")
   travel_date         = request.args.get("travel_date")

   flight_predict_data = predictor.get_flight_predict_data(predict_delay_hours_list, origin_airport_code, dest_airport_code, airline_id, travel_date)

   # Convert from metric to US units
   for flight_predict_data_row in flight_predict_data:
      
      #convert to mph
      flight_predict_data_row["wind"] = str(round(float(flight_predict_data_row["wind"]) * 0.62137119, 1))

      #convert to inches
      flight_predict_data_row["precipitation"] = str(round(float(flight_predict_data_row["precipitation"]) * 0.03937008, 3))

   return convert_to_JSON(flight_predict_data)


# Jsonify the return data list
def convert_to_JSON(list):
   

   if log_output == True:

      print(list)

   json = jsonify(list)

   if log_output:
      print(json)

   return json

# If the data retured from the database has only one column
# convert it to two identical columns so that there will be data
# to populate the select option name field and the option value field
def convert_to_opt_name_value_list(singleList): 
      
    return [(singleList[i][0], singleList[i][0]) for i in range(0, len(singleList))] 

if __name__ == "__main__":
    application.run(debug=True)