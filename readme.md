# Introduction
This repository contains various files related to a web application, TennisDoctor (http://tennisdoctor.herokuapp.com/), an injury predictor for female professional tennis players. 
This web application  has several components, which allows for tennis coaches and staff to assess their players' individual risk of injury in Python (female professional in the top 200 from 2010 - 2020).
This web application was created using streamlit and was deployed using Heroku. 

Last Edit: 2/12/20

Author: Daniella Patton

# Files
Current_Player_Info.csv
A csv file that has current female professional tennis player information used to preduct a player's future risk of injury.

ML_filtered_career.csv
This has the game and injury history of every female professional player from which one can select from. This information is used to create the player specific games played and injury history. 

Procfile
A required file for streamlit

app.py
The web application file.

logistic_model.sav
The logistic regression model used to predict future injury risk of tennis players. 

requirements.txt
The requirements file for Heroku

# License
MIT @daniella-patton

