# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel

# Class which describes Bank Notes measurements
class Parameters(BaseModel):
    RPM : float  # Revolutions per minute (RPM)
    Current_PhaseA:float  # Current in Phase A (Amps)
    Current_PhaseB:float  # Current in Phase B (Amps)
    Current_PhaseC:float  # Current in Phase C (Amps)
    Voltage_PhaseA:float  # Voltage in Phase A (Volts)
    Voltage_PhaseB:float  # Voltage in Phase B (Volts)
    Voltage_PhaseC:float  # Voltage in Phase C (Volts)
    Temperature:float  # Temperature (Celsius)
    Vibration_X:float  # Vibration in X direction (m/s^2)
    Vibration_Y:float  # Vibration in Y direction (m/s^2)
    Vibration_Z:float   # Vibration in Z direction (m/s^2)
    Acoustic:float  # Acoustic measurement (dB)
    Type:list  # Healthy status (alphabetic)
