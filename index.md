---
title: Inicio
nav_order: 1
---

# How to Make Almost Cyber-Physical

Bienvenido al curso de **Sistemas Ciberfísicos (CPS)**. El objetivo es construir un **stack completo**:

- **MCU / Embebido** (sensado + actuación)
- **Comunicación** (UART/I2C/SPI → TCP/UDP → MQTT/HTTP/WebSocket)
- **Gateway local (Python)** + **API**
- **Nube** (deploy + observabilidad + seguridad mínima)
- **Industrial** (Modbus/OPC-UA como puente CPS ↔ PLC/HMI/robots)
- **IA** (visión / clasificación) + **LLM** como capa de decisión **auditable**

Una diferencia clave: desde la Semana 1 medimos rendimiento para decidir protocolos:
**latencia (p50/p95), jitter, pérdida de paquetes, throughput** y **punto de quiebre** (stress test).

## Enlaces rápidos
- [Temario y entregables](syllabus)
- [Arquitectura de referencia](stack/architecture)
- [Metodología de benchmarking](bench/methodology)
- [Matriz de protocolos](resources/protocol-matrix)
- [Docker y contenedores](infra/docker)
- [Permisos, auth y CORS](security/auth-permissions)

## Estándar de evidencia (cada semana)
- Video corto (30–90s) demostrando el entregable
- Capturas (logs / dashboards)
- Código en repo + instrucciones reproducibles
- Registro de benchmark en `bench/results.csv`

Fecha de arranque de la versión base: **2025-12-25**.
