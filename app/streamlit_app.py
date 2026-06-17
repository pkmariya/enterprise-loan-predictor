import streamlit as st
import requests

st.title("Enterprise Loan Approval Predictor")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income", min_value=0.0, value=50000.0)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=700)
employment_years = st.number_input("Years of Employment", min_value=0, max_value=50, value=5)
existing_loans = st.number_input("Existing Loans")

if st.button("Predict Loan Approval"):
    response = requests.post(
        "http://localhost:8000/predict",
        params={
            "age": age,
            "income": income,
            "credit_score": credit_score,
            "employment_years": employment_years,
            "existing_loan": existing_loans
        }
    )

    if response.status_code == 200:
        result = response.json()
        if result["loan_approved"] == 1:
            st.success("Loan Approved!")
        else:
            st.error("Loan Denied.")
    else:
        st.error("Error in prediction API.")

