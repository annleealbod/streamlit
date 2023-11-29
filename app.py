#!/usr/bin/env python
# coding: utf-8


# In[2]:


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


# Interactive elements
input_data = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
checkbox = st.checkbox('Enable feature')


# In[ ]:


# Graph that updates based on input
data = np.random.randn(100, 1) * input_data[0] + input_data[1]
# Create the histogram using plt.hist()
plt.hist(data, bins=20)

# Display the plot using st.pyplot()
st.pyplot()

# In[ ]:


# Display other information
st.text(f'Checkbox value: {checkbox}')

