import pandas as pd

# Load datasets
crop_data = pd.read_csv("datasets/Crop_recommendation.csv")
fertilizer_data = pd.read_csv("datasets/Fertilizer Prediction.csv")

# Check for missing values
print("Crop Data Missing Values:\n", crop_data.isnull().sum())
print("Fertilizer Data Missing Values:\n", fertilizer_data.isnull().sum())

# Fill or drop missing values if any
crop_data = crop_data.dropna()
fertilizer_data = fertilizer_data.dropna()

print("Data Preprocessing Done")
