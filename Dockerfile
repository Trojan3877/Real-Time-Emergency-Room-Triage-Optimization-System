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

# Make entrypoint script executable
RUN chmod +x entrypoint.sh

# Expose Streamlit app port
EXPOSE 8501

# Train model on first run (if absent) then launch the Streamlit UI
ENTRYPOINT ["./entrypoint.sh"]
