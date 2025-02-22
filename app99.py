import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and layout
st.set_page_config(page_title="CSV Data Viewer", layout="wide")

# App Title
st.title("📊 Full CSV Data Graph Viewer")

# File Upload
file = st.file_uploader("📂 Upload a CSV file", type=["csv"])

# If a file is uploaded, process it
if file is not None:
    try:
        # Read CSV file into a DataFrame
        df = pd.read_csv(file)
        st.success("✅ File uploaded successfully!")

        # Define Rows & Columns in a Single Line
        rows, cols = 30, 12  # Change these values to control displayed rows & columns

        # Display Data Preview
        st.subheader("📄 Data Preview")
        st.write(df.iloc[:rows, :cols])  # Apply row & column limit in one line

        # Show Column Details
        st.subheader("🔍 Column Details")
        st.write(df.dtypes)

        # Data Visualization
        st.subheader("📊 Full Data Visualization")

        # Check for numeric columns
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

        if numeric_cols:
            # Convert DataFrame to long format for better visualization
            df_long = df.iloc[:rows, :].melt(id_vars=df.columns[0], value_vars=numeric_cols, 
                                            var_name="Column", value_name="Value")

            # Create a Bar Chart
            fig = px.bar(df_long, x=df_long.columns[0], y="Value", color="Column",
                        title="📊 Bar Chart for Selected Data",
                        labels={"Value": "Values", df_long.columns[0]: "Index"},
                        barmode="group", template="plotly_dark")

            # Display the graph
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("⚠️ No numeric columns found for visualization.")

    except Exception as e:
        st.error(f"❌ Error reading the file: {e}")

else:
    st.info("📂 Please upload a CSV file to get started.")
