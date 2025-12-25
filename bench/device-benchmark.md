---
title: Benchmark de dispositivos (tooling)
parent: Bench
nav_order: 4
---

# Benchmark de dispositivos (tooling)

Acompaña Semana 01.

## Script
- `bench/tools/device_bench.py`

## Uso
```bash
python bench/tools/device_bench.py --out bench/device_bench_<equipo>.json
```

## Qué mide
- SHA256 throughput (MB/s)
- zlib compress/decompress (MB/s + ratio)
- JSON encode/decode (ops/s)

## Buenas prácticas
- Mismo modo de energía para todas las corridas.
- Repetir 3 corridas y reportar promedio/variación.
