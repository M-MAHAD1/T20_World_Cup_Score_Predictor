project:
  name: "T20 World Cup Score Predictor"

overview: |
  This project predicts the final score of a T20 cricket match using machine learning. 
  Multiple regression models were tested and evaluated. Among them, the XGBRegressor 
  model achieved the best results and is used as the final model for predictions. 
  The application provides a web interface built using the Streamlit library for ease 
  of use and real-time prediction capability.

example:
  description: |
    In the Pakistan vs India T20 World Cup 2022 match at Melbourne Cricket Ground, 
    India scored 113 runs. The model predicted a total of 118 runs — showcasing its 
    high accuracy and real-time application.
  image_url: "https://github.com/M-MAHAD1/T20_World_Cup_Score_Predictor/blob/main/score%20prediction.PNG?raw=true"

features:
  - Predicts final T20 cricket match scores based on user input
  - Supports multiple international teams and global cricket venues
  - Real-time score prediction via Streamlit web interface
  - Accurate predictions with low error rates
  - Includes all trained models and test metrics for analysis

how_to_run:
  steps:
    - Open the project folder in PyCharm or any Python IDE.
    - Open the file named `App.py`.
    - Ensure the model file `pipe.pkl` is available in the same directory.
    - Open the terminal in the IDE and run:
      command: "streamlit run App.py"
    - Before running, install required libraries:
      install_command: "pip install xgboost streamlit pandas numpy scikit-learn"

models:
  main_model:
    name: "XGBRegressor"
    metrics:
      train_accuracy: "99.99%"
      test_accuracy: "98.76%"
      r2_score: "98.76"
      mae: 1.67
      mse: 12.86
      rmse: 3.58
      overfitting: "No (Model performs well on unseen data)"
  other_models:
    - name: "Decision Tree Regressor"
      metrics:
        train_accuracy: "99.99%"
        test_accuracy: "95.25%"
        r2_score: "95.25"
        mae: 1.44
        mse: 49.41
        rmse: 7.03
    - name: "Linear Regression"
      metrics:
        train_accuracy: "69.68%"
        test_accuracy: "69.15%"
        r2_score: "69.15"
        mae: 13.17
        mse: 321.32
        rmse: 17.92

input_features:
  - Batting team
  - Bowling team
  - City where the match is being played
  - Current score
  - Overs completed
  - Wickets fallen
  - Runs scored in last 5 overs

model_files:
  - XGBRegressor
  - Decision Tree Regressor
  - Linear Regression
  note: "Each model is saved as a .pkl file and can be reused or tested further."

web_interface: |
  The application is built with Streamlit to allow users to input match conditions 
  and get instant predictions. The interface is simple and user-friendly, requiring 
  no technical background to operate.

author:
  name: "Muhammad Mahad"
  email: "muhammadmahad.cs@gmail.com"
