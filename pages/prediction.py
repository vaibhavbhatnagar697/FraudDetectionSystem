import streamlit as st
import pandas as pd

def show_prediction(dt,scaler,type_encoder,dest_encoder):
    st.title("🤖 Fraud Prediction")
    col1,col2=st.columns(2)
    with col1:
        step=st.datetime_input("Enter Date and Time:",value="00:00:00",step=3600,width=500)
    with col2:
        type=st.selectbox("Enter payment Type:",["CASH_IN","CASH_OUT","DEBIT","PAYMENT","TRANSFER"])
    amount=st.number_input("Enter amount:",min_value=0,step=1000,width=600)
    old_balance_sender=st.number_input("Enter old balance of sender:",min_value=0,step=1000,key="1",width=600)
    new_balance_sender=st.number_input("Enter new balance of sender:",min_value=0,step=1000,key='2',width=600)
    old_balance_receiver=st.number_input("Enter old balance of receiver:",min_value=0,step=1000,key="3",width=600)
    new_balance_receiver=st.number_input("Enter old balance of receiver:",min_value=0,step=1000,key="4",width=600)

    col3,col4=st.columns(2)
    with col3:
        sender_orig=st.selectbox("Enter Origin of sender:",["C","M"],width=500)
    with col4:
        receiver_orig=st.selectbox("Enter Origin of receiver:",["C","M"])

    date_str=str(step.date())
    time_str=str(step.time())

    # Estimating actual parameters
    day=date_str[0]+date_str[1]
    hour=time_str[0]+time_str[1]
    type=type_encoder.transform([type])[0]
    amount=scaler.transform([[amount]])[0]
    old_balance_sender=scaler.transform([[old_balance_sender]])[0]
    new_balance_sender=scaler.transform([[new_balance_sender]])[0]
    old_balance_receiver=scaler.transform([[old_balance_receiver]])[0]
    new_balance_receiver=scaler.transform([[new_balance_receiver]])[0]
    sender_orig=dest_encoder.transform([sender_orig])[0]
    receiver_orig=dest_encoder.transform([receiver_orig])[0]
    
    st.write("")
    col1,col2,col3=st.columns(3)

    with col2:
        isClicked=st.button("🛡️ Predict Fraud",width=320)

    # On clicking on predict button
    if isClicked:
        df={
            "type":type,
            "amount":amount,
            "nameOrig":sender_orig,
            "oldbalanceOrg":old_balance_sender,
            "newbalanceOrig":new_balance_sender,
            "nameDest":receiver_orig,
            "oldbalanceDest":old_balance_receiver,
            "newbalanceDest":new_balance_receiver,
            "day":day,
            "hour":hour
        }
        df=pd.DataFrame(df)
        isFraud=dt.predict(df)
        probability = dt.predict_proba(df)
        print(probability)
        st.write("")

        col1,col2=st.columns(2)
        with col1:
            # If Fraud is detected
            if isFraud[0] == 1:
                st.error("🚨 Fraud Alert — Suspicious Transaction Detected")
            else:
                st.success("🛡️ Transaction Verified — No Fraud Detected")
        with col2:
            st.info(f"🎯 Confidence Score: {probability[0][0]*100:.2f}")