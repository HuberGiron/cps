---
title: 06 — Diagramas a bloques y arquitecturas (Canva / Visual Paradigm)
parent: Semana 01 — Fundamentos CPS + Benchmarks + Web + Just-the-Docs
nav_order: 6
---

# Diagramas a bloques y arquitecturas (Canva / Visual Paradigm)

**Meta:** establecer una arquitectura CPS clara (sistemas, subsistemas e interconexiones) y dejarla lista para operación, medición y futuras integraciones industriales (PLC/HMI/UR).

En este curso el diagrama no es “bonito”: es un **artefacto de ingeniería** que debe permitir responder:
- ¿Qué está **dentro** del sistema y qué está **fuera**?
- ¿Qué interfaces existen (físicas y lógicas)?
- ¿Qué protocolo corre por cada enlace?
- ¿Qué tráfico esperamos (payload, tasa, p95, pérdida) y dónde medimos?
- ¿Qué credenciales/permisos/protecciones aplican por interfaz?

---

## 1) Niveles de diagramado (estándar del curso)

### L0 — Contexto (Sistema y actores)
Muestra **tu sistema CPS** como una caja y:
- actores: usuario, operador, mantenimiento, servicios externos,
- entradas/salidas principales,
- objetivos (qué controla / qué monitorea).

**Entrega:** 1 diagrama L0.

### L1 — Bloques funcionales (sistemas y subsistemas)
Descompone en:
- embebido (MCU/sensores/actuadores),
- gateway/local server,
- nube (API/DB),
- UI (web/móvil/HMI),
- industrial (PLC/Robot/OPC-UA/Modbus) *si aplica, aunque sea “placeholder”*.

**Entrega:** 1 diagrama L1.

### L2 — Despliegue físico / red (qué corre dónde)
Representa el “dónde”:
- dispositivos físicos (PC, SBC, PLC, HMI, robot),
- switches/routers,
- enlaces (WiFi/Ethernet/USB/Serial/HDMI),
- y dónde viven los servicios (local vs nube).

**Entrega:** 1 diagrama L2.

> Opcional: **L3 — Secuencias** (login, telemetría, comando, alarma).

---

## 2) Convenciones de notación (para que todos hablen igual)

### 2.1 Cajas y jerarquía
- Caja grande = **Sistema** o **entorno** (p. ej. “Gabinete Robot”, “Nube”).
- Caja mediana = **sub-sistema** (p. ej. “Gateway Python”, “API Flask”).
- Caja pequeña = **componente** (sensor, MCU, DB, dashboard).

### 2.2 Flechas (siempre etiquetadas)
En cada flecha escribe, mínimo:
- **medio** (USB / Serial / WiFi / Ethernet),
- **protocolo** (TCP/UDP/HTTP/MQTT/WebSocket),
- **dirección** (telemetría, comando, auth),
- **formato** (JSON/CSV/CBOR, etc.),
- **tasa esperada** (msg/s o Hz) *si ya la sabes*.

Ejemplo de etiqueta:
`WiFi + UDP | telemetry | JSON | 200 msg/s`

### 2.3 Colores (recomendación)
Usa una leyenda consistente:
- Amarillo: TCP/IP Ethernet
- Morado: Serial
- Verde: I/O
- Cian: USB
- Rosa: HDMI

Si incluyes potencia:
- Rojo: 24V
- Azul: 127V

### 2.4 Estado del diseño
- Línea continua: **implementado**
- Línea punteada: **planeado**
- Flecha doble: bidireccional (si aplica)

---

## 3) Flujo de trabajo (pasos concretos)

### Paso A — Define frontera del sistema
1. ¿Qué *sí* está dentro del CPS del proyecto?
2. ¿Qué *no* (servicios externos, GitHub Pages, Firebase, etc.)?

### Paso B — Lista de componentes
- Dispositivos: MCU, PC, PLC, HMI, Robot UR, cámaras…
- Servicios: API, broker, DB, dashboard.
- Actores: usuario final, operador.

### Paso C — Mapa de interfaces (la parte más importante)
Completa esta tabla (y luego la reflejas en el diagrama):

| From | To | Medio | Protocolo | Dirección | Payload | Rate | Medición (sí/no) |
|---|---|---|---|---|---|---:|---|
| MCU | Gateway | USB | Serial | Telemetría | CSV | 50 msg/s | Sí |
| Gateway | UI | TCP/IP | WebSocket | Streaming | JSON | 10 Hz | Sí |
| API | DB | Nube | Firebase SDK | Read/Write | JSON | n/a | No |

> Regla del curso: **cada enlace relevante** debe poder apuntar a un benchmark (p95/jitter/pérdida/throughput) o justificar por qué no se mide.

### Paso D — Dibuja L0 → L1 → L2
1. Empieza por L0 (contexto).
2. Luego L1 (bloques y flujos).
3. Termina en L2 (despliegue real).

### Paso E — Exporta e integra a Just-the-Docs
- Exporta PNG (ideal 2x) o SVG.
- Guarda en `assets/week-01/diagrams/`.
- Inserta en tu página con:

```md
![Arquitectura L1](../../assets/week-01/diagrams/equipoX_L1.png)
```

---

## 4) Canva vs Visual Paradigm (criterio de uso)

### Canva (recomendado para rapidez y claridad)
Útil para:
- diagramas L0/L1/L2 limpios,
- leyendas de color,
- diagramas “tipo cloud + gabinete”.

Buenas prácticas:
- Usa grid/alineación.
- Bloques con tamaños consistentes.
- Tipografía uniforme.
- Exporta siempre con nombre de versión (v1, v2).

### Visual Paradigm (recomendado si quieres formalidad UML)
Útil para:
- deployment UML,
- component diagrams,
- secuencias L3.

Buenas prácticas:
- No te “pierdas” en UML: si el diagrama no se entiende en 30 segundos, está demasiado complejo.

---

## 5) Checklist de revisión (antes de entregar)
- [ ] ¿Existe L0, L1 y L2?
- [ ] ¿Hay frontera del sistema explícita?
- [ ] ¿Cada flecha tiene etiqueta (medio+protocolo+dirección)?
- [ ] ¿Existe leyenda de colores?
- [ ] ¿Se distinguen telemetría vs comando vs auth?
- [ ] ¿Hay referencias a medición (bench) por enlace crítico?
- [ ] ¿El diagrama permite detectar “puntos únicos de falla” (router, broker, API)?

---

## 6) Entregables (Semana 1)
1. **3 diagramas**: L0, L1, L2 (PNG/SVG).
2. Tabla “Mapa de interfaces” completa en tu `report.md`.
3. Breve conclusión (10–15 líneas):
   - Top 2 enlaces críticos y cómo los vas a medir.
   - Top 2 riesgos de integración (y mitigación).

---

## 7) Rúbrica rápida (10 puntos)
- (2) L0 claro (actores + frontera)
- (3) L1 completo (bloques + flujos + etiquetas)
- (2) L2 realista (dispositivos + red + dónde corre cada servicio)
- (2) Tabla de interfaces completa y consistente con diagramas
- (1) Integración correcta a Just-the-Docs (enlaces y assets)
