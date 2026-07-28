import streamlit as st
import plotly.express as px
import pandas as pd
def show_model_comparison():
    st.title("⚖️ Model Comparison")
    # Python sees file relative to current working directory which is file.py only
    cmp_table=pd.read_csv("data/processed/Models_comparison.csv")

    st.write("")
    st.subheader("🏆 Best Model: Random Forest",text_alignment="center")
    col1,col2,col3,col4=st.columns(4)
    
    with col1:
            st.metric("📊 Accuracy:",f"{cmp_table["Accuracy"][4]:.2f}%")
    with col2:
            st.metric("🎯 Precision:", f"{cmp_table["Precision"][4]:.2f}")
    with col3:
            st.metric("🔍 Recall:",f"{cmp_table["Recall"][4]:.2f}")
    with col4:
            st.metric("⚖️ F1 Score:", f"{cmp_table["F1 Score"][4]:.2f}")

    st.write("")
    st.dataframe(cmp_table)

    st.write("")
    col1,col2=st.columns(2)
    with col1:
        recall_bar_fig=px.bar(cmp_table,x="Model",y="Recall",title="Recall",color_discrete_sequence=["#F97316"])
        recall_bar_fig.update_traces(
                texttemplate="%{y:.2f}%",
                textposition="outside"
            )
        st.plotly_chart(recall_bar_fig,use_container_width=True)

        f1_bar_fig=px.bar(cmp_table,x="Model",y="F1 Score",title="F1 Score",color_discrete_sequence=["#22C55E"])
        f1_bar_fig.update_traces(
                texttemplate="%{y:.2f}%",
                textposition="outside"
            )
        st.plotly_chart(f1_bar_fig,use_container_width=True)

    with col2:
        precision_bar_fig=px.bar(cmp_table,x="Model",y="Precision",title="Precision",color_discrete_sequence=["#8B5CF6"])
        precision_bar_fig.update_traces(
                texttemplate="%{y:.2f}%",
                textposition="outside"
            )
        st.plotly_chart(precision_bar_fig,use_container_width=True)

        acc_bar_fig=px.bar(cmp_table,x="Model",y="Accuracy",title="Accuracy",color_discrete_sequence=["#3B82F6"])
        acc_bar_fig.update_traces(
                texttemplate="%{y:.2f}%",
                textposition="outside"
            )
        st.plotly_chart(acc_bar_fig,use_container_width=True)