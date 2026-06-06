import streamlit as st

import pickle

import pandas as pd
import numpy as np


st.set_page_config(page_title="viz Demo")

with open('df.pkl','rb') as file:
    df=pickle.load(file)


with open('pipeline.pkl','rb') as file:
    pipeline=pickle.load(file)




st.header("Enter your input")

property_type=st.selectbox('property type',['flat','house'])

sector=st.selectbox('sector',sorted(df['sector'].unique().tolist()))

bedroom=float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))


bathroom=float(st.selectbox('Number of Bathroom',sorted(df['bathroom'].unique().tolist())))



balcony=st.selectbox('Number of Balcony',sorted(df['balcony'].unique().tolist()))


property_age=st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

store_room = st.selectbox('Store Room', [0.0, 1.0])

built_up_area=float(st.number_input('Built-up_area'))

servant_room=st.selectbox('Servant Room',[0.0,1.0])

furnishing_type = st.selectbox(
    'Furnishing Type',
    sorted(df['furnishing_type'].unique().tolist())
)

luxury_category = st.selectbox(
    'Luxury Category',
    sorted(df['luxury_category'].unique().tolist())
)

floor_category = st.selectbox(
    'Floor Category',
    sorted(df['floor_category'].unique().tolist())
)


if st.button('Predict'):

    data = [[property_type, sector, bedroom, bathroom, balcony,
             property_age, built_up_area, servant_room,
             store_room, furnishing_type, luxury_category,
             floor_category]]

    columns = ['property_type', 'sector', 'bedRoom', 'bathroom',
               'balcony', 'agePossession', 'built_up_area',
               'servant room', 'store room', 'furnishing_type',
               'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    st.dataframe(one_df)
             
    
    prediction = np.expm1(pipeline.predict(one_df))[0]

    low = prediction - 0.22
    high = prediction + 0.22

    st.text(f"Estimated Price: {prediction:.2f} Cr")
    st.text(f"The price of the property is between {low:.2f} Cr and {high:.2f} Cr")
           






             