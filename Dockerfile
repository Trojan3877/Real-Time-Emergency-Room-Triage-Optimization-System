# Dockerfile
# Base image for Python ML model
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    && apt-get clean

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire application code
COPY . .

# Expose Streamlit app port (optional UI)
EXPOSE 8501

# Default command to run model training
CMD ["python", "ml_model/train_model.py"]
