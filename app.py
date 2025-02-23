import streamlit as st
import pandas as pd
import pickle

# Load trained models
with open("models/crop_model.pkl", "rb") as f:
    crop_model = pickle.load(f)

with open("models/fertilizer_model.pkl", "rb") as f:
    fertilizer_model = pickle.load(f)

# Soil & Crop type mappings (for fertilizer prediction)
soil_types = {0: "Sandy", 1: "Loamy", 2: "Clayey"}
crop_types = {0: "Wheat", 1: "Rice", 2: "Maize", 3: "Sugarcane"}

# Fertilizer mapping (Fixing numerical output issue)
fertilizer_mapping = {
    0: "Urea", 
    1: "DAP", 
    2: "MOP", 
    3: "SSP", 
    4: "Ammonium Sulphate", 
    5: "Compost"
}

# Streamlit UI
st.set_page_config(page_title="Smart Farming AI Assistant", layout="wide")
st.title("🌱 Smart Farming AI Assistant")

# User inputs for crop recommendation
st.header("🚜 Crop Recommendation")
N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, step=1)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=200, step=1)
K = st.number_input("Potassium (K)", min_value=0, max_value=200, step=1)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, step=0.1)

if st.button("Recommend Crop"):
    crop_prediction = crop_model.predict([[N, P, K, temperature, humidity, ph, rainfall]])
    st.success(f"🌾 Recommended Crop: **{crop_prediction[0]}**")

# User inputs for fertilizer recommendation
st.header("🧪 Fertilizer Suggestion")
soil_type = st.selectbox("Soil Type", options=list(soil_types.values()))
crop_type = st.selectbox("Crop Type", options=list(crop_types.values()))
moisture = st.number_input("Moisture Level (%)", min_value=0.0, max_value=100.0, step=0.1)

if st.button("Suggest Fertilizer"):
    # Convert categorical values to numbers
    soil_index = list(soil_types.keys())[list(soil_types.values()).index(soil_type)]
    crop_index = list(crop_types.keys())[list(crop_types.values()).index(crop_type)]

    # Predict fertilizer
    fertilizer_prediction = fertilizer_model.predict([[temperature, humidity, moisture, soil_index, crop_index, N, P, K]])
    
    # Convert numeric prediction to actual fertilizer name
    fertilizer_name = fertilizer_mapping.get(fertilizer_prediction[0], "Unknown Fertilizer")
    st.success(f"💡 Recommended Fertilizer: **{fertilizer_name}**")

st.markdown("📌 *Powered by Hack_HUstlers* ")
