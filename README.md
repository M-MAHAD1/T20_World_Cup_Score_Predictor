# 🏏 T20 World Cup Score Predictor

## 📌 Overview  
This project predicts the **final score** of a T20 cricket match using **machine learning**.  
Multiple regression models were tested and evaluated, with **XGBRegressor** achieving the best performance.  
The application features a **Streamlit web interface** for real-time score predictions, making it easy and interactive to use.  

**Example:**  
In the *Pakistan vs India* T20 World Cup 2022 match at Melbourne Cricket Ground, India scored **113 runs**. The model predicted **118 runs** — demonstrating **high accuracy** and practical real-world application.  

![Score Prediction Screenshot](https://github.com/M-MAHAD1/T20_World_Cup_Score_Predictor/blob/main/score%20prediction.PNG?raw=true)

---

## ✨ Features  
- Predicts final T20 match scores based on user input.  
- Supports multiple **international teams** and **global cricket venues**.  
- Real-time score prediction via **Streamlit web interface**.  
- Highly accurate with **low error rates**.  
- Includes all trained models and **test metrics** for analysis.  

---

## 🚀 How to Run the Project  

1. **Open** the project folder in **PyCharm** or any Python IDE.  
2. **Open** the file: `App.py`.  
3. Ensure the model file **`pipe.pkl`** is in the same directory.  
4. In the terminal, run:  
   ```bash
   streamlit run App.py
   ```
5. **Before running**, install the required libraries:  
   ```bash
   pip install xgboost streamlit pandas numpy scikit-learn
   ```

---

## 🧠 Main Model: XGBRegressor  
- **Train Accuracy:** 99.99%  
- **Test Accuracy:** 98.76%  
- **R² Score:** 98.76  
- **MAE:** 1.67  
- **MSE:** 12.86  
- **RMSE:** 3.58  
- **Overfitting:** No (Model performs well on unseen data)  

---

## 📊 Other Models Tested  

### 1️⃣ Decision Tree Regressor  
- Train Accuracy: 99.99%  
- Test Accuracy: 95.25%  
- R² Score: 95.25  
- MAE: 1.44  
- MSE: 49.41  
- RMSE: 7.03  

### 2️⃣ Linear Regression  
- Train Accuracy: 69.68%  
- Test Accuracy: 69.15%  
- R² Score: 69.15  
- MAE: 13.17  
- MSE: 321.32  
- RMSE: 17.92  

---

## 🎯 Input Features  
The model takes the following inputs:  
- **Batting team**  
- **Bowling team**  
- **City** where the match is played  
- **Current score**  
- **Overs completed**  
- **Wickets fallen**  
- **Runs scored in last 5 overs**  

---

## 📂 Model Files  
Included trained models:  
- **XGBRegressor**  
- **Decision Tree Regressor**  
- **Linear Regression**  

Each model is saved as a **`.pkl`** file for reuse or further testing.  

---

## 🌐 Web Interface  
The **Streamlit**-based interface allows users to input match details and receive instant predictions.  
- Simple and user-friendly design.  
- No technical knowledge required to operate.  

---

## 👨‍💻 Author  
**Muhammad Mahad**  
📧 Email: [muhammadmahad.cs@gmail.com](mailto:muhammadmahad.cs@gmail.com)  
