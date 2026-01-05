import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# -------------------------
# Step 1: Prepare sample data
# -------------------------
data = {
    'feature1': [5, 7, 8, 2, 6, 9, 1, 4],
    'feature2': [3, 2, 7, 5, 8, 9, 1, 0],
    'label':    [0, 1, 1, 0, 1, 1, 0, 0]
}

df = pd.DataFrame(data)

X = df[['feature1', 'feature2']]
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------
# Step 2: Train model
# -------------------------
model = RandomForestClassifier()
model.fit(X_train, y_train)

# -------------------------
# Step 3: Save model
# -------------------------
with open('ML/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model saved as ML/model.pkl")
