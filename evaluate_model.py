"""
evaluate_model.py

Evaluates the saved triage prediction model on a test dataset.
Generates precision, recall, AUC, and confusion matrix.
"""

import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)
from sklearn.model_selection import train_test_split

# Load data and model
data = pd.read_csv("../database/patient_records_sample.csv")
model = joblib.load("../ml_model/triage_model.pkl")

# Features/target split
X = data.drop(columns=['priority_level'])
y = data['priority_level']

# Train/test split
_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Predictions
y_pred = model.predict(X_test)

# Metrics
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='weighted')
rec = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(f"Accuracy: {acc:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall: {rec:.4f}")
print(f"F1 Score: {f1:.4f}")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=[1,2,3], yticklabels=[1,2,3])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("../metrics/confusion_matrix.png")
plt.close()

print("Confusion matrix saved to ../metrics/confusion_matrix.png")
