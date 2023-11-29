import streamlit as st
import numpy as np

# Title of the app
st.title("Streamlit App with Checkbox")

# Interactive elements
input_data = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
checkbox = st.checkbox('Enable feature')

# Function to generate data based on input and checkbox
def generate_data(input_range, enable_feature):
    if enable_feature:
        return np.sin(np.linspace(input_range[0], input_range[1], 100))
    else:
        return np.linspace(input_range[0], input_range[1], 100)

# Calculate data based on the input and checkbox
data = generate_data(input_data, checkbox)

# Display the graph
st.line_chart(data)

# Display other information
st.text(f'Checkbox value: {checkbox}')
