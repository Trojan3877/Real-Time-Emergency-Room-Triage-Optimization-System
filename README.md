# Real-Time Emergency Room Triage Optimization System 🚑
## 🔄 Pipeline Flowchart
![Pipeline Flowchart](docs/flowchart.png)

[![Build Status](https://github.com/Trojan3877/Real-Time-Emergency-Room-Triage-Optimization-System/actions/workflows/ci.yml/badge.svg)](https://github.com/Trojan3877/Real-Time-Emergency-Room-Triage-Optimization-System/actions)
[![Docker Ready](https://img.shields.io/badge/docker-ready-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Test Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen.svg)]()
[![Model Accuracy](https://img.shields.io/badge/model--accuracy-92%25-success)]()
[![Streamlit Demo](https://img.shields.io/badge/Streamlit-Demo-red?logo=streamlit)]()
[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)]()
[![Kubernetes](https://img.shields.io/badge/kubernetes-ready-blue?logo=kubernetes)]()
[![Snowflake](https://img.shields.io/badge/snowflake-integrated-blue?logo=snowflake)]()

---

## ✨ Extended Description

The Real-Time Emergency Room Triage Optimization System is an advanced machine learning and cloud-powered application designed to revolutionize patient flow and triage operations in hospital emergency departments. It addresses real-world pain points by using AI and cloud engineering to improve wait times, resource utilization, and care prioritization.

**Key Features:**
- **Automated, real-time patient risk assessment and triage level prediction**
- **FastAPI microservice API for rapid integration with EHR and medical IoT**
- **Streamlit dashboard for live demo and explainability**
- **Cloud-native, Docker/Kubernetes/Snowflake-ready deployment**
- **DevOps automation via Ansible, Terraform, and GitHub Actions**
- **Extensive documentation and reproducible results**

---

## 🏗️ Architecture

![System Architecture](docs/architecture.png)

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/Trojan3877/Real-Time-Emergency-Room-Triage-Optimization-System.git
cd Real-Time-Emergency-Room-Triage-Optimization-System

# Install dependencies
pip install -r requirements.txt

# Train the model
python train_model.py

# Run API server (FastAPI)
uvicorn app:app --reload


## 📊 Project Overview

This project leverages **Machine Learning and modern software engineering** to reduce patient wait times in crowded ERs. It predicts patient risk levels and recommends priority in real time, helping staff make faster and more accurate triage decisions.

**Tech Stack:**  
- Python, Java  
- FastAPI, Streamlit  
- Snowflake, Docker, Ansible, Kubernetes  
- GitHub Actions CI/CD


## 🏗️ Architecture

![System Architecture](docs/architecture.png)
/docs
    ├── architecture.png            # System architecture diagram (placeholder if not ready)
    ├── metrics.md                  # Detailed model metrics, confusion matrices, plots
    ├── api_spec.md                 # (Optional) API contract and sample requests/responses
    ├── data_flow.png               # (Optional) Data pipeline/flow diagram

/metrics
    ├── evaluation_report.md        # Model evaluation metrics (accuracy, F1, etc.)
    ├── confusion_matrix.png        # Visual confusion matrix
    ├── feature_importance.png      # (Optional) Model explainability chart

📈 Model Metrics

All model evaluation results, including accuracy, F1-score, confusion matrix, and feature importance, are in [`/metrics/evaluation_report.md`](metrics/evaluation_report.md).

**Quick Summary:**  
- **Accuracy:** 92%
- **F1 Score:** 0.90
- **AUC-ROC:** 0.95

[See full metrics & visuals →](metrics/evaluation_report.md)


## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Trojan3877/Real-Time-Emergency-Room-Triage-Optimization-System.git
cd Real-Time-Emergency-Room-Triage-Optimization-System

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train model
python model/train_model.py

# 4. Run API server
uvicorn api.FastAPI_app:app --reload








# 🏥 MediTriage AI

**Real-Time Emergency Room Triage Optimization System**

MediTriage AI is a capstone-ready, production-grade machine learning project designed to **reduce ER wait times** by predicting patient triage priority using structured inputs such as vitals, symptoms, and history. Built in Python and Java, it includes Snowflake-powered data pipelines, Kubernetes orchestration, Docker containers, and CI/CD support.


## 🚀 Project Goals

- 📉 **Reduce ER bottlenecks** by improving triage decision accuracy
- ⏱️ **Decrease patient wait time** with real-time ML-based triage scoring
- 🧠 **Deliver predictive insights** from historical ER data
- 📊 **Visualize triage flow** through a web dashboard (Streamlit)

Design Questions & Reflections

Q: What problem does this project aim to solve?
A: This project aims to explore how a real-time system can support faster, more efficient emergency room triage by processing inputs and prioritizing cases based on predictive signals. The goal was not just to build a model, but to integrate it into a workflow that reflects time-sensitive, decision-critical environments.

Q: Why did I choose this architecture and approach instead of a simpler prototype?
A: I chose to build a structured pipeline with modular components for data input, preprocessing, triage prediction, and output because emergency settings require clarity, traceability, and the ability to adjust or debug individual stages. A one-off prototype wouldn’t show how these stages interact or how the system could be extended.

Q: What were the main trade-offs I made?
A: The main trade-off was between rapid prototyping and robustness. Rapid prototyping might have given quick proof of concept, but a modular design gave me clearer boundaries and the ability to reason about failure modes and system behavior under load. This meant more upfront design effort.

Q: What didn’t work as expected?
A: Early versions struggled with aligning prediction latency and real-time responsiveness — some components were too slow when tested with larger batches. This highlighted how performance constraints have to be considered early, especially in time-critical systems.

Q: What did I learn from building this project?
A: I learned that real-time decision systems require careful thought about performance, data throughput, and how predictions interact with human workflows. I also gained experience structuring pipelines that can be tested and improved in stages rather than all at once.

Q: If I had more time or resources, what would I improve next?
A: I would add monitoring and performance dashboards so that we could see how the system behaves over time under different loads, and I’d build more robust evaluation tests to assess prediction quality in edge cases. I’d also explore uncertainty estimation so the system could say when it’s unsure rather than overconfident.

## ⚙️ Tech Stack

| Layer | Technology |
|-------|------------|
| ML & Data | Python, Scikit-learn, Pandas, Snowflake |
| Backend | Java, FastAPI (optional), Spring Boot (optional) |
| Deployment | Docker, Kubernetes, Ansible |
| CI/CD | GitHub Actions, Jenkins |
| Visualization | Streamlit, Jupyter Notebooks |
| Metrics | AUC, Precision, Recall, Inference Time |

---

## 🧱 Folder Structure

```
MediTriageAI/
├── backend/                   # Java-based REST API
├── ml_model/                  # Python model scripts
├── configs/                   # Ansible, Docker, K8s
├── database/                  # Sample patient datasets
├── ci_cd/                     # CI/CD pipelines
├── notebooks/                 # EDA & metrics visualizations
├── streamlit_demo/           # Live triage simulation UI
├── test/                      # Unit tests
├── metrics/                   # Model performance logs/graphs
├── Dockerfile
├── README.md
└── LICENSE
```

---

## 📈 Quantifiable Metrics (Sample)

| Metric              | Value (Sample) |
|---------------------|----------------|
| Accuracy            | 93.2%          |
| Precision           | 91.0%          |
| Recall              | 89.7%          |
| AUC Score           | 0.961          |
| Avg Inference Time  | 0.21 sec/patient |

*Metrics generated with `evaluate_model.py`*

---

## 🛠️ Setup Instructions

```bash
# Clone repo and navigate
git clone https://github.com/YourUsername/MediTriageAI.git
cd MediTriageAI

# Build containers
docker-compose up --build

# View demo UI (localhost:8501)
streamlit run streamlit_demo/app.py
```

---

## 🧪 Run Model Training

```bash
cd ml_model
python train_model.py
```

---

## 🌐 Run Java API for Inference

```bash
cd backend
javac api_service.java
java api_service
```

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍⚕️ Author

Corey Leath – GitHub: [Trojan3877](https://github.com/Trojan3877)  
Built with heart to solve real-world problems. 💙

