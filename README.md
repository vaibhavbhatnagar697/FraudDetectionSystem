# 🛡️ Financial Fraud Detection Using Machine Learning

## 📌 Overview

This project is a Machine Learning-based Financial Fraud Detection System developed to identify fraudulent transactions and analyze fraud patterns within financial data. The application combines data preprocessing, feature engineering, machine learning, and interactive visualizations to help users understand transaction behavior and detect potential fraud.

An interactive Streamlit dashboard provides insights into transaction trends, fraud statistics, model performance, and real-time fraud predictions.

---

## 🚀 Features

### 📊 Interactive Dashboard

* Total Transactions
* Fraud Transactions
* Fraud Rate
* Total Transaction Amount
* Model Performance Metrics

### 📈 Transaction Analysis

* Fraud vs Normal Transaction Distribution
* Transaction Type Analysis
* Daily Transaction Trends
* Transaction Amount Distribution
* Fraud Pattern Visualization

### 🤖 Fraud Prediction

* Real-time transaction classification
* User-friendly prediction interface
* Instant fraud detection results

### 📉 Model Evaluation

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 🗂 Dataset Information

The project uses the PaySim Financial Transaction Dataset.

| Feature        | Description                         |
| -------------- | ----------------------------------- |
| step           | Time step in hours                  |
| type           | Transaction type                    |
| amount         | Transaction amount                  |
| nameOrig       | Sender account ID                   |
| oldbalanceOrg  | Sender balance before transaction   |
| newbalanceOrig | Sender balance after transaction    |
| nameDest       | Receiver account ID                 |
| oldbalanceDest | Receiver balance before transaction |
| newbalanceDest | Receiver balance after transaction  |
| isFraud        | Fraud label (0 = Normal, 1 = Fraud) |
| isFlaggedFraud | Flagged suspicious transaction      |

---

## 🧠 Project Workflow

### 1. Data Preprocessing

* Data Cleaning
* Handling Missing Values
* Feature Engineering
* Feature Scaling
* Label Encoding
* Exploratory Data Analysis
* Splitting Data

### 2. Model Development

The following machine learning algorithms were evaluated:

* Logistic Regression
* Decision Tree Classifier
* Naive Bayes (Gaussian NB and Bernoulli NB)
* Random Forest Classifier

### 3. Model Evaluation

Models were compared using:

* Accuracy
* Precision
* Recall
* F1 Score

The final model was selected based on overall classification performance and fraud detection capability.

### 4. Hyperparamter Tuning

* Obtain final model by Randomized Search cv

---

## 📊 Dashboard Pages

### 🏠 Dashboard

Provides an overview of key fraud detection metrics and business insights.

### 🤖 Prediction

Allows users to enter transaction details and predict whether a transaction is fraudulent.

### ⚖️ Model Comparison

Compares different models and selects best one on the basis of confusion Matrix (Recall and Precision).

### 📈 Data Insights

Highlights the most influential features and important facts of raw data.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn

### Data Visualization

* Plotly
* Plotly Express

### Web Application

* Streamlit

### Model Serialization

* Joblib

---

## 📂 Project Structure

```text
Financial-Fraud-Detection/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── dt_dest_encoder.pkl
│   └── dt_model.pkl
│   └── dt_scaler.pkl
│   └── dt_type_encoder.pkl
│   └── gb_model.pkl
│   └── rf_model.pkl
│
├── notebooks/
│   └── file.ipynb
│
├── pages/
│   ├── dashboard.py
│   ├── prediction.py
│   ├── model_comparison.py
│   └── data_insights.py
│
├── app.py
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to the Project Directory

```bash
cd Financial-Fraud-Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📈 Key Insights

* Fraudulent transactions represent a very small percentage of total transactions.
* Certain transaction types are more likely to be associated with fraud.
* Transaction amount and balance-related features play a significant role in fraud detection.
* Proper evaluation using Precision, Recall, and F1 Score is essential for imbalanced datasets.

---

## 🎯 Future Enhancements

* Advanced Feature Engineering
* Hyperparameter Optimization
* Real-Time Transaction Monitoring
* Model Explainability (SHAP)
* Deployment on Cloud Platforms
* REST API Integration

---

## 👨‍💻 Author

**Vaibhav Bhatnagar**

B.Tech Computer Engineering
J.C. Bose University of Science and Technology, YMCA Faridabad

---

### ⭐ If you found this project useful, consider giving it a star on GitHub.
