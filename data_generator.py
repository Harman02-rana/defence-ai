import pandas as pd
import random

data = []

for _ in range(1000):
    fatigue = random.randint(1, 10)
    sleep = random.randint(1, 10)
    stress = random.randint(1, 10)
    mission_intensity = random.randint(1, 10)
    
    risk_score = fatigue + stress + mission_intensity - sleep
    if risk_score <= 15:
        risk = "LOW"
    elif risk_score <= 22:
        risk = "MEDIUM"
    else:
        risk = "HIGH"
    
    data.append([fatigue, sleep, stress, mission_intensity, risk])

df = pd.DataFrame(data, columns=["fatigue","sleep","stress","mission_intensity","risk"])
df.to_csv("soldier_data.csv", index=False)
print("Dataset created: soldier_data.csv")
