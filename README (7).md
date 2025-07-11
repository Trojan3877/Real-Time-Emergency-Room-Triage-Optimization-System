
# 🏥 MediTriage AI

**Real-Time Emergency Room Triage Optimization System**

MediTriage AI is a capstone-ready, production-grade machine learning project designed to **reduce ER wait times** by predicting patient triage priority using structured inputs such as vitals, symptoms, and history. Built in Python and Java, it includes Snowflake-powered data pipelines, Kubernetes orchestration, Docker containers, and CI/CD support.

---

## 🚀 Project Goals

- 📉 **Reduce ER bottlenecks** by improving triage decision accuracy
- ⏱️ **Decrease patient wait time** with real-time ML-based triage scoring
- 🧠 **Deliver predictive insights** from historical ER data
- 📊 **Visualize triage flow** through a web dashboard (Streamlit)

---

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

