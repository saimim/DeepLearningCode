import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set up the main app title
st.set_page_config(page_title="EWMA Calculator")
st.markdown("<h1 style='text-align: center;'>Exponentially Weighted Moving Average (EWMA) Calculator</h1>", unsafe_allow_html=True)

# Description
st.markdown("""
    <p style='text-align: center;'>
        Upload a CSV file containing your data, specify the target column, and set an alpha value to compute the EWMA.
    </p>
    <hr>
""", unsafe_allow_html=True)

# File upload section
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# If a file is uploaded
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the data
    st.markdown("<h4>Data Preview:</h4>", unsafe_allow_html=True)
    st.write(df.head())

    # Check if the 'date' column is present
    if 'date' in df.columns:
        # Convert 'date' column to datetime for plotting
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

        # Input box for target column
        target_column = st.text_input("Enter the target column name (e.g., 'meantemp'):")

        # Ensure the target column exists in the DataFrame
        if target_column and target_column in df.columns:
            # Set alpha value through a slider
            alpha = st.slider("Select alpha value (0 < alpha < 1)", 0.01, 1.0, 0.9, step=0.01)

            # Calculate EWMA
            df['ewm'] = df[target_column].ewm(alpha=alpha).mean()
            
            # Plotting
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(df['date'], df[target_column], color='red', label=target_column)
            ax.plot(df['date'], df['ewm'], color='black', label=f'EWMA (alpha={alpha})')

            # Add labels and title
            ax.set_xlabel('Date')
            ax.set_ylabel(target_column.capitalize())
            ax.set_title('Exponentially Weighted Moving Average (EWMA)')
            ax.legend()
            
            # Display plot
            st.pyplot(fig)
        else:
            st.error("Please enter a valid target column name that exists in the uploaded file.")
    else:
        st.error("The uploaded file must contain a 'date' column.")
else:
    st.info("Please upload a CSV file to begin.")
