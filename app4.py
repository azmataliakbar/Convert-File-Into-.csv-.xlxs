import streamlit as st
import webbrowser

# ✅ Move this to the top before anything else
st.set_page_config(page_title="Beautiful Calculator", page_icon="🧮", layout="centered")

def main():
    st.sidebar.title("A Simple Calculator")

    # Buttons with hidden links
    if st.sidebar.button("📜 Chat GPT"):
        webbrowser.open_new_tab("https://chatgpt.com/")

    if st.sidebar.button("💻 My Project 1"):
        webbrowser.open_new_tab("https://heaven-hills-furniture.netlify.app/")

    if st.sidebar.button("🚀 Deep Seek"):
        webbrowser.open_new_tab("https://chat.deepseek.com/")

    if st.sidebar.button("🔗 Google"):
        webbrowser.open_new_tab("https://www.google.co.uk/")

    # Main container for the calculator UI
    with st.container():
        st.title(" Learn Python 🐍")
        st.title("📟 Streamlit Calculator")
        
        num1 = st.text_input("Enter first number", key="num1")
        num2 = st.text_input("Enter second number", key="num2")

        if num1 and num2:
            try:
                num1, num2 = float(num1), float(num2)
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    if st.button("➕"):
                        st.success(f"Result: {num1 + num2}")
                
                with col2:
                    if st.button("➖"):
                        st.success(f"Result: {num1 - num2}")
                
                with col3:
                    if st.button("✖"):
                        st.success(f"Result: {num1 * num2}")
                
                with col4:
                    if st.button("➗"):
                        if num2 != 0:
                            st.success(f"Result: {num1 / num2}")
                        else:
                            st.error("Cannot divide by zero")
            except ValueError:
                st.error("Please enter valid numeric values.")

if __name__ == "__main__":
    main()

