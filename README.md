# Wind Turbine Predictive Maintenance System

This project combines Artificial Intelligence and Physics-Based Modeling to predict and validate faults in wind turbines. It uses a trained machine learning model and physical equations to detect operational anomalies from turbine sensor readings.

## Project Overview

- Uses wind speed, rotor speed, temperature, vibration, and power output as input features
- AI model predicts whether the turbine is operating normally or at risk of failure
- Physics-based validation checks turbine performance using expected power, efficiency, and tip speed ratio (TSR)
- Built using Streamlit for an interactive web application interface

---

## Demo

To run the app locally:

```bash
streamlit run app.py
