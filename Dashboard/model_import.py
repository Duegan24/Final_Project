# Load Dependencies
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Import Encoder Information for origin and destination
le_origin = pickle.load(open('pickle_files/Origin_encoder.pkl', 'rb')) 
le_dest = pickle.load(open('pickle_files/Dest_encoder.pkl', 'rb'))

# load the scaler for all input columns
scaler = pickle.load(open('pickle_files/scaler.pkl', 'rb'))

# Load the model
model_dt = pickle.load(open('pickle_files/model_dt.pkl', 'rb'))

# Create Method that runs a singe set of user defined options through the model
def flight_delay_model(op_carrier, origin, dest, windspeedKmph, precipMM):

    # Setup input dataframe with what the model was trained with
    ## set column names
    input_columns = ['origin', 'dest', 'DEP_Hour', 'windspeedKmph', 'precipMM', 'Carrier_9E'
                    , 'Carrier_AA', 'Carrier_AS', 'Carrier_B6', 'Carrier_DL', 'Carrier_EV'
                    , 'Carrier_F9', 'Carrier_G4', 'Carrier_HA', 'Carrier_MQ', 'Carrier_NK'
                    , 'Carrier_OH', 'Carrier_OO', 'Carrier_UA', 'Carrier_WN', 'Carrier_YV'
                    , 'Carrier_YX']

    ## Setup the actual dataframe
    inputs_df = pd.DataFrame(columns = input_columns)

    ## Create set date to put into model
    inputs_df['DEP_Hour'] = range(4, 17, 1)
    inputs_df['origin'] = origin
    inputs_df['dest'] = dest
    inputs_df['windspeedKmph'] = windspeedKmph
    inputs_df['precipMM'] = precipMM
    carrier_column = "Carrier_" + op_carrier
    inputs_df[carrier_column] = 1

    ## Remove all NAN since that is not how the model was trained.
    inputs_df = inputs_df.fillna(0)

    # Encode Data
    ## create new dataframe so it will be easy to compare to later
    inputs_df_encoded = inputs_df

    ## Encode origin and destination data
    inputs_df_encoded['origin'] = le_origin.transform(inputs_df['origin'])
    inputs_df_encoded['dest'] = le_dest.transform(inputs_df['dest'])

    ## scale all the input data table
    inputs_scaled = scaler.transform(inputs_df_encoded)

    # Run the inputs through the model to get predicted results
    y_pred = model_dt.predict(inputs_scaled)

    outputs_df = inputs_df.copy()
    outputs_df['delayed'] = y_pred

    return outputs_df

