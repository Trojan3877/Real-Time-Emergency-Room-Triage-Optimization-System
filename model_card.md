# 🧠 Model Card: MediTriageAI

## Overview
MediTriageAI is a machine learning–powered system that assists hospitals in triaging emergency room patients efficiently and fairly. It predicts the urgency level of a patient using medical data like vitals and symptoms, helping hospitals reduce wait times and prioritize care.

---

## Model Details
- **Type**: Random Forest Classifier
- **Training Framework**: scikit-learn
- **Data Source**: Synthetic dataset mimicking ER vitals and records
- **Input Features**:
  - Age
  - Blood Pressure
  - Heart Rate
  - Temperature
  - Symptom Severity Score
- **Output**: Triage Priority (0 = Low, 1 = Urgent, 2 = Immediate)

---

## Intended Use
- Assisting ER staff in early patient prioritization
- Educational tool for triage model design
- Research on ML applications in healthcare queue management

---

## Performance Metrics
- Accuracy: ~87%
- Precision (Immediate): 91%
- Recall (Urgent): 85%
- F1-Score (All Classes): ~0.86

---

## Ethical Considerations
- Model is for **supporting** decisions, not replacing medical staff
- Must be trained on real-world data before live deployment
- Regular auditing needed to detect bias against age or symptoms

---

## Limitations
- Trained on synthetic data, not production-ready
- Does not account for comorbidities or drug allergies
- No NLP symptom parsing (currently tabular inputs only)

---

## License
[MIT License](LICENSE)

---

## Maintainer
Corey Leath – Dual Bachelor's Student in AI + CS at UAT  
GitHub: [@Trojan3877](https://github.com/Trojan3877)
