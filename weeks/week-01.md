---
title: Semana 01 — Arquitectura CPS + setup del repo + benchmark kickoff
parent: Semanas
nav_order: 1
---

## Objetivo (medible)
Al finalizar la semana, el equipo debe:
1. Tener el **sitio del curso** (Just-the-Docs) publicado y navegable.
2. Definir una **arquitectura CPS de referencia** (MCU ↔ local ↔ nube ↔ UI) con diagramas.
3. Justificar una **selección de stack** (tipo “armado con presupuesto”) con trade-offs.
4. Implementar y ejecutar un **benchmark base** (TCP/UDP) y registrar métricas en `bench/results.csv`.

---

## Conceptos mínimos (lectura breve)
- CPS como sistema integrado: físico + cómputo + comunicación + decisión + humano.
- Arquitectura por capas: **embebido → transporte → mensajería → servicios → UI → persistencia → seguridad**.
- Selección de protocolos por evidencia: **latencia (p50/p95), jitter, pérdida, throughput**.
- “Punto de quiebre”: la tasa máxima donde el sistema sigue estable (criterio definido).

---

## Práctica A — Setup del repo y publicación
1. Verifica que en el repo existan (o crea) estas páginas:
   - `stack/architecture.md`
   - `stack/contracts.md`
   - `stack/decision-log.md` (la crearemos hoy)
   - `bench/methodology.md`
   - `bench/results.csv`
2. Publica el sitio (GitHub Pages) y valida:
   - que el buscador funcione,
   - que la navegación muestre: Semanas, Stack, Bench, Infra, Seguridad, Recursos.

**Evidencia mínima**
- URL del sitio.
- Captura de pantalla del menú lateral y la portada.

---

## Práctica B — Arquitectura y diagramas (obligatorio)
En `stack/architecture.md` agrega:

### 1) Diagrama a bloques (funcional)
Debe mostrar explícitamente:
- MCU/sensores/actuadores
- Gateway local (Python)
- Broker (MQTT)
- Nube (API)
- UI (dashboard)
- (reservado para Semana 15) Industrial: Modbus/OPC-UA

### 2) Diagrama de despliegue (qué corre dónde)
- MCU (firmware)
- Laptop/PC local (broker + gateway + UI local)
- Nube (API + DB)
- Clientes (web / móvil / HMI)

### 3) Flujo de datos y control
- Telemetría (publish)
- Comandos (control)
- Eventos (alarmas/IA)
- Persistencia (DB)

**Evidencia mínima**
- Diagramas incrustados en la página (imagen o diagrama textual).
- 1 párrafo explicando por qué el stack está así.

---

## Práctica C — Selección del stack (ejercicio tipo “armado con presupuesto”)
En `stack/decision-log.md` documenta:

### 1) Restricciones del sistema (elige valores)
- Presupuesto: $____ MXN por equipo
- Latencia objetivo control: p95 < ____ ms
- Pérdida máxima aceptable: < ____ %
- Throughput mínimo telemetría: ____ msg/s o ____ kbps
- Entorno de red: WiFi / Ethernet / mixto

### 2) Propuesta de stack (BOM + justificación)
Incluye (mínimo):
- MCU (modelo y por qué)
- Sensores/actuadores base
- Transporte local (USB/BLE/WiFi)
- Backbone (MQTT/HTTP/WS)
- Gateway (Python + FastAPI/Flask)
- Nube (Render/VPS)
- DB (candidatos: SQLite/Postgres/Firebase)
- Seguridad mínima (tokens/roles)

### 3) Trade-offs y riesgos
- Riesgo técnico #1, mitigación
- Riesgo técnico #2, mitigación
- Dependencias críticas (drivers, librerías, red)

**Evidencia mínima**
- Tabla BOM.
- Un “Decision” por cada elección (qué se eligió y por qué).

---

## Práctica D — Benchmark kickoff (TCP/UDP) con stress test
### Objetivo del benchmark
Medir en tu red real (al menos PC↔PC o PC↔router):
- Latencia RTT p50/p95
- Jitter
- Pérdida
- Throughput
- Punto de quiebre (incrementando tasa)

### Setup mínimo
- 2 equipos en la misma red (ideal), o un equipo y el router como referencia (limitado).
- Ejecutar los scripts en `bench/tools/` (se agregan abajo).

### Condiciones del experimento (obligatorio)
Fija y registra:
- payload: 64B, 256B, 1024B
- duration: 30s
- rates: 50, 100, 200, 500 msg/s (ajusta según red)

### Criterio de “quiebre”
Declara por escrito:
- quiebre si `loss_pct > 1%` **o** `latency_p95_ms > 100ms` (ajusta valores al curso)

**Evidencia mínima**
- 1 corrida TCP y 1 corrida UDP
- 1 mini-barrido de rates (3–5 puntos)
- `bench/results.csv` actualizado

---

## Registro en `bench/results.csv` (Semana 1)
Agrega al menos 4 filas:
- UDP payload 256B @ 50 msg/s, 100 msg/s, 200 msg/s
- TCP payload 256B @ 50 msg/s (o el máximo estable que encuentres)

En `setup_notes` anota:
- hardware, distancia, WiFi/Ethernet, OS, hora/día (sí, afecta).

---

## Checklist de aceptación (Semana 1)
- [ ] Sitio publicado y navegable
- [ ] `stack/architecture.md` con 3 diagramas (bloques, despliegue, flujo)
- [ ] `stack/decision-log.md` con BOM, restricciones, trade-offs, riesgos
- [ ] Benchmark TCP/UDP ejecutado con logs/evidencia
- [ ] `bench/results.csv` con resultados reales y punto de quiebre
- [ ] Conclusión: “para control usaría __, para telemetría usaría __” (justificada)

---

## Entregables
- URL del sitio
- Actualización de páginas:
  - `stack/architecture.md`
  - `stack/decision-log.md`
- Scripts agregados en:
  - `bench/tools/`
- Resultados en:
  - `bench/results.csv`
- Evidencia (video 30–90s + capturas)

## Referencia: Bench tools (TCP/UDP)
Consulta el instructivo: [Bench Tools — Echo Probes](../bench/tools/bench-tools-guide).
