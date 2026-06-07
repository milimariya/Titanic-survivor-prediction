# 🚢 Titanic Survival Prediction System

## 📌 Project Overview

This project is a Machine Learning web application that predicts whether a passenger would have survived the Titanic disaster based on passenger information such as passenger class, gender, age, and fare.

The model was trained using the Titanic dataset and deployed using Flask, allowing users to make predictions through a web interface and API.

---

## 🎯 Objectives

* Perform data preprocessing and cleaning
* Train a Machine Learning classification model
* Save the trained model for future use
* Build a Flask API for predictions
* Create a user-friendly web interface
* Test API endpoints using Postman

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Flask
* HTML
* Postman
* Git & GitHub

---

## 📊 Machine Learning Workflow

1. Load Titanic dataset
2. Handle missing values
3. Convert categorical data into numerical format
4. Select relevant features
5. Train Logistic Regression model
6. Save trained model as `titanic_model.pkl`
7. Build Flask API
8. Test predictions using Postman
9. Create a web interface for user interaction

---

## 📂 Project Structure

```text
titanic-prediction/
│
├── app.py
├── titanic_model.pkl
├── titanic.ipynb
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## 🚀 Features

* Titanic survival prediction
* Flask REST API
* Interactive web interface
* Saved machine learning model
* Real-time predictions
* Postman API testing

---

## 🔮 Sample Input

```json
{
    "Pclass": 3,
    "Sex": 1,
    "Age": 22,
    "Fare": 7.25
}
```

---

## 📈 Sample Output

```json
{
    "prediction": "Did Not Survive"
}
```

---

## ▶️ Running the Project

### Install Dependencies

```bash
pip install pandas numpy scikit-learn flask joblib
```

### Run Flask Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## 📚 Learning Outcomes

Through this project I learned:

* Data preprocessing techniques
* Classification using Logistic Regression
* Model serialization using Joblib
* Building APIs with Flask
* API testing with Postman
* Creating web interfaces using HTML
* Version control with Git and GitHub

---

## 👩‍💻 Author

Mili Mariya

Machine Learning and Web Development Enthusiast
