from fastapi import FastAPI
import numpy as np

from backend.model_loader import model
from backend.schemas import SoldierData

app = FastAPI(title="Defence-AI Risk Prediction API")

@app.get("/")
def root():
    return {"status": "Defence-AI backend running"}

@app.post("/predict-risk")
def predict_risk(data: SoldierData):
    input_data = np.array([[  
        data.fatigue,
        data.sleep,
        data.stress,
        data.mission_intensity
    ]])

    prediction = model.predict(input_data)[0]

    risk_label = "HIGH" if prediction == 1 else "LOW"

    return {
        "risk": risk_label
    }
