import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="MediTriage AI", layout="centered")

# Load model
model = joblib.load("ml_model/triage_model.pkl")

st.title("🏥 MediTriage AI")
st.subheader("Real-Time Emergency Room Triage Optimization System")

st.markdown("### 🧾 Enter Patient Information")

# Input fields
age = st.slider("Patient Age", 0, 100, 30)
bp = st.slider("Systolic Blood Pressure", 80, 200, 120)
hr = st.slider("Heart Rate (BPM)", 40, 180, 75)
temp = st.slider("Body Temperature (°F)", 95.0, 105.0, 98.6)
symptom_score = st.slider("Symptom Severity (0 = Mild, 10 = Severe)", 0, 10, 5)

# Create DataFrame
input_data = pd.DataFrame(
    [[age, bp, hr, temp, symptom_score]],
    columns=["age", "blood_pressure", "heart_rate", "temperature", "symptom_score"]
)

# Prediction
if st.button("🚑 Predict Triage Priority"):
    prediction = model.predict(input_data)[0]
    probs = model.predict_proba(input_data)[0]

    priority_map = {0: "🟢 Low", 1: "🟠 Urgent", 2: "🔴 Immediate"}
    st.success(f"Predicted Priority: **{priority_map[prediction]}**")

    st.markdown("#### Prediction Probabilities:")
    st.progress(probs[prediction])
    st.json({
        "Low": f"{probs[0]:.2%}",
        "Urgent": f"{probs[1]:.2%}",
        "Immediate": f"{probs[2]:.2%}"
    })

st.markdown("---")
st.caption("Built by Corey Leath • Dual Bachelor's in AI + CS • GitHub: @Trojan3877")
