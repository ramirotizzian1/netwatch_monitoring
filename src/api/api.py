from fastapi import FastAPI

app = FastAPI(title="Net-Watch API", description="API Gateway para el estado de la red")

@app.get("/health")
def health_check():
    """Endpoint de salud para Kubernetes"""
    return {"status": "ok", "service": "net-watch-api"}

@app.get("/api/v1/network/status")
def network_status():
    """Endpoint que simula devolver el estado actual del monitoreo"""
    return {
        "target_ip": "8.8.8.8",
        "monitoring_status": "Activo",
        "metrics_engine": "Prometheus",
        "message": "El microservicio Prober está ejecutando pruebas ICMP en segundo plano."
    }