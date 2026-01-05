import joblib
import os

MODEL_PATH = os.path.join("ML", "risk_model.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model file not found. Train the model first.")
    return joblib.load(MODEL_PATH)

model = load_model()
