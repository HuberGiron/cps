---
title: Arquitectura de referencia
parent: Stack
nav_order: 1
---

# Arquitectura CPS (referencia)

**Sistema de referencia** (mínimo):  
**MCU/Embebido ↔ Gateway local (Python) ↔ Nube ↔ UI**, con un backbone de mensajería (MQTT) y APIs.

## Componentes
- **Nodo embebido (MCU):** sensores/actuadores, timestamps, seq id.
- **Gateway local (Python):** normaliza telemetría, expone API, aplica políticas (rate limit, validación).
- **Broker MQTT:** desacopla productores/consumidores; habilita escalabilidad.
- **Nube:** API pública, persistencia, observabilidad.
- **UI:** dashboard local/remoto + control.
- **Industrial (semana 15):** puente por Modbus u OPC-UA (y opcionalmente al PLC/HMI/robot).

## Contratos recomendados (mínimo)
- `device_id`, `ts_ms`, `seq`, `topic`, `payload`
- Telemetría: valores con unidades explícitas
- Comandos: estructura validable (no texto libre)

Siguiente: [Contratos de datos](contracts).
