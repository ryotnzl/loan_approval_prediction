import streamlit as st
import requests

# FastAPI URL (ensure FastAPI backend is running)
API_URL = "http://127.0.0.1:8000/predict/"

# Title
st.title("Loan Risk Prediction App")

# Collect user inputs
Income = st.number_input("Income", min_value=0, step=1000)
Age = st.number_input("Age", min_value=18, max_value=100, step=1)
Experience = st.number_input("Work Experience (Years)", min_value=0, step=1)
CURRENT_JOB_YRS = st.number_input("Years in Current Job", min_value=0, step=1)
CURRENT_HOUSE_YRS = st.number_input("Years in Current House", min_value=0, step=1)

Married_Single = st.selectbox("Marital Status", ["married", "single"])
House_Ownership = st.selectbox("House Ownership", ["owned", "rented", "norent_noown"])
Car_Ownership = st.selectbox("Car Ownership", ["yes", "no"])
Profession = st.text_input("Profession")
CITY = st.text_input("City")
STATE = st.text_input("State")

# Submit button
if st.button("Predict Loan Risk"):
    # Create input dictionary
    input_data = {
        "Income": Income,
        "Age": Age,
        "Experience": Experience,
        "Married_Single": Married_Single,
        "House_Ownership": House_Ownership,
        "Car_Ownership": Car_Ownership,
        "Profession": Profession,
        "CITY": CITY,
        "STATE": STATE,
        "CURRENT_JOB_YRS": CURRENT_JOB_YRS,
        "CURRENT_HOUSE_YRS": CURRENT_HOUSE_YRS
    }

    # Make prediction request
    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Loan Risk Prediction: {result['risk_flag']} (Probability: {result['probability']:.2f})")
    else:
        st.error("Error making prediction")
