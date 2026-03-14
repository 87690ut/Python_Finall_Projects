# 🚀 ML Journey - Day 1: Sales Prediction Model

## 📌 Project Overview
This project marks the beginning of my Machine Learning journey. I built a Multiple Linear Regression model to predict the daily sales of a business based on various real-world factors such as the Day, Discount Percentage, and Holidays.

## 🧠 Concepts Learned & Applied
* **Multiple Linear Regression:** Transitioned from simple 1D predictions to handling multiple independent variables (Features).
* **Train-Test Split:** Implemented an 80-20 split using `scikit-learn` to train the model and evaluate it on unseen data, ensuring real-world readiness.
* **Model Evaluation:** Analyzed the model's performance using mathematical metrics like `R2 Score` and `Mean Squared Error (MSE)`.

## 🛠️ Key Challenges & Problem Solving
* **The "Negative Sales" Issue:** Encountered a core limitation of Linear Regression when it predicted negative sales (-8.21) for low-activity days. This taught me that models lack business "common sense" and only follow mathematical equations.
* **Data Engineering Magic:** Instead of changing the model, I engineered the data. By correctly mapping the 'Holiday' variable, the model quickly caught the hidden pattern. 
* **Final Result:** This simple data manipulation boosted my model's accuracy (R2 Score) to a solid **85%** and drastically reduced the error rate.

## 💻 Tech Stack Used
* **Language:** Python
* **Libraries:** Pandas (Data Handling), Scikit-Learn (ML & Metrics)
