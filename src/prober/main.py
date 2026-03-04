import time
import subprocess
import re
from prometheus_client import start_http_server, Gauge

TARGET_IP = "8.8.8.8"

# Definimos las métricas que Prometheus va a leer
# Gauge es un tipo de métrica que puede subir y bajar (ideal para latencia)
PING_LATENCY = Gauge('netwatch_ping_latency_ms', 'Latencia del ping en milisegundos', ['target'])
PING_STATUS = Gauge('netwatch_ping_status', 'Estado del ping (1=Up, 0=Down)', ['target'])

def ping_target(ip):
    try:
        # Ejecuta un ping de 1 paquete
        output = subprocess.check_output(["ping", "-c", "1", ip], universal_newlines=True)
        
        # Buscamos el valor de "time=X.X" en la salida del comando usando Regex
        match = re.search(r'time=([\d.]+)', output)
        if match:
            latency = float(match.group(1))
            print(f"[OK] {ip} -> Latencia: {latency} ms")
            
            # Actualizamos las métricas para Prometheus
            PING_LATENCY.labels(target=ip).set(latency)
            PING_STATUS.labels(target=ip).set(1)
            
    except subprocess.CalledProcessError:
        print(f"[FALLO] No se pudo alcanzar a {ip}")
        # Si falla, ponemos la latencia en 0 y el estado en 0 (Down)
        PING_LATENCY.labels(target=ip).set(0)
        PING_STATUS.labels(target=ip).set(0)

if __name__ == "__main__":
    print("Iniciando Net-Watch Prober...")
    
    # Levantamos el servidor de métricas de Prometheus en el puerto 8000
    start_http_server(8000)
    print("Servidor de métricas expuesto en el puerto 8000 (/metrics)")
    
    # Bucle infinito de monitoreo
    while True:
        ping_target(TARGET_IP)
        time.sleep(5)