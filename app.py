import streamlit as st
import numpy as np
import pandas as pd
from sklearn.externals import joblib
import matplotlib.pyplot as plt
import datetime

"""
# TennisDoctor

This is a machine learning model that predicts the three month injury risk of female professional 
tennis players.

This model is based off of privious match, injury, and ranking history. 

Select the player of interest from the drop down menu on the left. 

Risk options - Lower Risk/Higher Risk
"""
url = 'https://raw.githubusercontent.com/daniella-patton/Test2/master/Filter_Final_Logistic_Regression.csv'
df = pd.read_csv(url, index_col=0)
unique_names = df.PlayerName.unique()
option = st.sidebar.selectbox(
    'Select the tennis player you would like to predict injury risk from',
     unique_names)
'You selected:', option

name_df = pd.DataFrame([option], columns = ['Player Name']) 
st.dataframe(name_df)

arr = np.random.normal(1, 1, size=100)
plt.hist(arr, bins=20)
st.pyplot()


