import streamlit as st
import numpy as np
import pandas as pd
from sklearn.externals import joblib

st.title('TennisDoctor')

@st.cache
def get_data():
    url = "https://github.com/daniella-patton/Test2/blob/master/App_data.csv"
    return pd.read_csv(url)

master = get_data()
unique_names = master.PlayerName.unique()
# Load in the model 
# load the model from disk
#filename = 'logistic_reg_model.sav'
#loaded_model = joblib.load(filename)


option = st.sidebar.selectbox(
    'Select the tennis player you would like to predict injury risk from',
     unique_names)

'You selected:', option

'Starting computation...'

