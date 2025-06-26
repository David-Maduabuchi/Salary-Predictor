# basically a streamlit adshboard is a simple interface that connects to
# your model and helps you test and predict prices easily
# observe

import streamlit as st
from src.predict import predict_price

st.set_page_config(page_title="Salary Predictor", layout="centered")
st.title("Salary Predictor Based on Experience")
st.write("Enter the number of years of experience below: ")

# User input # Text input instead of slider
exp_input = st.text_input("Enter your years of experience:", placeholder="e.g. 5")

# Validate and predict
if st.button("Predict Salary"):
    if not exp_input:
        st.warning("🚨 Please enter a value.")
    elif not exp_input.isdigit():
        st.error("❌ Please enter a valid number.")
    else:
        prediction = predict_price(int(exp_input))
        st.success(f"💰 Estimated Salary: ${prediction:,.2f}")
