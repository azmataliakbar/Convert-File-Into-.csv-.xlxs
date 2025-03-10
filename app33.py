import streamlit as st
import pandas as pd
import plotly.graph_objects as go  # Correct import for graph_objects
print("Plotly imported successfully!")
import plotly.express as px        # Import plotly.express for convenience
import os
from io import BytesIO



# Set up our App
st.set_page_config(page_title="🧹 Data sweeper", layout='wide')

# Custom CSS to match the dark theme
# Update the CSS section only - rest of the code remains the same
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
    
    /* Main container */
    .main {
        background-color: #0E1117 !important;
        color: white !important;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #262730 !important;
    }
    
    /* File uploader */
    div[data-testid="stFileUploader"] {
        background-color: #262730 !important;
        color: white !important;
        font-size: 2.0rem !important;
        font-weight: bold !important;
        border: 1px dashed #4B4B4B !important;
        padding: 1rem !important;
        border-radius: 10px !important;
    }
    
    div[data-testid="stFileUploader"] section {
        color: #02f733 !important;
        background-color: #262730 !important;
        border-radius: 10px !important;
        font-size: 2.0rem !important;
        font-weight: bold !important;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #262730 !important;
        color: blue !important;
        border: 1px solid #4B4B4B !important;
        border-radius: 4px !important;
        padding: 0.5rem 1rem !important;
    }
    
    .stButton button:hover {
        background-color: #363940 !important;
        border-color: #565656 !important;
    }
    
    button {
        font-size: 2.0rem !important;
        font-weight: bold !important;
        padding: 12px 24px !important;
    }
    
    /* File info box */
    .uploadedFile {
        background-color: #1E1E1E !important;
        padding: 1rem !important;
        border: 1px solid gray !important;
        border-radius: 10px !important;
        margin-bottom: 1rem !important;
        font-size: 2.0rem !important;
        font-weight: bold !important;
    }
    
    .uploadedFile h3 {
        color: #0CAFFF !important;
    }
    
    .uploadedFile p {
        color: lightgreen !important;
    }
    
    /* DataFrame */
    .stDataFrame {
        background-color: #262730 !important;
    }
    
    /* Form elements */
    .stCheckbox label {
        color: white !important;
    }
    
    .stRadio label {
        color: white !important;
    }
    
    /* Markdown text */
    div[data-testid="stMarkdownContainer"] {
        color: orange !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
    }
    
    /* Mobile specific styles */
    @media (max-width: 768px) {
        .main {
            background-color: #0E1117 !important;
        }
        
        .stApp {
            background-color: #0E1117 !important;
        }
        
        div[data-testid="stFileUploader"] {
            font-size: 1.5rem !important;
        }
        
        .uploadedFile {
            font-size: 1.5rem !important;
        }
        
        button {
            font-size: 1.5rem !important;
            padding: 8px 16px !important;
            
        }
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌱 Growth Mindset Challenge")
st.title("🧹 Data sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")
st.markdown("**Convert `.csv` to `.xlsx` && `.xlsx` to `.csv`**", unsafe_allow_html=True)

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"],
                            accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue
        except Exception as e:
            st.error(f"Error reading file {file.name}: {str(e)}")
            continue
        
        # Display info about the file
        st.markdown(f"""
            <div class="uploadedFile">
                <h3>File Name: {file.name}</h3>
                <p>File Size: {file.size/1024:.2f} KB</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Show 5 rows of our df
        st.write("Preview the Head of the Dataframe")
        st.dataframe(df.head())
        
        # Options for data cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed!")
            
            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values have been Filled!")
        
        # Choose Specific Columns to Keep or Convert
        st.subheader("Select Columns to Convert")
        columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
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
                
                # Line and Bar charts for numeric columns
                if len(numeric_cols) >= 2:
                    # Line chart
                    line_fig = px.line(df, y=numeric_cols[:4], title='Line Chart of Numeric Columns')
                    line_fig.update_layout(
                        template="plotly_dark",
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        margin=dict(t=30, l=10, r=10, b=10)
                    )
                    st.plotly_chart(line_fig, use_container_width=True)
                    
                    # Bar chart
                    bar_fig = px.bar(df, y=numeric_cols[:4], title='Bar Chart of Numeric Columns')
                    bar_fig.update_layout(
                        template="plotly_dark",
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        margin=dict(t=30, l=10, r=10, b=10)
                    )
                    st.plotly_chart(bar_fig, use_container_width=True)
                else:
                    st.warning("Not enough numeric columns for visualization. Please check your data types.")
                        
            except Exception as e:
                st.error(f"Error in visualization: {str(e)}")
        
        # Convert the File -> CSV to Excel
        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext,".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            
            buffer.seek(0)
            
            # Download Button
            st.download_button(
                label=f"📥 Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )
    
    st.success("✨ All files processed!")
    st.write("*Built with ❤️ using Streamlit.*")
    st.write("*✍️Prepared By: Azmat Ali*")



