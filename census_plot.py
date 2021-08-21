# Code for 'census_plots.py' file.
# Import necessary modules.
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):
  st.subheader('Visualise Data')
  st.set_option('deprecation.showPyplotGlobalUse', False)

    # Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
    # Store the current value of this widget in a variable 'plot_list'.
  st.subheader('Visualization Selector')
  plot_list=st.multiselect('Choose your plot',('count plot','pie chart','box plot'))
    # Display count plot using seaborn module and 'st.pyplot()' 
  if 'count plot' in plot_list:
    st.subheader('Count plot')
    plt.figure(figsize=(20,5))
    plt.title('Count plot for distribution of records for unique workclass groups')
    sns.countplot(x='workclass',data=census_df)
    st.pyplot()


    # Display pie plot using matplotlib module and 'st.pyplot()'
  if 'pie chart' in plot_list:
    st.subheader('Pie Chart')
    plt.figure(figsize=(20,5))
    pie_data = st.selectbox('Select income or gender',('income','gender'))
    plt.title(f'Distribution of records for {pie_data}')
    plt.figure(figsize=(20,5))
    plt.pie(census_df[pie_data].value_counts(), labels = census_df[pie_data].value_counts().index, autopct='%1.2f%%', startangle=30)
    st.pyplot()


    # Display box plot using matplotlib module and 'st.pyplot()'
  if 'box plot' in plot_list:
    st.subheader('Box Plot')
    plt.figure(figsize=(20,5))
    column = st.selectbox('Select the column for boxplot', ('income', 'gender'))
    plt.title(f'The distribution of records for {column} with hours-per-week')
    sns.boxplot(x='hours-per-week', y=census_df[column], data = census_df)
    st.pyplot()
      
