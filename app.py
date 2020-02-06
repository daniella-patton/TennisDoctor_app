import streamlit as st
import numpy as np
import pandas as pd
from sklearn.externals import joblib
import altair as alt
import datetime
import os, sys, pickle
from PIL import Image


st.title('TennisDoctor')
st.header('An injury predictor for female professional tennis players.')

"""
Select the player of interest from the drop down menu on the left. 

This is a machine learning model that predicts the three month injury risk of female professional 
tennis players based off of match, injury, and ranking history. 

Risk options - Lower Risk/Higher Risk
"""

url = 'https://raw.githubusercontent.com/daniella-patton/Test2/master/Filter_Final_Logistic_Regression.csv'
df = pd.read_csv(url, index_col=0)
unique_names = df.PlayerName.unique()
option = st.sidebar.selectbox('Select the tennis player you would like to predict injury risk from',
     unique_names)
		
'You selected:', 
st.markdown('You selected **option**.')

#name_df = pd.DataFrame([option], columns = ['Player Name']) 
#st.dataframe(name_df)


name_filter = df[df['PlayerName'] == option]
#x = name_filter['StartDate']
#print(type(x))
#x = x.apply(lambda x: parser.parse(x).date())

'Based off of your selection, we predict that ',  option, ' is'

# Running the machine learning model on the data

# load the model from disk
if len(sys.argv) > 1: # parse command-line argument if supplied (folder path)
    folder = os.path.abspath(sys.argv[1])
else: # otherwise use the current working directory
    folder = os.path.abspath(os.getcwd())

# function to load model
def load_model(modelName):
	model = pd.read_pickle(os.path.join(folder, modelName + '.sav'))
	return model

# load model
modelName = 'random_forest_model'
model = load_model(modelName)

#result = loaded_model.score(X_test, Y_test)
#print(result)

risk_r = 'Not at risk'
risk_df = pd.DataFrame([risk_r], columns = ['Risk']) 
st.dataframe(risk_df)

# LOADING IN PICTURE
def load_pic(option):
	try:
		file = os.path.join(folder, 'WTA_Pictures', option + '.jpg')
		image = Image.open(file)
	except IOError:
		file = os.path.join(folder, 'WTA_Pictures', 'base.jpg') # base.jpg
		image = Image.open(file)
	return image

player_pic = load_pic(option)
  
#else:
#    image = Image.open('base.jpg')
st.image(player_pic, caption = option, width=None)

c = alt.Chart(name_filter, width=800,
    height=600, title="Matches Played and Injury History").mark_bar().encode(
    x='StartDate',
    y='Month1MatchesPlayed',
    color='Injured').configure_axis(
    labelFontSize= 15,
    titleFontSize= 15).configure_title(fontSize=24).interactive()


c.encoding.x.title = 'Date of Play'
c.encoding.y.title = 'Number of Matches Played'

st.write(c)



