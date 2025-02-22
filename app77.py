import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Data Analyzer", layout="wide")

# Title
st.title("📊 Data Analyzer and Visualizer")

# Upload multiple CSV files
uploaded_files = st.file_uploader("Upload CSV files", type=["csv"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        st.subheader(f"📄 File: {file.name}")
        df = pd.read_csv(file)

        # Display dataframe
        if st.checkbox(f"Show Data for {file.name}"):
            st.dataframe(df)

        # Handle non-numeric columns
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            if df[col].nunique() < 10:  # Encode if few unique values
                df[col] = df[col].astype('category').cat.codes
            else:
                st.warning(f"Skipping non-numeric column: {col}")

        # Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            numeric_cols = df.select_dtypes(include=['number']).columns
            
            if len(numeric_cols) == 0:
                st.warning("No numeric columns found! Please ensure your data has numerical values.")
            elif len(numeric_cols) == 1:
                fig = px.histogram(df, x=numeric_cols[0], title=f"Distribution of {numeric_cols[0]}")
                st.plotly_chart(fig, use_container_width=True)
            else:
                fig = go.Figure()
                for col in numeric_cols[:12]:
                    fig.add_trace(go.Scatter(y=df[col], name=col, line=dict(width=1)))
                fig.update_layout(template="plotly_dark", title="Line Chart of Numeric Data")
                st.plotly_chart(fig, use_container_width=True)

st.write("Upload CSV files to explore your data!")
