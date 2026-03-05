# Net-Watch: Plataforma de Observabilidad de Red (GitOps & CI/CD)

Sistema automatizado de monitoreo de disponibilidad y latencia de red, diseñado con arquitectura Cloud-Native, prácticas DevSecOps y GitOps.

## 🚀 Arquitectura y Tecnologías
* **Prober Service:** Microservicio en Python que ejecuta pruebas ICMP (Ping) y expone métricas en formato Prometheus.
* **Contenedores:** Dockerizado sobre imágenes ligeras (`python:3.10-slim`).
* **CI/CD (DevSecOps):** GitHub Actions con pruebas automatizadas y escaneo estático de vulnerabilidades (`Trivy` y `Bandit`).
* **Orquestación:** Kubernetes (Minikube).
* **GitOps:** ArgoCD para la sincronización continua de manifiestos.
* **Observabilidad:** Kube-Prometheus-Stack (Prometheus + Grafana).
**API Gateway (NUEVO):** Microservicio REST desarrollado con FastAPI que actúa como punto de entrada para consultar el estado del monitoreo.
* **Contenedores:** Dockerizados de forma independiente sobre imágenes ligeras (`python:3.10-slim`).

---

## Despliegue

### 1. Pipeline CI/CD (GitHub Actions)
El flujo automatizado compila, escanea y publica la imagen en Docker Hub ante cada commit en la rama `main`.

![Pipeline CI/CD](imagenes/github-actions.png)

### 2. Despliegue GitOps (ArgoCD)
ArgoCD monitorea este repositorio y despliega automáticamente los recursos en Kubernetes (`Deployment`, `Service`, `ServiceMonitor`).

![ArgoCD Sync](imagenes/argocd-sync.png)

### 3. Observabilidad (Grafana)
Las métricas generadas por el Prober (`netwatch_ping_latency_ms`) son recolectadas por Prometheus y visualizadas en tiempo real en Grafana.

![Dashboard Grafana](imagenes/grafana-dashboard.png)

### 4. API REST (Swagger UI)
El microservicio de la API expone los endpoints de consulta de estado (`/api/v1/network/status`) y salud (`/health`), autogenerando su documentación interactiva mediante Swagger.
![Health Check](imagenes/healtcheck-api.png)

![Server Response](imagenes/server-response-api.png)

![Server Response](imagenes/network-status-api.png)


![Server Response](imagenes/server-response-network-status.png
)


---

## 🛠️ Estructura del Proyecto
- `/src/prober/`: Código fuente y Dockerfile del agente medidor de latencia.
- `/src/api/`: Código fuente y Dockerfile de la API REST Gateway.
- `/k8s/`: Manifiestos de Kubernetes (Deployments, Services, ServiceMonitor).
- `/.github/workflows/`: Definición del pipeline de Integración Continua multi-imagen.