import streamlit as st
import numpy as np
import pandas as pd
from sklearn.externals import joblib
import altair as alt
import datetime
import os, sys, pickle
from PIL import Image


st.markdown('''
<style>
body {
    background-color:#e6f9ff;
}
<style>
    ''', unsafe_allow_html=True)

# load the model from disk
if len(sys.argv) > 1: # parse command-line argument if supplied (folder path)
    folder = os.path.abspath(sys.argv[1])
else: # otherwise use the current working directory
    folder = os.path.abspath(os.getcwd())

# function to load model
def load_model(modelName):
    model = pd.read_pickle(os.path.join(folder, modelName + '.sav'))
    return model

# function to load in csv
def load_csv(csv_name):
    player_csv = pd.read_csv(os.path.join(folder, csv_name + '.csv'), index_col=0)
    return player_csv

# function to load image
def load_pic(option):
    try:
        file = os.path.join(folder, 'WTA_Pictures', option + '.jpg')
        image = Image.open(file)
    except IOError:
        file = os.path.join(folder, 'WTA_Pictures', 'base.jpg') # base.jpg
        image = Image.open(file)
    return image

# Load in csv
csv_name = 'Current_Player_Info'
df = load_csv(csv_name)
unique_names = df.PlayerName.unique()


# Load in Model
modelName = 'logistic_model'
model = load_model(modelName)


# Main page layout

st.title('TennisDoctor')
st.header('An injury predictor for female professional tennis players.')


"""

Select the player of interest from the drop-down menu on the left. 

This is a machine learning model that predicts the three month injury risk of female professional 
tennis players based off of match, injury, and ranking history. 

Risk options - Lower Risk/Higher Risk
"""

option = st.sidebar.selectbox('Select the tennis player',
     unique_names)
		
st.markdown('You selected **' + str(option) + '**')


name_filter = df[df['PlayerName'] == option]
name_filter = name_filter.drop(['PlayerName'], axis=1)



'We predict that ',  option, ' is:'

# Running the logistic regression model on the data
result = model.predict_proba(name_filter)

results_p = result[:,1]

if results_p >= 0.75:
    risk_as = 'At higher risk injury'

if results_p < 0.75 and results_p >= 0.5:
    risk_as = 'At moderate risk of injury'

if results_p < 0.5:
    risk_as = 'At low risk of injury'

st.markdown('**' + risk_as + '**')


csv_name = 'ML_filtered_career'
df2 = load_csv(csv_name)
name_filter2 = df2[df2['PlayerName'] == option]
name_filter2 = name_filter2.drop(['PlayerName'], axis=1)

c = alt.Chart(name_filter2).mark_bar().encode(
    x='Age',
    y='Doubles_Ranking'
)

#c = alt.Chart(name_filter, width=800,
#    height=600, title="Matches Played and Injury History").mark_bar().encode(
#    x='StartDate',
#    y='Month1MatchesPlayed',
#    color='Injured').configure_axis(
#    labelFontSize= 15,
#    titleFontSize= 15).configure_title(fontSize=24).interactive()
#c.encoding.x.title = 'Date of Play'
#c.encoding.y.title = 'Number of Matches Played'

source = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

c = alt.Chart(source).mark_bar().encode(
    x='a',
    y='b'
)


st.write(c)



