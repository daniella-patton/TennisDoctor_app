import streamlit as st
import numpy as np
import pandas as pd
from sklearn.externals import joblib

st.title('TennisDoctor')

url = 'https://github.com/daniella-patton/Test2/blob/master/App_data.csv'
df = pd.read_csv(url, index_col=0)
print(df.head(5))

# function to load model
#@st.cache # cache
#def load_csv(modelName):
#	model = pd.read_csv(os.path.join(folder, modelName + '.csv'))
#	return model
        
#@st.cache
#def get_data():
#    url = "https://github.com/daniella-patton/Test2/blob/master/App_data.csv"
#    return pd.read_csv(url, error_bad_lines=False)

#modelName = 'App_data'
#master = load_csv(modelName)
st.write(df)
unique_names = master.PlayerName.unique()


