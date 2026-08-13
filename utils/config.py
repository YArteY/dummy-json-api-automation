import os

BASE_URL = os.getenv("BASE_URL", "https://dummyjson.com")

DEFAULT_HEADERS = {"Content-Type": "application/json"}

# Tiempo máximo (en segundos) aceptado por las respuestas
MAX_RESPONSE_TIME_SECONDS = float(os.getenv("MAX_RESPONSE_TIME_SECONDS", "2.0"))
