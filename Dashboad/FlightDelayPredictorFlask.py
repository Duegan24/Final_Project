from flask import Flask, render_template, request, jsonify
from FlightDelayPredictor import FlightDelayPredictor


app = Flask(__name__)

predictor = FlightDelayPredictor()

@app.route("/")
def flight_delay_predictor():
   return render_template("FlightDelayPredictor.html")

@app.route("/get_origin_states")
def get_origin_states():

   origin_states_list = predictor.get_origin_states()

   return jsonify(origin_states_list)

@app.route("/get_origin_state_airports")
def get_origin_state_airports():

   origin_state_code = request.args.get("origin_state_code")
   origin_state_airports_list = predictor.get_origin_state_airports(origin_state_code)

   return jsonify(origin_state_airports_list)

@app.route("/get_dest_states")
def get_dest_states():

   date = request.args.get("date")
   origin_airport_code = request.args.get("origin_airport_code")
   dest_states_list = predictor.get_dest_states(date, origin_airport_code)

   return jsonify(dest_states_list)

@app.route("/get_dest_state_airports")
def get_dest_state_airports():

   date = request.args.get("date")
   origin_airport_code = request.args.get("origin_airport_code")
   dest_state_code = request.args.get("dest_state_code")
   dest_state_airports_list = predictor.get_dest_state_airports(date, origin_airport_code, dest_state_code)

   return jsonify(dest_state_airports_list)

@app.route("/get_dest_flight_info")
def get_dest_flight_info():

   date = request.args.get("date")
   origin_airport_code = request.args.get("origin_airport_code")
   dest_airport_code = request.args.get("dest_airport_code")
   dest_flight_info = predictor.get_dest_flight_info(date, origin_airport_code, dest_airport_code)

   return jsonify(dest_flight_info)


if __name__ == "__main__":
    app.run(debug=True)