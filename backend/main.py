from fastapi import FastAPI
import numpy as np

from .model_loader import model, scaler
from .schemas import ThreatInput

app = FastAPI(title="Defence AI Threat Detection")

@app.get("/")
def root():
    return {"status": "Defence-AI Backend Running"}

@app.post("/predict")
def predict_threat(data: ThreatInput):
    input_data = np.array([[ 
        data.distance_km,
        data.speed_kmph,
        data.altitude_m,
        data.radar_cross_section,
        data.heat_signature,
        data.signal_jamming,
        data.object_size,
        data.time_of_day
    ]])

    scaled = scaler.transform(input_data)
    prediction = int(model.predict(scaled)[0])

    threat_map = {
        0: "No Threat",
        1: "Low Threat",
        2: "Medium Threat",
        3: "High Threat"
    }

    return {
        "threat_level": prediction,
        "description": threat_map[prediction]
    }
