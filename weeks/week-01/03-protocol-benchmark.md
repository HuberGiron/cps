---
title: 03 — Benchmark de protocolos (TCP/UDP) + stress test
parent: Semana 01 — Fundamentos CPS + Benchmarks + Web + Just-the-Docs
nav_order: 3
---

# Benchmark de protocolos (TCP/UDP) + stress test

**Meta:** medir latencia (p50/p95), jitter, pérdida, throughput y punto de quiebre.

## Instructivo del curso
- `bench/tools/bench-tools-guide.md` (ya lo tienes del paquete anterior)

## Actividad
- Levanta servidores echo (UDP/TCP).
- Corre probes.
- Haz stress test con payload 64/256/1024 y rate 50/100/200/500 msg/s (mínimo).

## Entregable
- `bench/results.csv` actualizado + conclusión (control vs telemetría).
