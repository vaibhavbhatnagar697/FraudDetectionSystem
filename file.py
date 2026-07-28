import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from pages.dashboard import show_dashboard
from pages.data_insights import show_data_insights
from pages.model_comparison import show_model_comparison
from pages.prediction import show_prediction

# Set page config 
st.set_page_config(
    page_title="Fraud Detection",
    layout="wide"
)

# Import Models,Scalers and Encoders
dt = joblib.load("Models/dt_model.pkl")
gb = joblib.load("Models/gb_model.pkl")
rf = joblib.load("Models/rf_model.pkl")
scaler=joblib.load("Models/dt_scaler.pkl")
type_encoder=joblib.load("Models/dt_type_encoder.pkl")
dest_encoder=joblib.load("Models/dt_dest_encoder.pkl")

# Reading summary data from csv file
@st.cache_data
def load_summary_data():
    return pd.read_csv("./data/processed/summary.csv")
@st.cache_data
def load_data():
    return pd.read_csv("./data/raw/data.csv")
summary_data=load_summary_data()
data=load_data()

# Estimating important parameters
Total_txns=float(load_summary_data()["Total Txns"][0])
Normal_txns=float(load_summary_data()["Normal Txns"][0])
Fraud_txns=float(load_summary_data()["Fraud Txns"][0])
No_of_fraud = (data["isFraud"].value_counts())
No_of_fraud=No_of_fraud[1]
Fraud_Rate=(No_of_fraud/data.shape[0])*100

# Making Sidebar
st.sidebar.title("🛡️ Fraud Detection System")
page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🤖 Prediction",
        "⚖️ Model Comparison",
        "📈 Data Insights"
    ]
)

# If clicked on Dashboard radio btn
if page=="🏠 Dashboard":
    show_dashboard(Total_txns,Normal_txns,Fraud_txns,No_of_fraud,Fraud_Rate,data)

# If clicked on Dashboard radio btn
elif page=="🤖 Prediction":
    show_prediction(dt,scaler,type_encoder,dest_encoder)

# If clicked on Model Comparison
elif page=="⚖️ Model Comparison":
      show_model_comparison()

# If clicked on Data insights
else :
    show_data_insights(data)
    

   


