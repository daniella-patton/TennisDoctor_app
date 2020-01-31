import streamlit as st
import numpy as np
import pandas as pd
from sklearn.externals import joblib
import altair as alt
import datetime

"""
# TennisDoctor

An injury predictor for female professional tennis players.

This is a machine learning model that predicts the three month injury risk of female professional 
tennis players based off of match, injury, and ranking history. 

Select the player of interest from the drop down menu on the left. 

Risk options - Lower Risk/Higher Risk

"""
url = 'https://raw.githubusercontent.com/daniella-patton/Test2/master/Filter_Final_Logistic_Regression.csv'
df = pd.read_csv(url, index_col=0)
unique_names = df.PlayerName.unique()
option = st.sidebar.selectbox(
    'Select the tennis player you would like to predict injury risk from',
     unique_names)
'You selected:', 
name_df = pd.DataFrame([option], columns = ['Player Name']) 
st.dataframe(name_df)


name_filter = df[df['PlayerName'] == option]
#x = name_filter['StartDate']
#print(type(x))
#x = x.apply(lambda x: parser.parse(x).date())

'Based off of your selection, we predict that ',  option, ' is'
risk_r = 'Not at risk'
risk_df = pd.DataFrame([risk_r], columns = ['Risk']) 
st.dataframe(risk_df)

c = alt.Chart(name_filter, width=800,
    height=800).mark_bar().encode(
    x='StartDate',
    y='Month1MatchesPlayed',
    color='Injured',
    clamp=True).interactive()

c.encoding.x.title = 'Date of Play'
c.encoding.y.title = 'Number of Games Played'

st.write(c)



