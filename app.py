# app.py

import streamlit as st
import numpy as np
import joblib

# Load trained AI model
model = joblib.load("model.pkl")

# Page configuration
st.set_page_config(page_title="Wind Turbine Fault Detection", layout="centered")

# Header
st.title("Wind Turbine Predictive Maintenance System")
st.markdown("**Hybrid Artificial Intelligence and Mathematical Validation**")
st.markdown("Developed by **Isaac Adeyemi** | July 2025")
st.divider()

# Sidebar instructions
with st.sidebar:
    st.header("Instructions")
    st.write("""
    Enter wind turbine sensor values below and click 'Predict Fault'.

    You can simulate faults by increasing:
    - Vibration
    - Temperature
    - Power deviation
    """)

# Input sliders
st.subheader("Turbine Sensor Inputs")
col1, col2 = st.columns(2)

with col1:
    windspeed = st.slider("Wind Speed (m/s)", 3.0, 25.0, 12.0)
    temperature = st.slider("Temperature (°C)", 20.0, 100.0, 45.0)
    power_output = st.slider("Power Output (Watts)", 100_000.0, 1_000_000.0, 500_000.0)

with col2:
    rotorspeed = st.slider("Rotor Speed (RPM)", 5.0, 100.0, 20.0)
    vibration = st.slider("Vibration Level (mm/s)", 0.1, 1.0, 0.4)

# Prediction button
if st.button("Predict Fault"):
    input_data = np.array([[windspeed, rotorspeed, temperature, power_output, vibration]])
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]

    # AI Prediction Result
    with st.container():
        st.subheader("AI Model Prediction")
        if prediction == 1:
            st.error("Fault Detected — Maintenance Required")
        else:
            st.success("Normal Operation — No Fault Detected")
        st.caption(f"Model's Probability of Fault: **{proba:.2%}**")

    # Physics-based model validation
    rho = 1.225
    Cp = 0.4
    r = 20
    A = np.pi * r**2

    expected_power = 0.5 * rho * Cp * A * windspeed**3
    efficiency = power_output / expected_power
    tsr = (rotorspeed * 2 * np.pi * r / 60) / windspeed

    with st.container():
        st.divider()
        st.subheader("Physics-Based Validation")
        st.metric("Expected Power Output", f"{int(expected_power):,} W")
        st.metric("Efficiency", f"{efficiency:.2%}")
        st.metric("Tip Speed Ratio (TSR)", f"{tsr:.2f}")

        # Show warnings if needed
        issues = []
        if abs(power_output - expected_power) > 100_000:
            issues.append("Power deviation is high (> 100,000 W)")
        if efficiency < 0.3 or efficiency > 0.6:
            issues.append("Efficiency outside optimal range (30% - 60%)")
        if tsr < 3 or tsr > 6:
            issues.append("TSR outside aerodynamic efficiency range (3 - 6)")

        if issues:
            for issue in issues:
                st.warning(issue)
        else:
            st.success("All physics metrics are within safe operating ranges.")

        st.caption("Validation complete.")
