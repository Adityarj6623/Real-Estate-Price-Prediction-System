import streamlit as st

st.set_page_config(
    page_title="Real Estate Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Real Estate Price Prediction System")

st.write("""
Welcome to the Real Estate Price Prediction System.

This application helps users analyze real estate data and predict property prices
using Machine Learning techniques.
""")

st.subheader("Features")

st.markdown("""
- 📊 Exploratory Data Analysis (EDA)
- 📈 Interactive Data Visualizations
- 🤖 Property Price Prediction
- 📍 Location-Based Insights
""")

st.info("👈 Use the sidebar to navigate between different sections of the application.")

st.markdown("---")
st.caption("Built with Streamlit and Machine Learning")