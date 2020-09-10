# Load Dependencies
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


class FlightDelayPredictorModel:

    def __init__(self, modelConfig):

        # Initialize model origin and destination encoders
        self.le_origin = pickle.load(open(modelConfig["origin_encode_file"], 'rb')) 
        self.le_dest = pickle.load(open(modelConfig["dest_encode_file"], 'rb'))

        # Initialize model scaler
        self.scaler = pickle.load(open(modelConfig["scaler_file"], 'rb'))

        # Initialize model
        self.model_dt = pickle.load(open(modelConfig["model_file"], 'rb'))

        # Prediction delay model input dataframe columns
        self.model_input_df_columns =  ['origin', 'dest', 'DEP_Hour', 'windspeedKmph', 'precipMM', 'Carrier_9E'
                                        , 'Carrier_AA', 'Carrier_AS', 'Carrier_B6', 'Carrier_DL', 'Carrier_EV'
                                        , 'Carrier_F9', 'Carrier_G4', 'Carrier_HA', 'Carrier_MQ', 'Carrier_NK'
                                        , 'Carrier_OH', 'Carrier_OO', 'Carrier_UA', 'Carrier_WN', 'Carrier_YV'
                                        , 'Carrier_YX']

    def predict_hourly_delays(self, hours_list, op_carrier, origin, dest, windspeedKmph_list, precipMM_list):

        ## Setup the actual dataframe
        inputs_df = pd.DataFrame(columns = self.model_input_df_columns)

        ## Create set date to put into model
        inputs_df['DEP_Hour'] = hours_list
        inputs_df['origin'] = origin
        inputs_df['dest'] = dest
        inputs_df.update({'windspeedKmph': windspeedKmph_list})
        inputs_df.update({'precipMM' : precipMM_list})
        carrier_column = "Carrier_" + op_carrier
        inputs_df[carrier_column] = 1

        ## Remove all NAN since that is not how the model was trained.
        inputs_df = inputs_df.fillna(0)

        # Encode Data
        ## create new dataframe so it will be easy to compare to later
        inputs_df_encoded = inputs_df

        ## Encode origin and destination data
        inputs_df_encoded['origin'] = self.le_origin.transform(inputs_df['origin'])
        inputs_df_encoded['dest'] = self.le_dest.transform(inputs_df['dest'])

        ## scale all the input data table
        inputs_scaled = self.scaler.transform(inputs_df_encoded)

        # Run the inputs through the model to get predicted results
        y_pred = self.model_dt.predict(inputs_scaled)

        outputs_df = inputs_df.copy()
        outputs_df['delayed'] = y_pred

        return outputs_df

