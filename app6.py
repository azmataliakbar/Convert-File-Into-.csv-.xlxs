import streamlit as st
import webbrowser

# Set up page config
st.set_page_config(page_title="Calculator", layout="centered")

# Custom CSS for dark theme and card design
st.markdown("""
    <style>
    /* Global styles */
    body {
        background-color: #0E1117 !important;
        color: white !important;
    }
    
    .stApp {
        background-color: #0E1117 !important;
    }
    
    /* Calculator Card */
    .calculator-card {
        background-color: #262730;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 20px auto;
        max-width: 400px;
    }
    
    /* Display */
    .calculator-display {
        background-color: #1E1E1E;
        color: red !important;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        font-size: 50px;
        text-align: right;
        border: 2px solid lightgray !important;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #363940 !important;
        color: yellow !important;
        border: 2px solid lightgray !important;
        border-radius: 8px !important;
        padding: 15px 0px !important;
        font-size: 3.0rem !important;
        font-weight: bold !important;
        margin: 5px !important;
        width: 100% !important;
        height: 60px !important;
        transition: background-color 0.3s !important;
    }
    
    .stButton button:hover {
        background-color: #4A4D55 !important;
    }
    
    /* Operator buttons */
    .stButton button[data-baseweb="button"]:nth-of-type(4n) {
        background-color: #4CAF50 !important;
    }
    
    .stButton button[data-baseweb="button"]:nth-of-type(4n):hover {
        background-color: #45a049 !important;
    }
    
    /* Title */
    h1 {
        color: yellow;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Result text */
    .result-text {
        color: #02f733;
        font-size: 50px;
        text-align: center;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Calculator title
st.markdown("<h1>🌠 Simple Calculator 🌠</h1>", unsafe_allow_html=True)

# Sidebar for navigation
def main():
    st.sidebar.title("🔍 Navigation")
    st.sidebar.write("Explore these links:")
    
    if st.sidebar.button("📜 Chat GPT"):
        webbrowser.open_new_tab("https://chatgpt.com/")

    if st.sidebar.button("💻 My Project 1"):
        webbrowser.open_new_tab("https://heaven-hills-furniture.netlify.app/")

    if st.sidebar.button("🚀 Deep Seek"):
        webbrowser.open_new_tab("https://chat.deepseek.com/")

    if st.sidebar.button("🔗 Google"):
        webbrowser.open_new_tab("https://www.google.co.uk/")

# Call main to render the sidebar
main()

# Initialize session state
if 'display' not in st.session_state:
    st.session_state.display = '0'
if 'first_number' not in st.session_state:
    st.session_state.first_number = None
if 'operation' not in st.session_state:
    st.session_state.operation = None
if 'reset_next' not in st.session_state:
    st.session_state.reset_next = False

# Function to update display
def update_display(value):
    if st.session_state.reset_next or st.session_state.display == '0':
        st.session_state.display = str(value)
        st.session_state.reset_next = False
    else:
        st.session_state.display += str(value)

# Function to handle operations
def handle_operation(op):
    st.session_state.first_number = float(st.session_state.display)
    st.session_state.operation = op
    st.session_state.reset_next = True

# Function to calculate result
def calculate_result():
    if st.session_state.first_number is not None and st.session_state.operation:
        second_number = float(st.session_state.display)
        if st.session_state.operation == 'add':
            result = st.session_state.first_number + second_number
        elif st.session_state.operation == 'subtract':
            result = st.session_state.first_number - second_number
        elif st.session_state.operation == 'multiply':
            result = st.session_state.first_number * second_number
        elif st.session_state.operation == 'divide':
            if second_number != 0:
                result = st.session_state.first_number / second_number
            else:
                st.error("Cannot divide by zero!")
                result = 0
        
        st.session_state.display = str(result)
        st.session_state.first_number = None
        st.session_state.operation = None
        st.session_state.reset_next = True

# Function to clear calculator
def clear_calculator():
    st.session_state.display = '0'
    st.session_state.first_number = None
    st.session_state.operation = None
    st.session_state.reset_next = False

# Calculator card
with st.container():
    # Display
    st.markdown(f'<div class="calculator-display">{st.session_state.display}</div>', unsafe_allow_html=True)
    
    # Calculator buttons
    cols = st.columns(4)
    
    # Row 1
    cols[0].button('7', on_click=update_display, args=(7,))
    cols[1].button('8', on_click=update_display, args=(8,))
    cols[2].button('9', on_click=update_display, args=(9,))
    cols[3].button('DIVIDE', on_click=handle_operation, args=('divide',))
    
    # Row 2
    cols[0].button('4', on_click=update_display, args=(4,))
    cols[1].button('5', on_click=update_display, args=(5,))
    cols[2].button('6', on_click=update_display, args=(6,))
    cols[3].button('MULTIPLY', on_click=handle_operation, args=('multiply',))
    
    # Row 3
    cols[0].button('1', on_click=update_display, args=(1,))
    cols[1].button('2', on_click=update_display, args=(2,))
    cols[2].button('3', on_click=update_display, args=(3,))
    cols[3].button('SUBTRACT', on_click=handle_operation, args=('subtract',))
    
    # Row 4
    cols[0].button('0', on_click=update_display, args=(0,))
    cols[1].button('.', on_click=lambda: update_display('.') if '.' not in st.session_state.display else None)
    cols[2].button('=', on_click=calculate_result)
    cols[3].button('ADD', on_click=handle_operation, args=('add',))
    
    # Clear button
    st.button('Clear', on_click=clear_calculator)


