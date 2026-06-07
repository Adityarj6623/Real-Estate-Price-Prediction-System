import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns


# Page configuration
st.set_page_config(page_title="Plotting Demo")

# Title
st.title("Analytics")

# Load dataset
new_df = pd.read_csv('data_viz1.csv')

feature_text=pickle.load(open('feature_text.pkl', 'rb'))


# Group data by sector and calculate mean values
group_df = new_df.groupby('sector').mean(numeric_only=True)[
    ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
]



st.title('Scatter Map of Price per Sqft by Location')
# Create scatter map
fig = px.scatter_mapbox(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size="built_up_area",
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    mapbox_style="open-street-map",
    width=1200,
    height=700,
    hover_name=group_df.index
)

# Display plot
st.plotly_chart(fig, use_container_width=True)

st.title('Word Cloud of Features')

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='white',
    stopwords=set(['s']),
    min_font_size=10
).generate(feature_text)

fig, ax = plt.subplots(figsize=(8, 8))

ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")

st.pyplot(fig)

st.header('Area vs Price')


property_type = st.selectbox('select property type',['flat','house'])

if property_type=='house':
        fig = px.scatter(new_df[new_df['property_type']=='house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

# Show the plot
        st.plotly_chart(fig, use_container_width=True)
else:
        fig = px.scatter(new_df[new_df['property_type']=='flat'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

        st.plotly_chart(fig, use_container_width=True)




st.header('BHK Pie Chart')

sector_option = new_df['sector'].unique().tolist()
sector_option.insert(0, 'All')

selected_sector = st.selectbox('select sector', sector_option)

# filter data
if selected_sector == 'All':
    temp_df = new_df
else:
    temp_df = new_df[new_df['sector'] == selected_sector]

# pie chart
fig2 = px.pie(
    temp_df,
    names='bedRoom',
    title='Distribution of BHK'
)

st.plotly_chart(fig2, use_container_width=True)



st.header('Side by Side BHK price comparison')

fig3=px.box(new_df[new_df['bedRoom']<=4], x='bedRoom', y='price', color='property_type', title='BHK Price Comparison')
st.plotly_chart(fig3, use_container_width=True)



st.header('Side by Side Distplot for property type')
fig3=plt.figure(figsize=(10,4))

sns.distplot(new_df[new_df['property_type']=='house']['price'], label='house')
sns.distplot(new_df[new_df['property_type']=='flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)


