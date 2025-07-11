"""
test_model.py

Unit tests for MediTriage model using pytest.
"""

import pytest
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

@pytest.fixture
def sample_data():
    df = pd.read_csv("database/patient_records_sample.csv")
    X = df.drop(columns=["priority_level"])
    y = df["priority_level"]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def test_model_loads():
    model = joblib.load("ml_model/triage_model.pkl")
    assert isinstance(model, RandomForestClassifier)

def test_model_accuracy(sample_data):
    X_train, X_test, y_train, y_test = sample_data
    model = joblib.load("ml_model/triage_model.pkl")
    acc = model.score(X_test, y_test)
    assert acc > 0.7, f"Model accuracy too low: {acc}"
