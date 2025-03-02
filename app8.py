import streamlit as st

# Page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="📏", layout="centered")

# Title and description
st.markdown("<h1 style='text-align: center; color: #8B5CF6;'>BMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #6B7280;'>Enter your height and weight to calculate your BMI.</h4>", unsafe_allow_html=True)

# Input fields for height and weight
height = st.number_input("Height (cm)", min_value=0.0, step=0.1, format="%.1f")
weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1, format="%.1f")

# Error message and result variables
error = ""
bmi = None
category = ""

# Function to calculate BMI
def calculate_bmi():
    global bmi, category, error
    if height <= 0 or weight <= 0:
        error = "Please enter both height and weight as positive numbers."
        return
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    error = ""

# Button to trigger BMI calculation
if st.button("Calculate"):
    calculate_bmi()

# Display error message if any
if error:
    st.error(error)

# Display BMI result if available
if bmi is not None:
    st.markdown(f"<h3 style='text-align: center; color: #2563EB;'>Your BMI: {bmi:.1f}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center; color: #10B981;'>{category}</h4>", unsafe_allow_html=True)

# Author
st.markdown("<h4 style='text-align: center; color: #FF4500;'>Author: Azmat Ali</h4>", unsafe_allow_html=True)
