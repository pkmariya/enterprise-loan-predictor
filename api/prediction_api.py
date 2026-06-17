from fastapi import FastAPI
import numpy as np
import joblib

app = FastAPI()

model = joblib.load('model/loan_model.pkl')

@app.get("/")
def health():
    return {"status": "API is healthy"}

@app.post("/predict")
def predict(
    age: int,
    income: float,
    credit_score: int, 
    employment_years: int,
    existing_loan: int
):
    prediction = model.predict([[age, income, credit_score, employment_years, existing_loan]])
    return {"loan_approved": int(prediction[0])}