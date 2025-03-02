import streamlit as st
import time
from PIL import Image
import random

# Page configuration
st.set_page_config(page_title="Birthday Card", page_icon="🎉", layout="centered")

st.title(" Python 🐍 :  Birthday Greeting 🍰")

# Custom function to display animated title
def animated_title(title):
    animated_text = ""
    for char in title:
        animated_text += char
        st.markdown(f"<h1 style='text-align: center; color: #FF6B6B;'>{animated_text}</h1>", unsafe_allow_html=True)
        time.sleep(0.1)
        st.empty()  # Clear previous line to create animation effect

# Function to display confetti
def show_confetti():
    for _ in range(3):
        st.balloons()

# Animated Title and Subtitle
animated_title("🎉 Happy 25th Birthday! 🎉")
st.markdown("<h2 style='text-align: center; color: #02fa51;'>🍰 James Anthony 🍰</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #45B7D1;'> 📜 March 5th 📜</h4>", unsafe_allow_html=True)

# Display candles
st.markdown("### 🕯️ Light the candles 🕯️:")
candles_lit = st.slider("Candles Lit", min_value=0, max_value=5, step=1)
st.progress(candles_lit / 5)

# Display balloons
st.markdown("### 🎈 Pop the balloons 🎈:")
balloons_popped = st.slider("Balloons Popped", min_value=0, max_value=5, step=1)
st.progress(balloons_popped / 5)

# Celebration button
if st.button("🎁 🎁 🎁 Celebrate! 🎁 🎁 🎁"):
    if candles_lit == 5 and balloons_popped == 5:
        st.success("🎉 All candles lit and balloons popped! Let's celebrate! 🎉")
        show_confetti()
    else:
        st.warning("Please light all candles and pop all balloons first!")

# Author
st.markdown("<h4 style='text-align: center; color: #FFA07A;'>Author: Azmat Ali</h4>", unsafe_allow_html=True)

