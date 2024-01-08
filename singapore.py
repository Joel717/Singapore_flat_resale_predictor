# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle

# Load data
data = pd.read_csv(r"C:\\Users\\devli\\sghousing\\data.csv")



# Create dictionary to get the encoded values
town_dict = dict(zip(data['town'].unique(), data['town_code'].unique()))
model_dict = dict(zip(data['flat_model'].unique(), data['flat_modelcode'].unique()))
town_list = data['town'].unique()
model_list = data['flat_model'].unique()
type_cat = {'1 ROOM': 1,
            '2 ROOM': 2,
            '3 ROOM': 3,
            '4 ROOM': 4,
            '5 ROOM': 5,
            'EXECUTIVE': 6,
            'MULTI GENERATION': 7}
type_list = list(type_cat.keys())

# Set page config for the web app
st.set_page_config(page_title='Price Prediction', page_icon=':bar_chart:', layout='wide')
st.title((":red[_Singapore Flat Resale Value Predictor_]"))
# Create columns in UI
col1, col2, col3, col4 = st.columns(4)

with col1:
    # Create input field for year input
    selling_year = st.number_input('Selling Year', value=2022, format="%d", help="yyyy")

with col2:
    # Create input field for month input
    selling_month = int(st.select_slider('Selling month', options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

with col3:
    # Create input field for town
    town_key = st.selectbox('Town', options=town_list)

with col4:
    # Create input field for flat type
    flat_type_key = st.selectbox('Flat Type', options=type_list)

with col1:
    # Create input field for storey range
    storey_range = st.text_input('Storey range', value=None, placeholder="ex: 01 TO 03")

with col2:
    # Create input field for floor area
    floor_area_sqm = st.number_input('Floor Area (sqm)', value=0, help="Type floor area...")

with col3:
    # Create input field for flat model
    flat_model = st.selectbox('Flat Model', options=model_list)

with col4:
    # Create input field for lease commence date
    lease_commence_date = st.text_input('Lease Commence Date', value="", help="Type the year (yyyy)")

# Function to load pickled model
def model_data():
    with open("C:\\Users\\devli\\sghousing\\resale_rfr_pkl", "rb") as files:
        model = pickle.load(files)
    return model

# Function to predict
def predict(model, a, b, c, d, e, f, g, h):
    pred_value = model.predict([[a, b, c, d, e, f, g, h]])
    return pred_value


# Create predict button
if st.button('Predict Price'):
    town = town_dict[town_key]
    flat_type = type_cat[flat_type_key]
    if storey_range is not None:
        storey_min, storey_max = map(int, storey_range.split(" TO "))
    flat_modelcode = model_dict[flat_model]

    # Call predict function
   # Call predict function
    pred = predict(model_data(), selling_year, selling_month, town,storey_min, storey_max,
               floor_area_sqm, flat_modelcode, lease_commence_date)

    # Display predicted price in dollar
    st.success(f'Predicted Price: ${pred[0]:,.2f}')
#creating a sidebar with about section
with st.sidebar:
     st.title(":red[_Singapore Flat Resale Value Predictor_]")
     st.divider()
     st.caption('''This Streamlit app allows users to predict the resale price of a flat 
                by selecting different parameters based on requirement ''')
     st.caption("This App is created as a part of GUVI Master Data Science Program")
     st.caption("This app is created by Joel Gracelin")
     st.write("[Ghithub](https://github.com/Joel717)") 
    
