---
title: Matriz de protocolos
nav_order: 1
parent: Recursos
---

# Matriz de protocolos (referencia)

Esta tabla se deriva del archivo de planeación (**Benchmark_Protocolos_Dispositivos.xlsx**) y se usa como mapa rápido
para seleccionar protocolos por aplicación, velocidad y latencia estimada.

## Subconjunto recomendado (los más usados en CPS/IoT/Industrial)
| Protocolo                  | Modelo de Comunicación   | Aplicación   | Velocidad Aproximada                       | Latencia Estimada   |
|:---------------------------|:-------------------------|:-------------|:-------------------------------------------|:--------------------|
| CANopen                    | Maestro-Esclavo          | Automotriz   | 1 Mbps                                     | 1-5 ms              |
| LIN                        | Maestro-Esclavo          | Automotriz   | 20 kbps                                    | 5-10 ms             |
| Bluetooth (Clásico)        | Maestro-Esclavo          | Computo      | 1-3 Mbps (v2.0+EDR), hasta 50 Mbps (v5.0)  | 10-100 ms           |
| HTTP/HTTPS                 | Cliente-Servidor         | Computo      | ~10 Mbps - 1 Gbps                          | 100-300 ms          |
| TCP/UDP                    | Peer-to-Peer             | Computo      | ~100 Mbps                                  | 1-10 ms             |
| WebSocket                  | Streaming/Full-Duplex    | Computo      | ~1-10 Mbps                                 | 10-100 ms           |
| Wi-Fi (IEEE 802.11n/ac/ax) | Cliente-Servidor         | Computo      | 72 Mbps – >1 Gbps (según estándar y canal) | 1-10 ms             |
| I2C                        | Serial Fisico            | Embebido     | 100 kbps - 3.4 Mbps                        | 1-10 ms             |
| SPI                        | Serial Fisico            | Embebido     | 10+ Mbps                                   | 1-2 ms              |
| UART                       | Serial Fisico            | Embebido     | Hasta 1 Mbps                               | 1-10 ms             |
| Bluetooth Low Energy (BLE) | Maestro-Esclavo          | IOT          | 125 kbps - 2 Mbps                          | 7-50 ms             |
| MQTT                       | Pub-Sub                  | IOT          | ~1-10 Mbps típico                          | 10-50 ms            |
| EtherCAT                   | Peer-to-Peer             | Industrial   | 100 Mbps                                   | 1 ms                |
| Modbus RTU                 | Maestro-Esclavo          | Industrial   | 9.6 kbps - 115.2 kbps                      | 100-300 ms          |
| Modbus TCP                 | Cliente-Servidor         | Industrial   | ~10 Mbps                                   | 30-200 ms           |

## Tabla completa
- CSV: `data/protocolos.csv` (lista completa)

> Nota: Las cifras son aproximadas. En este curso las validamos con **benchmarks reales**.
