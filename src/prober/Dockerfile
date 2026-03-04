FROM python:3.10-slim

# Instalamos la herramienta ping
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instalamos la librería de Prometheus para Python
RUN pip install prometheus-client

COPY main.py .
COPY test_main.py .

CMD ["python", "main.py"]