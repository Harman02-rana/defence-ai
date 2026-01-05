import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1200

data = {
    "distance_km": np.random.uniform(0.5, 50, rows),
    "speed_kmph": np.random.uniform(0, 2000, rows),
    "altitude_m": np.random.uniform(0, 15000, rows),
    "radar_cross_section": np.random.uniform(0.1, 15, rows),
    "heat_signature": np.random.uniform(10, 500, rows),
    "signal_jamming": np.random.randint(0, 2, rows),
    "object_size": np.random.uniform(0.5, 30, rows),
    "time_of_day": np.random.randint(0, 2, rows),
}

df = pd.DataFrame(data)

# Threat logic
def assign_threat(row):
    score = 0
    if row["speed_kmph"] > 900: score += 1
    if row["altitude_m"] > 8000: score += 1
    if row["signal_jamming"] == 1: score += 1
    if row["heat_signature"] > 300: score += 1
    return min(score, 3)

df["threat_level"] = df.apply(assign_threat, axis=1)

df.to_csv("../data.csv", index=False)

print("✅ Defence-AI dataset created")
