
# Smart Farming AI Assistant

**Smart Farming AI Assistant** is a **Streamlit-based AI assistant** designed to empower farmers with intelligent crop and fertilizer recommendations. By analyzing soil nutrients, weather conditions, and moisture levels, it leverages **pre-trained machine learning models** to predict the most suitable crops and fertilizers. This helps farmers make **data-driven decisions**, enhance productivity, and optimize resource usage, ultimately reducing costs and improving yield efficiency.



## Features  

1. **🌾 Crop Recommendation**  
   - Predicts the most suitable crop for a given piece of land based on soil nutrients (Nitrogen, Phosphorus, Potassium), temperature, humidity, soil pH, and rainfall.  
   - Uses a trained machine learning model (`crop_model.pkl`) to provide accurate suggestions, helping farmers maximize their yield.  

2. **🧪 Fertilizer Recommendation**  
   - Suggests the best fertilizer based on soil type, crop type, moisture level, temperature, humidity, and nutrient levels.  
   - Uses a trained model (`fertilizer_model.pkl`) to ensure optimal fertilization, improving soil health and reducing costs.  

3. **📊 User-Friendly UI (Streamlit)**  
   - Provides an interactive interface where farmers can input their data easily using number inputs and dropdown menus.  
   - Displays instant recommendations in a simple and understandable format, making it accessible even for non-technical users.  

4. **🚀 Fast & Efficient Predictions**  
   - Uses pre-trained machine learning models, making recommendations almost instantly without heavy processing.  
   - Can run on local devices or cloud servers, ensuring accessibility for farmers in different regions with varying internet and hardware capabilities.  
## Installation 

## 1. Clone the Repository
```bash
git clone https://github.com/your-username/smart-farming-ai.git
cd smart-farming-ai
```
OR

*Download the zip file*

## 2. Create a Virtual Environment (Optional but Recommended) 
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

## 3. Install Dependencies 
```bash
pip install -r requirements.txt
```

## 4. Place the Trained Models
Ensure the trained machine learning models (`crop_model.pkl` and `fertilizer_model.pkl`) are inside the `models/` directory.  

---

## Run the Application
```bash
streamlit run app.py
```
This will start the **Smart Farming AI Assistant** in your browser.  



## Usage

- **Monitoring Soil Health**: View real-time data from connected IoT sensors on the dashboard to monitor soil conditions and receive recommendations for irrigation and fertilization.

- **Predicting Crop Yields**: Utilize the predictive analytics feature to forecast crop yields based on current and historical data, aiding in effective resource planning.

## Technologies Used 

1. **Python** – Core programming language for backend logic.  
2. **Streamlit** – Web framework used to build an interactive UI.  
3. **Pandas** – Data processing and handling library.  
4. **Scikit-learn** – Machine learning library for training and using models.  
5. **Pickle** – Used for saving and loading pre-trained ML models.
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

This project was inspired by the need to integrate advanced technologies into agriculture to enhance productivity and sustainability. Special thanks to the contributors and the open-source community for their invaluable support.

Let me know if you need any other modifications!

