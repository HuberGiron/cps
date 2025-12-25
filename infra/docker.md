---
title: Docker y contenedores
nav_order: 1
parent: Infra
---

# Docker y contenedores (mínimo viable)

Usaremos Docker para:
- reproducibilidad (mismo entorno en todas las máquinas),
- despliegue (local → nube),
- separar servicios (broker, gateway, UI).

## Docker Compose base (broker MQTT + gateway)
Archivo sugerido: `docker-compose.yml`

```yaml
services:
  mqtt:
    image: eclipse-mosquitto:2
    ports:
      - "1883:1883"
    volumes:
      - ./infra/mosquitto.conf:/mosquitto/config/mosquitto.conf:ro

  gateway:
    build: ./services/gateway
    environment:
      - MQTT_HOST=mqtt
      - MQTT_PORT=1883
      - API_TOKEN=changeme
    ports:
      - "8000:8000"
    depends_on:
      - mqtt
```

## Buenas prácticas
- Secrets por variable de entorno (no hardcode).
- Logs estructurados.
- Healthcheck en API (`/status`).
