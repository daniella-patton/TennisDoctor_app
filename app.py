import streamlit as st
import numpy as np
import pandas as pd
from sklearn.externals import joblib

st.title('TennisDoctor')

master = pd.read_csv('App_data.csv')
#print(master.head())
unique_names = master.PlayerName.unique()
# Load in the model 
# load the model from disk
filename = 'logistic_reg_model.sav'
loaded_model = joblib.load(filename)


