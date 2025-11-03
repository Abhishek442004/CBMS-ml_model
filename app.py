# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI, Query
import numpy as np
import pickle

# 2. Create the app object
app = FastAPI()
pickle_in = open("random_forest_model.pkl", "rb")
classifier = pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
# @app.get('/{name}')
# def get_name(name: str):
#     return {'Welcome To Krish Youtube Channel': f'{name}'}

# 5. Expose the prediction functionality with required fields in query parameters
@app.get('/predict')
def predict_banknote(
    RPM : float = Query(..., description="Revolutions per minute (RPM)"),
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
    Acoustic: float = Query(..., description="Acoustic measurement (dB)"),
    # Type: float = Query(..., description="Value of Healthy status")
):
    # Predict using the model
    prediction = classifier.predict([[RPM, Current_PhaseA, Current_PhaseB, Current_PhaseC,
                                     Voltage_PhaseA, Voltage_PhaseB, Voltage_PhaseC,
                                     Temperature, Vibration_X, Vibration_Y, Vibration_Z,
                                     Acoustic]])
    
    # Convert the prediction (numpy.ndarray) to a Python list and return as JSON
    prediction_str = prediction[0]  # Get the first element of the array

    return {
        # 'Voltage_RMS': Voltage_RMS,
        # 'Current_RMS': Current_RMS,
        # 'Temperature': Temperature,
        # 'Vibration': Vibration,
        # 'Acoustic': Acoustic,
        # 'Speed': Speed,
        'prediction': prediction_str
    }

# 6. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
