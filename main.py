from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import joblib
import numpy as np

# Load the model once when the server starts
model = joblib.load("house_price_model.pkl")

app = FastAPI()

# Define the input structure
class HouseFeatures(BaseModel):
    area: int
    bedrooms: int
    location: Optional[str] = "unknown"
    furnished: Optional[bool] = False

# Root endpoint
@app.get("/")
def home():
    return {"message": "House Price Prediction API is running!"}

# Prediction endpoint
@app.post("/predict")
def predict_price(features: HouseFeatures):

    # Prepare input for the model
    input_data = np.array([[features.area, features.bedrooms]])

    # Get prediction
    prediction = model.predict(input_data)

    # Return result
    return {
        "input_received": {
            "area": features.area,
            "bedrooms": features.bedrooms,
            "location": features.location,
            "furnished": features.furnished
        },
        "predicted_price_lakhs": round(float(prediction[0]), 2)
    }