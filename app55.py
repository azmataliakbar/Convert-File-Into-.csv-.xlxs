import streamlit as st
import pandas as pd
import os
from io import BytesIO
import plotly.express as px
import plotly.graph_objects as go

# Configure the Streamlit page
st.set_page_config(
    page_title="🧹 Data sweeper",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🧹"
)

# Custom CSS to match the dark theme
st.markdown("""
    <style>
    .main {
        background-color:  #0E1117;
        color: white;
    }
    .stButton button {
        background-color: #262730;
        color: blue;
        border: 1px solid #4B4B4B;
        border-radius: 4px;
        padding: 0.5rem 1rem;
    }
    .stButton button:hover {
        background-color: #363940;
        border-color: #565656;
    }
    div[data-testid="stFileUploader"] section {
        color: #02f733 !important;
        border-radius: 10px !important;
        font-size: 2.0rem !important;
        font-weight: bold !important;
    }
    .uploadedFile {
        background-color: #1E1E1E;
        padding: 1rem;
        border: 1px solid gray;
        border-radius: 10px;
        margin-bottom: 1rem;
        font-size: 2.0rem;
        font-weight: bold;
    }
    .uploadedFile h3 {
        color: #0CAFFF !important;
    }
    .uploadedFile p {
        color: lightgreen !important;
    }
    .stDataFrame {
        background-color: #262730;
    }
    .stCheckbox label {
        color: white;
    }
    .stRadio label {
        color: white;
    }
    div[data-testid="stFileUploader"] {
        background-color: #262730;
        color: white;
        font-size: 2.0rem;
        font-weight: bold;
        border: 1px dashed #4B4B4B;
        padding: 1rem;
        border-radius: 10px;
    }
    div[data-testid="stMarkdownContainer"] {
        color: orange;
        font-size: 1.2rem;
        font-weight: bold;
    }
    button {
        font-size: 2.0rem !important;
        font-weight: bold;
        padding: 12px 24px !important;
    }
    </style>
""", unsafe_allow_html=True)

# App title and description
st.title("🧹 Data sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")
st.markdown("**Convert `.csv` to `.xlsx` && `.xlsx` to `.csv`**", unsafe_allow_html=True)

# File uploader
uploaded_files = st.file_uploader(
    "Upload your files ( CSV or Excel ):",
    type=["csv", "xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        try:
            # Read the file
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue

            # Display file information
            st.markdown(f"""
                <div class="uploadedFile">
                    <h3 style="color: #FFA500;">File Name: {file.name}</h3>
                    <p style="color: #00FF00;">File Size: {file.size/1024:.2f} KB</p>
                </div>
            """, unsafe_allow_html=True)

            # Preview the dataframe
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
                        rows_removed = initial_rows - len(df)
                        st.write(f"Duplicates Removed! ({rows_removed} rows removed)")

                with col2:
                    if st.button(f"Fill Missing Values for {file.name}"):
                        numeric_cols = df.select_dtypes(include=['number']).columns
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                        st.write("Missing Values have been Filled!")

            # Column Selection
            st.subheader("🎯 Select Columns to Convert")
            columns = st.multiselect(
                f"Choose Columns for {file.name}",
                df.columns,
                default=df.columns
            )
            if columns:
                df = df[columns]

            # Data Visualization
            st.subheader("📊 Data Visualization")
            if st.checkbox(f"Show Visualization for {file.name}"):
                try:
                    # Display column information
                    st.write("Column Information:")
                    for col in df.columns:
                        st.write(f"{col}: {df[col].dtype}")
                    
                    # Convert 'Date' column to datetime if it exists
                    if 'Date' in df.columns:
                        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
                    
                    # Identify numeric columns
                    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
                    st.write(f"Numeric columns: {list(numeric_cols)}")
                    
                    # Check if necessary columns for candlestick chart exist
                    if all(col in df.columns for col in ['Date', 'Open', 'High', 'Low', 'Close']):
                        # Ensure these columns are numeric
                        for col in ['Open', 'High', 'Low', 'Close']:
                            df[col] = pd.to_numeric(df[col], errors='coerce')
                        
                        # Create an interactive candlestick chart using Plotly
                        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'])])
                        
                        fig.update_layout(
                            title='Price Chart',
                            yaxis_title='Price',
                            xaxis_title='Date',
                            template="plotly_dark",
                            plot_bgcolor='rgba(0,0,0,0)',
                            paper_bgcolor='rgba(0,0,0,0)',
                            margin=dict(t=30, l=10, r=10, b=10)
                        )
                        
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Add volume chart if 'Volume' column exists
                        if 'Volume' in df.columns:
                            df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')
                            volume_fig = px.bar(df, x='Date', y='Volume', title='Trading Volume')
                            volume_fig.update_layout(
                                template="plotly_dark",
                                plot_bgcolor='rgba(0,0,0,0)',
                                paper_bgcolor='rgba(0,0,0,0)',
                                margin=dict(t=30, l=10, r=10, b=10)
                            )
                            st.plotly_chart(volume_fig, use_container_width=True)
                    else:
                        # Fallback to line chart for numeric columns
                        if len(numeric_cols) >= 2:
                            fig = go.Figure()
                            for col in numeric_cols[:4]:  # Use first two numeric columns
                                fig.add_trace(go.Scatter(
                                    y=df[col],
                                    name=col,
                                    line=dict(width=1)
                                ))
                            
                            fig.update_layout(
                                title='Data Visualization',
                                yaxis_title='Value',
                                xaxis_title='Index',
                                template="plotly_dark",
                                plot_bgcolor='rgba(0,0,0,0)',
                                paper_bgcolor='rgba(0,0,0,0)',
                                margin=dict(t=30, l=10, r=10, b=10)
                            )
                            st.plotly_chart(fig, use_container_width=True)
                            
                        else:
                            st.warning("Not enough numeric columns for visualization. Please check your data types.")

                            
                except Exception as e:
                    st.error(f"Error in visualization: {str(e)}")

            # Conversion Options
            st.subheader("🔄 Conversion Options")
            conversion_type = st.radio(
                f"Convert {file.name} to:",
                ["CSV", "Excel"],
                key=file.name
            )

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
                
                buffer.seek(0)
                
                # Download button
                st.download_button(
                    label=f"📥 Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type
                )

        except Exception as e:
            st.error(f"Error processing {file.name}: {str(e)}")
            continue

    st.success("✨ All files processed!")