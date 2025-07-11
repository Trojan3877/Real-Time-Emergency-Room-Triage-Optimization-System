├── api_service.java              # Java microservice (integration)
├── app.py                        # FastAPI or Streamlit application
├── dotenv_loader.py              # Loads env variables safely
├── evaluate_model.py             # Model evaluation and metrics
├── logging_config.py             # Logging settings for prod
├── test_model.py                 # Unit and integration tests
├── train_model.py                # ML training pipeline
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Container spec
├── k8s_deployment.yaml           # Kubernetes deployment config
├── main.tf                       # Terraform for cloud infra
├── provision_meditriage.yml      # Ansible playbook for provisioning
├── .env.example                  # Example environment variables
├── .github/workflows/ci.yml      # CI/CD pipeline
├── docs/                         # Diagrams, API spec
├── metrics/                      # Evaluation report and visuals
├── data/                         # Sample or anonymized data
├── notebooks/                    # EDA/model exploration
└── README.md                     # Project overview (this file)
