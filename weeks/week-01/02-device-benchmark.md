---
title: 02 — Benchmark de dispositivos de cómputo “inteligente”
parent: Semana 01 — Fundamentos CPS + Benchmarks + Web + Just-the-Docs
nav_order: 2
---

# Benchmark de dispositivos de cómputo “inteligente”

**Meta:** elegir hardware (laptop/edge/SBC) con evidencia.

---

## Métricas mínimas
### Caracterización
- CPU (modelo, cores/threads)
- RAM (GB)
- Almacenamiento (tipo)
- Red (WiFi/Ethernet/Bluetooth)
- GPU/NPU (si aplica)

### Microbenchmarks
- SHA256 throughput (MB/s)
- zlib compress/decompress (MB/s)
- JSON encode/decode (ops/s)

---

## Tool recomendado (Python, sin dependencias)
Incluido en este patch: `bench/tools/device_bench.py`

Ejecuta:
```bash
python bench/tools/device_bench.py --out bench/device_bench_<equipo>.json
```

---

## Actividad (obligatoria)
1. Selecciona 2 dispositivos.
2. Ejecuta el benchmark en ambos (ideal 3 corridas).
3. Reporta tabla comparativa y conclusión: gateway / IA local.

---

## Entregable
- `bench/device_bench_*.json`
- Página (Just-the-Docs) con tabla y conclusión.
