---
title: Bench Tools — Echo Probes (Semana 1)
parent: Bench
nav_order: 3
---

# Bench Tools — Echo Probes (Semana 1)

Este instructivo explica los scripts de benchmarking TCP/UDP usados desde Semana 1 para medir:

- Throughput (msg/s y Mbps)
- Latencia RTT (p50, p95)
- Jitter (dispersión)
- Pérdida (%)
- Punto de quiebre (stress test)

## 1) Fundamento teórico (mínimo)

### RTT vs one-way latency
Medimos RTT (ida+vuelta) porque no requiere sincronizar relojes.

### Percentiles p50 y p95
- p50 (mediana): típico.
- p95: “peor caso frecuente” (muy relevante para control).

### Jitter
Variabilidad de la latencia. Jitter alto degrada el control.

### Pérdida
loss(%) = (sent - recv) / sent * 100  
En UDP se manifiesta como pérdida; en TCP se manifiesta como retransmisión (aumenta p95).

### Throughput (aprox.)
throughput(Mbps) = recv * payload_bytes * 8 / (duration_s * 1e6)

### Punto de quiebre
Incrementamos rate (msg/s) hasta fallar por:
- pérdida > 1% o
- p95 > umbral (ej. 100 ms)

El último punto “stable” es el máximo sostenible.

## 2) Scripts

### Servidores (eco)
- `udp_echo_server.py`: eco UDP
- `tcp_echo_server.py`: eco TCP

### Probes (cliente)
- `udp_probe.py`
- `tcp_probe.py`

Formato del paquete:
- `seq` (uint32): para pérdida
- `t0_us` (uint64): timestamp para RTT
- `padding`: fuerza tamaño de payload

Salida:
`RESULT sent=... recv=... loss_pct=... throughput_mbps=... lat_p50_ms=... lat_p95_ms=... jitter_ms=...`

## 3) Ejecución

Servidor:
```bash
python bench/tools/udp_echo_server.py
python bench/tools/tcp_echo_server.py
```

Cliente (cambia IP):
```bash
python bench/tools/udp_probe.py --host 192.168.1.10 --port 9001 --payload 256 --rate 100 --duration 30
python bench/tools/tcp_probe.py --host 192.168.1.10 --port 9002 --payload 256 --rate 100 --duration 30
```

## 4) Stress test recomendado

Condiciones:
- payload: 64, 256, 1024 bytes
- duration: 30 s
- rate: 50, 100, 200, 500, 1000 msg/s (ajusta)

Ejemplo:
```bash
python bench/tools/udp_probe.py --host 192.168.1.10 --payload 256 --rate 50  --duration 30
python bench/tools/udp_probe.py --host 192.168.1.10 --payload 256 --rate 100 --duration 30
python bench/tools/udp_probe.py --host 192.168.1.10 --payload 256 --rate 200 --duration 30
python bench/tools/udp_probe.py --host 192.168.1.10 --payload 256 --rate 500 --duration 30
```

## 5) Registro en `bench/results.csv`
Para cada corrida, agrega una fila con: protocolo, payload, rate, p50/p95, jitter, pérdida, throughput y notas del setup.

## 6) Limitaciones
- UDP puede perder/reordenar paquetes.
- TCP oculta pérdidas vía retransmisión → sube p95.
- `time.sleep()` limita tasas muy altas; para Semana 1 es suficiente.
