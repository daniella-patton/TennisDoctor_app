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


