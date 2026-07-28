import streamlit as st
def show_data_insights(data):
    st.title("📈 Data Insights")
    st.write("")
    st.subheader("📋 About the Dataset")
    st.text("This dataset contains financial transactions used to identify fraudulent activities. It includes transaction amounts, account balances, transaction types, and fraud labels. The target variable is isFraud, where 1 indicates fraud and 0 indicates a legitimate transaction.")

    st.write("")
    st.subheader("📊 Quick Statistics")
    st.text(f"""
    • Total Records: {data.shape[0]}
    • Features: {data.shape[1]-1}
    • Transaction Types: 5
    • Problem Type: Binary Classification
    """)

    st.write("")
    st.subheader("💡 Key Findings")
    st.text("""
    • Fraud is concentrated in TRANSFER and CASH_OUT transactions.
    • The dataset is highly imbalanced.
    • Balance-related features are strong indicators of fraud.
    • Most transactions are legitimate.
    """)

    st.write("")
    st.subheader("🔥 Interesting Facts")
    st.text("""
    • Less than 1% of transactions are fraudulent.
    • Fraudulent transactions tend to involve larger amounts.
    • Certain transaction types have significantly higher fraud rates.
    """)