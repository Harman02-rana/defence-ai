import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("soldier_data.csv")

X = df[["fatigue","sleep","stress","mission_intensity"]]
y = df["risk"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, "risk_model.pkl")
print("Model trained & saved as risk_model.pkl")
