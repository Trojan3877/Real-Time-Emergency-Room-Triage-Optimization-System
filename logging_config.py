"""
logging_config.py

Configures JSON logging for MediTriage AI system.
"""

import logging
import json_log_formatter

class CustomJsonFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message, extra, record):
        extra['severity'] = record.levelname
        extra['logger'] = record.name
        extra['message'] = message
        return extra

formatter = CustomJsonFormatter()

json_handler = logging.StreamHandler()
json_handler.setFormatter(formatter)

logger = logging.getLogger("meditriage")
logger.setLevel(logging.INFO)
logger.addHandler(json_handler)
logger.propagate = False

# Example usage
if __name__ == "__main__":
    logger.info("Model started", extra={"module": "inference", "model": "triage_rf_v1"})
