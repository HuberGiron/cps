---
title: Contratos de datos
parent: Stack
nav_order: 2
---

# Contratos de datos (mínimo viable)

## Telemetría (JSON recomendado)
```json
{
  "device_id": "mcu-01",
  "ts_ms": 1735080000000,
  "seq": 10234,
  "signals": {
    "temp_c": 24.3,
    "v_batt": 3.92,
    "motor_rpm": 1200
  }
}
```

## Comando (control)
```json
{
  "target": "mcu-01",
  "ts_ms": 1735080001234,
  "seq": 554,
  "cmd": "set_motor",
  "args": { "rpm": 900 }
}
```

## Reglas
- `seq` incrementa siempre (sirve para pérdida).
- `ts_ms` en milisegundos.
- Validar rangos antes de actuar (seguridad).

