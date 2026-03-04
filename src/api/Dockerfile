FROM python:3.10-slim

WORKDIR /app

# Instalamos FastAPI y Uvicorn (el servidor web)
RUN pip install --no-cache-dir fastapi uvicorn

COPY main.py .

# Exponemos la API en el puerto 8080
CMD ["uvicorn", "main.py", "--host", "0.0.0.0", "--port", "8080"]