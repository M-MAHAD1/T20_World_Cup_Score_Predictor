import streamlit as st
import pickle
import pandas as pd
import numpy as np

with open('pipe.pkl', 'rb') as file:
    pipe = pickle.load(file)

teams = ['Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa',
         'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka']

cities = ['Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland',
          'Cape Town', 'London', 'Pallekele', 'Barbados', 'Sydney',
          'Melbourne', 'Durban', 'St Lucia', 'Wellington', 'Lauderhill',
          'Hamilton', 'Centurion', 'Manchester', 'Abu Dhabi', 'Mumbai',
          'Nottingham', 'Southampton', 'Mount Maunganui', 'Chittagong',
          'Kolkata', 'Lahore', 'Delhi', 'Nagpur', 'Chandigarh', 'Adelaide',
          'Bangalore', 'St Kitts', 'Cardiff', 'Christchurch', 'Trinidad']

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select City', sorted(cities))

col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input('Current Score', min_value=0, step=1)
with col4:
    overs = st.number_input('Overs done (works for over > 5)', min_value=0.0, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input('Wickets out', min_value=0, max_value=10, step=1)

last_five = st.number_input('Runs scored in last 5 overs', min_value=0, step=1)

if st.button('Predict Score'):
    if batting_team == bowling_team:
        st.error("Batting and Bowling teams cannot be the same.")
    elif overs <= 0:
        st.error("Overs must be greater than 0.")
    else:
        balls_left = 120 - int(overs * 6)
        wickets_left = 10 - int(wickets)
        crr = current_score / overs if overs > 0 else 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'current_score': [int(current_score)],
            'balls_left': [balls_left],
            'wickets_left': [wickets_left],
            'crr': [crr],
            'last_five': [int(last_five)]
        })

        result = pipe.predict(input_df)
        st.header('Predicted Score - ' + str(int(result[0])))
