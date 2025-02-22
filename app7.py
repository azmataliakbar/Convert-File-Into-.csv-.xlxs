import streamlit as st
import random

# Title
st.title("🌱 Growth Mindset Challenge")
st.write("Welcome to the Growth Mindset Challenge! Train your brain to embrace learning and perseverance.")

# Growth Mindset Quotes
quotes = [
    "Failure is an opportunity to grow.",
    "I can learn anything I want to.",
    "Challenges help me grow.",
    "My effort and attitude determine my abilities.",
    "Feedback is constructive.",
    "I am inspired by the success of others."
]
if st.button("Get a Motivational Quote ✨"):
    st.write(random.choice(quotes))

# Growth Mindset Quiz
st.header("🧠 Growth Mindset Quiz")
st.write("Answer the following questions to check your mindset!")

questions = {
    "Do you believe intelligence can be developed?": ["Yes", "No"],
    "How do you see challenges?": ["Opportunities to grow", "Something to avoid"],
    "What do you do after making a mistake?": ["Learn from it", "Feel discouraged"]
}

score = 0
for q, options in questions.items():
    answer = st.radio(q, options)
    if answer == options[0]:
        score += 1

if st.button("Submit Quiz"):
    if score == len(questions):
        st.success("🎉 Great! You have a strong growth mindset!")
    else:
        st.warning("💡 Keep practicing a growth mindset!")

# Reflection Journal
st.header("✍️ Reflection Journal")
reflection = st.text_area("Write about a challenge you faced today and what you learned from it:")
if st.button("Save Reflection"):
    st.success("Your reflection has been saved! Keep growing! 🚀")

# Footer
st.write("---")
st.write("*Built with ❤️ using Streamlit.*")


# pip install streamlit
# streamlit run app7.py