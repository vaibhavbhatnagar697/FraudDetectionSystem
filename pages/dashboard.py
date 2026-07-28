import streamlit as st
import plotly.express as px

# Dashboard
def show_dashboard(Total_txns,Normal_txns,Fraud_txns,No_of_fraud,Fraud_Rate,data):
    st.title("🛡️ AI-Powered Fraud Detection System")
    st.subheader("Real-Time Transaction Risk Analysis")
    st.write("")

    col1,col2,col3,col4=st.columns(4)
    
    with col1:
        st.metric("Total Amount",  f"{Total_txns}",format="compact")
    
    with col2:
        st.metric("Total Transactions", f"{data.shape[0]}",format="compact")
    
    with col3:
        st.metric("Fraud Transactions", f"{No_of_fraud}",format="compact")
    
    with col4:
        st.metric("Fraud Rate",f"{Fraud_Rate:.2f}%")
    
    st.write("")
        
    st.subheader("📊 Dataset Overview")
    col4,col5=st.columns(2)
    with col4:
        fig_pie=px.pie(
                names=["Fraud Txns","Normal Txns"],
                values=[Fraud_txns,Normal_txns],
                title="Fraud vs Normal Transactions",
                color=["Fraud Txns","Normal Txns"],
                color_discrete_map={
                "Normal Txns": "#10B981",
                "Fraud Txns": "#DC2626"
                },
                hole=0.6)
        st.plotly_chart(fig_pie,use_container_width=True)
    with col5:
        bar_data=(data.groupby(["type","isFraud"])["amount"].sum().reset_index())
        bar_data["Status"] = bar_data["isFraud"].map({
                0: "Normal",
                1: "Fraud"
            })
        fig_bar=px.bar(
                    bar_data,
                    x="type",
                    y="amount",
                    color="Status",
                    color_discrete_map={
                        "Normal": "#10B981",
                        "Fraud": "#DC2626"
                    },
                    title="Transaction Type Distribution")
        st.plotly_chart(fig_bar,use_container_width=True)
    
    st.write("")
    st.subheader("💰 Transaction Analysis")
    st.write("")
    box_data=data.sample(50000)
    box_data["Status"]=box_data["isFraud"].map({
        0:"Normal",
        1:"Fraud"
    })
    fig_box=px.box(
                box_data,
                x="Status",
                y="amount",
                color="Status",
                color_discrete_map={
                "Normal": "#10B981",
                "Fraud": "#DC2626"
                },
                title="Fraud vs Non-Fraud Amounts"
            )
    st.plotly_chart(fig_box,use_container_width=True)
    
    line_data=data
    line_data["day"]=line_data["step"]//24
    line_data=(line_data.groupby(["day","isFraud"])["amount"].sum().reset_index())
    line_data["Status"]=line_data["isFraud"].map({
                0:"Normal",
                1:"Fraud"
                })
    print(line_data)
    fig_line=px.line(line_data,x="day",y="amount",color="Status",title="Transactions by Time",color_discrete_map={
                    "Normal": "#10B981",
                    "Fraud": "#DC2626"
        })
    st.plotly_chart(fig_line,use_container_width=True)