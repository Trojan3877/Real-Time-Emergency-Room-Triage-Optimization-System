#!/bin/sh
# entrypoint.sh
# Trains the model on first run (if the pkl file is absent), then launches the Streamlit UI.

set -e

MODEL_PKL="ml_model/triage_model.pkl"

if [ ! -f "$MODEL_PKL" ]; then
    echo "[entrypoint] Model not found — running train_model.py …"
    python train_model.py
    echo "[entrypoint] Training complete."
else
    echo "[entrypoint] Model already exists — skipping training."
fi

echo "[entrypoint] Starting Streamlit app …"
exec streamlit run app.py --server.port=8501 --server.address=0.0.0.0
