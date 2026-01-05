from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import SoldierData

app = FastAPI(title="Defence-AI")

# CORS (already discussed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/predict")
def predict(data: SoldierData):
    # TEMP logic (replace later with ML model)
    risk_score = (
        data.heart_rate * 0.25 +
        data.stress_level * 5 +
        (10 - data.sleep_hours) * 5 +
        data.fatigue_level * 6 +
        data.blood_pressure * 2 +
        (100 - data.oxygen_level) * 0.4 +
        (10000 - data.daily_steps) * 0.001
    )

    if risk_score > 120:
        risk = "HIGH"
    elif risk_score > 70:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "risk_level": risk,
        "risk_score": round(risk_score, 2),
        "received_features": data.dict()
    }
