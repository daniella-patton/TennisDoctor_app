import streamlit as st
import numpy as np
import pandas as pd
import os, sys, pickle
from sklearn.externals import joblib

st.title('TennisDoctor')

if len(sys.argv) > 1: # parse command-line argument if supplied (folder path)
    folder = os.path.abspath(sys.argv[1])
else: # otherwise use the current working directory
    folder = os.path.abspath(os.getcwd())
 
st.write(folder)

# function to load model
@st.cache # cache
def load_csv(modelName):
	model = pd.read_csv(os.path.join(folder, modelName + '.csv'))
	return model
        
#@st.cache
#def get_data():
#    url = "https://github.com/daniella-patton/Test2/blob/master/App_data.csv"
#    return pd.read_csv(url, error_bad_lines=False)

modelName = 'App_data'
master = load_csv(modelName)
st.write(master)
#unique_names = master.PlayerName.unique()


