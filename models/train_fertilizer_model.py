import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
fertilizer_data = pd.read_csv("datasets/Fertilizer Prediction.csv")

# Convert categorical data to numerical (Soil Type & Crop Type)
fertilizer_data["Soil Type"] = fertilizer_data["Soil Type"].astype("category").cat.codes
fertilizer_data["Crop Type"] = fertilizer_data["Crop Type"].astype("category").cat.codes
fertilizer_data["Fertilizer Name"] = fertilizer_data["Fertilizer Name"].astype("category").cat.codes

# Split features and labels
X = fertilizer_data.drop(columns=["Fertilizer Name"])  # Features
y = fertilizer_data["Fertilizer Name"]  # Target (Fertilizer)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Fertilizer Suggestion Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
with open("models/fertilizer_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")
