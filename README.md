# Net-Watch: Plataforma de Observabilidad de Red

Sistema de monitoreo de disponibilidad y latencia orientado a redes de telecomunicaciones, diseñado bajo una arquitectura de microservicios y principios nativos de la nube (Cloud-Native).

## Arquitectura del Sistema
El proyecto se compone de los siguientes microservicios:
* **Prober Service:** Script en Python encargado de ejecutar pruebas de conectividad (ICMP/Ping) contra nodos de red.
* **API Gateway (En desarrollo):** Servicio RESTful (FastAPI) para la consulta de métricas.
* **Time-Series Database (En desarrollo):** Almacenamiento optimizado para métricas de red (InfluxDB).

## Estado Actual del Despliegue (Fase 1)

### 1. Integración Continua (CI)
Se ha implementado un pipeline automatizado mediante **GitHub Actions** (`.github/workflows/main.yml`) que ejecuta los siguientes stages ante cada cambio en la rama `main`:
* **Linting & Testing:** Ejecución de pruebas unitarias con `pytest`.
* **SAST:** Escaneo estático de vulnerabilidades en el código fuente utilizando `Bandit`.
* **Build:** Construcción automatizada de la imagen Docker.
* **Container Security:** Escaneo de vulnerabilidades en la imagen base mediante `Trivy`.
* **Registry Push:** Publicación automática de la imagen validada en Docker Hub.

### 2. Infraestructura y GitOps
* La infraestructura se gestiona como código (IaC).
* Se ha definido el primer manifiesto de Kubernetes (`prober-deployment.yaml`) para el despliegue del servicio Prober, estableciendo límites de recursos (CPU/RAM) y políticas de actualización de imagen.

## Próximos Pasos (Roadmap)
- [ ] Desplegar un clúster de Kubernetes (Local o Cloud).
- [ ] Configurar ArgoCD para la sincronización continua (GitOps) de los manifiestos.
- [ ] Implementar el stack de observabilidad (Prometheus + Grafana).