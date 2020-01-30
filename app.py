import streamlit as st
import numpy as np
import pandas as pd
from sklearn.externals import joblib

st.title('TennisDoctor')

url = 'https://raw.githubusercontent.com/daniella-patton/Test2/master/Filter_Final_Logistic_Regression.csv'
df = pd.read_csv(url, index_col=0)

st.write(df)
unique_names = df.PlayerName.unique()

"""
# Predicting Risk of Injury in Female Professional Tennis Players

This is a machine learning model that predicts the risk of player injury in the following three months.

Risk options - Lower Risk/Higher Risk
"""

option = st.sidebar.selectbox(
    'Select the tennis player you would like to predict injury risk from',
     unique_names)

'You selected:', option

'Starting computation...'
