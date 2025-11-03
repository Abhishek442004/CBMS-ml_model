# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020
@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import pickle

# 2. Create the app object
app = FastAPI()

# 3. Enable CORS for your frontend hosted on Render
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Load your trained ML model
pickle_in = open("random_forest_model.pkl", "rb")
classifier = pickle.load(pickle_in)

# 5. Index route
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 6. Prediction route
@app.get('/predict')
def predict_banknote(
    RPM: float = Query(..., description="Revolutions per minute (RPM)"),
    Current_PhaseA: float = Query(..., description="Current in Phase A (Amps)"),
    Current_PhaseB: float = Query(..., description="Current in Phase B (Amps)"),
    Current_PhaseC: float = Query(..., description="Current in Phase C (Amps)"),
    Voltage_PhaseA: float = Query(..., description="Voltage in Phase A (Volts)"),
    Voltage_PhaseB: float = Query(..., description="Voltage in Phase B (Volts)"),
    Voltage_PhaseC: float = Query(..., description="Voltage in Phase C (Volts)"),
    Temperature: float = Query(..., description="Temperature (Celsius)"),
    Vibration_X: float = Query(..., description="Vibration in X direction (m/s^2)"),
    Vibration_Y: float = Query(..., description="Vibration in Y direction (m/s^2)"),
    Vibration_Z: float = Query(..., description="Vibration in Z direction (m/s^2)"),
    Acoustic: float = Query(..., description="Acoustic measurement (dB)")
):
    # Predict using the model
    prediction = classifier.predict([[
        RPM, Current_PhaseA, Current_PhaseB, Current_PhaseC,
        Voltage_PhaseA, Voltage_PhaseB, Voltage_PhaseC,
        Temperature, Vibration_X, Vibration_Y, Vibration_Z, Acoustic
    ]])

    prediction_str = prediction[0]  # Convert prediction result to string

    return {'prediction': prediction_str}


# 7. Run the API with uvicorn (only for local testing)
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
