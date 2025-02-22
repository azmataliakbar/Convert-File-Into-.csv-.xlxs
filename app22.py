import streamlit as st
import pandas as pd
import os
from io import BytesIO
import plotly.express as px

# Configure the Streamlit page
st.set_page_config(
    page_title="🧹 Data Sweeper",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🧹"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
    .main { background-color:  #0E1117; color: white; }
    .stButton button { background-color: #262730; color: blue; border: 1px solid #4B4B4B; border-radius: 4px; }
    .stButton button:hover { background-color: #363940; border-color: #565656; }
    div[data-testid="stFileUploader"] section { color: #02f733 !important; border-radius: 10px !important; }
    .uploadedFile { background-color: #1E1E1E; padding: 1rem; border: 1px solid gray; border-radius: 10px; }
    .uploadedFile h3 { color: #0CAFFF !important; }
    .uploadedFile p { color: lightgreen !important; }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("🧹 Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")
st.markdown("**Convert `.csv` to `.xlsx` & `.xlsx` to `.csv`**", unsafe_allow_html=True)

# File uploader
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        try:
            # Read the file
            df = pd.read_csv(file) if file_ext == ".csv" else pd.read_excel(file)
            
            # Display file info
            st.markdown(f"""
                <div class="uploadedFile">
                    <h3>File Name: {file.name}</h3>
                    <p>File Size: {file.size/1024:.2f} KB</p>
                </div>
            """, unsafe_allow_html=True)

            # Show preview of data
            st.write("Preview the Head of the Dataframe")
            st.dataframe(df.head(), use_container_width=True)

            # Data Cleaning Options
            st.subheader("🛠️ Data Cleaning Options")
            if st.checkbox(f"Clean Data for {file.name}"):
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"Remove Duplicates from {file.name}"):
                        initial_rows = len(df)
                        df.drop_duplicates(inplace=True)
                        st.write(f"Duplicates Removed! ({initial_rows - len(df)} rows removed)")
                with col2:
                    if st.button(f"Fill Missing Values for {file.name}"):
                        numeric_cols = df.select_dtypes(include=['number']).columns
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                        st.write("Missing Values have been Filled!")

            # Column Selection
            st.subheader("🎯 Select Columns to Convert")
            columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
            if columns:
                df = df[columns]

            # Data Visualization
            st.subheader("📊 Data Visualization")
            if st.checkbox(f"Show Visualization for {file.name}"):
                numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
                
                if len(numeric_cols) >= 2:
                    fig = px.bar(df, x=df.index, y=numeric_cols[:4], barmode='group', title="Bar Chart Representation")
                    fig.update_layout(template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Not enough numeric columns for visualization. Please check your data.")

            # Conversion Options
            st.subheader("🔄 Conversion Options")
            conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"
                else:
                    df.to_excel(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                st.download_button("Download File", buffer.getvalue(), file_name, mime=mime_type)
        except Exception as e:
            st.error(f"Error processing {file.name}: {str(e)}")

            
