# Show complete dataset and summary in 'census_home.py'
# Import necessary modules.

# Define a function 'app()' which accepts 'census_df' as an input.
import streamlit as st
import numpy as np
import pandas as pd
 
def app(census_df):
  st.header('Census Visualisation Web App')
  st.text('This web app allows the user to explore and visualise the census data')
  # Display dataset within beta_expander.
  if st.checkbox('View data set'):
    with st.beta_expander('view data set'):
      st.table(census_df.head())
    # Show dataset summary on click of a checkbox.
    if st.checkbox('show summary'):
      with st.beta_expander('show summary'):
        st.table(census_df.describe())
      
    