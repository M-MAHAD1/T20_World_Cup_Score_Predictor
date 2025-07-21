T20 World Cup Score Predictor

Overview

This project predicts the final score of a T20 cricket match using machine learning. Multiple regression models were tested and evaluated. Among them, the XGBRegressor model achieved the best results and is used as the final model for predictions. The application provides a web interface built using the Streamlit library for ease of use and real-time prediction capability.

Example:

In the Pakistan vs India T20 World Cup 2022 match at Melbourne Cricket Ground, India scored 113 runs. The model predicted a total of 118 runs — showcasing its high accuracy and real-time application.
[!image alt](imagelinkaddress)

Project Features

Predicts final T20 cricket match scores based on user input

Supports multiple international teams and global cricket venues

Real-time score prediction via Streamlit web interface

Accurate predictions with low error rates

Includes all trained models and test metrics for analysis

How to Run the Project

Open the project folder in PyCharm or any Python IDE.

Open the file named App.py.

Make sure the model file pipe.pkl is available in the same directory.

Open the terminal in the IDE and type the following command:

streamlit run App.py

Note: Before running, ensure required libraries are installed by running:

pip install xgboost streamlit pandas numpy scikit-learn

Main Model: XGBRegressor

Train Accuracy: 99.99%
Test Accuracy: 98.76%
R² Score: 98.76
MAE (Mean Absolute Error): 1.67
MSE (Mean Squared Error): 12.86
RMSE (Root Mean Squared Error): 3.58
Overfitting: No (Model performs well on unseen data)

Other Models Tested

Decision Tree Regressor
Train Accuracy: 99.99%
Test Accuracy: 95.25%
R² Score: 95.25
MAE: 1.44
MSE: 49.41
RMSE: 7.03

Linear Regression
Train Accuracy: 69.68%
Test Accuracy: 69.15%
R² Score: 69.15
MAE: 13.17
MSE: 321.32
RMSE: 17.92

Input Features

The model takes the following inputs:

Batting team

Bowling team

City where the match is being played

Current score

Overs completed

Wickets fallen

Runs scored in last 5 overs

Model Files

The project folder includes trained model files for:

XGBRegressor

Decision Tree Regressor

Linear Regression

Each model is saved as a .pkl file and can be reused or tested further.

Web Interface

The application is built with Streamlit to allow users to input match conditions and get instant predictions. The interface is simple and user-friendly, requiring no technical background to operate.

Author

Muhammad Mahad
muhammadmahad.cs@gmail.com
