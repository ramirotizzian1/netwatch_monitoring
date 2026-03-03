# Usamos una imagen oficial y muy ligera de Python
FROM python:3.10-slim

# Las imágenes "slim" vienen vacías. Necesitamos instalar la herramienta 'ping' del sistema operativo base (Debian)
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos nuestro script de la computadora al contenedor
COPY main.py .

# Le decimos al contenedor qué comando ejecutar cuando arranque
CMD ["python", "main.py"]