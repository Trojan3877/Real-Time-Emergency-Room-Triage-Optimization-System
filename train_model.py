"""
train_model.py

Trains a machine learning classifier to predict ER triage priority based on patient data.
Uses scikit-learn with a RandomForestClassifier. Outputs the model and training metrics.
"""

import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load and preprocess data
data = pd.read_csv("../database/patient_records_sample.csv")

# Basic preprocessing (assumes columns like 'age', 'bp', 'hr', 'symptom_code', 'priority_level')
X = data.drop(columns=['priority_level'])  # Features
y = data['priority_level']  # Target (triage category: 1-Immediate, 2-Urgent, 3-Low)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, "../ml_model/triage_model.pkl")
print("Model saved to ../ml_model/triage_model.pkl")
