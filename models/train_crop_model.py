import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
crop_data = pd.read_csv("datasets/Crop_recommendation.csv")

# Split features and labels
X = crop_data.drop(columns=["label"])  # Features (N, P, K, temp, humidity, pH, rainfall)
y = crop_data["label"]  # Target (Crop Type)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Crop Recommendation Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
with open("models/crop_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")
