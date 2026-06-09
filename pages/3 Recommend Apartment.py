import streamlit as st
import pickle
import numpy as np
import pandas as pd
st.set_page_config(page_title="Recommend Apartment")
location_df=pickle.load(open('location_distance.pkl', 'rb'))
cosine_sim1=pickle.load(open('cosine_sim1.pkl', 'rb'))
cosine_sim2=pickle.load(open('cosine_sim2.pkl', 'rb'))
cosine_sim3=pickle.load(open('cosine_sim3.pkl', 'rb'))

def recommend_properties_with_scores(property_name, top_n=5):

    cosine_sim_matrix = (
        0.5 * cosine_sim1
        + 0.8 * cosine_sim2
        + 1 * cosine_sim3
    )

    # Find index of selected property
    idx = location_df.index.get_loc(property_name)

    # Similarity scores
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))

    # Sort by similarity
    sorted_scores = sorted(
        sim_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Top 5 recommendations (excluding itself)
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Property names
    top_properties = location_df.index[top_indices].tolist()

    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df
st.title("Select Location and Radius")

selected_location = st.selectbox('Location',sorted(location_df.columns.to_list()))

radius=st.number_input('Radius in Kms')

if st.button('Search'):
    result_ser=location_df[location_df[selected_location]<=radius*1000][
     selected_location].sort_values()  
    
    for key,value in result_ser.items():
        st.text(str(key)+" "+str(round(value/1000))+'Kms')


st.title('Recommend Apartment')
selected_apartment = st.selectbox('Select an apartment', sorted(location_df.index.to_list()))

if st.button('Recommend'):
    recommendations_df = recommend_properties_with_scores(selected_apartment)

    st.dataframe(recommendations_df)
    





             
