---
title: Metodología de benchmarking
nav_order: 1
parent: Bench
---

# Metodología de benchmarking (obligatoria)

La meta es **elegir protocolos por evidencia**, no por preferencia.

## Métricas
- **Throughput**: mensajes por segundo (msg/s) y/o Mbps
- **Latencia**: p50 y p95 (idealmente RTT)
- **Jitter**: dispersión (p95–p50 o desviación estándar)
- **Pérdida**: (enviados - recibidos) / enviados
- **Punto de quiebre**: tasa máxima antes de fallar (pérdida > 1% o p95 excede umbral)

## Procedimiento estándar (stress test)
1. Fija payload (ej. 64B, 256B, 1KB).
2. Corre 30–60s por condición.
3. Incrementa rate (ej. 10, 50, 100, 200, 500, 1000 msg/s).
4. Detecta quiebre y registra el último punto estable.

## Registro
Captura resultados en `bench/results.csv`.
- Incluye hardware, red, distancia, QoS, y parámetros.

Siguiente: [Resultados](results).
