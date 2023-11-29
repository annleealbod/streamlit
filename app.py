import streamlit as st
import numpy as np

# Title of the app
st.title("Simple Streamlit App")

# Interactive elements
input_data = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
checkbox = st.checkbox('Enable feature')

# Function to generate data based on input
def generate_data(input_range):
    return np.linspace(input_range[0], input_range[1], 100)

# Calculate data based on the input
data = generate_data(input_data)

# Display the graph
st.line_chart(data)

# Display other information
st.text(f'Checkbox value: {checkbox}')
