"""
dotenv_loader.py

Loads environment variables from .env file securely.
"""

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access variables
MODEL_PATH = os.getenv("MODEL_PATH")
DATABASE_PATH = os.getenv("DATABASE_PATH")
API_KEY = os.getenv("API_KEY")
LOG_LEVEL = os.getenv("LOG_LEVEL")

print(f"Model Path: {MODEL_PATH}")
print(f"Database Path: {DATABASE_PATH}")
print(f"Log Level: {LOG_LEVEL}")
