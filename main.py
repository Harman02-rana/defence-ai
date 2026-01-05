from fastapi import FastAPI
app = FastAPI()

import numpy as np

from backend.model_loader import model
from backend.schemas import SoldierData

app = FastAPI(title="Defence-AI Risk Prediction API")

@app.get("/")
def root():
    return {"status": "Defence-AI backend running"}

@app.post("/predict-risk")
def predict_risk(data: SoldierData):
    input_data = [[
        data.heart_rate,
        data.stress_level,
        data.sleep_hours,
        data.fatigue,
        data.age,
        data.blood_pressure,
        data.oxygen_level,
        data.steps
    ]]

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][prediction]

    risk = "HIGH" if prediction == 1 else "LOW"

    return {
        "status": "EXECUTED",
        "prediction": int(prediction),
        "risk": risk,
        "confidence": round(float(probability), 2),
        "received": data.dict()
    }
