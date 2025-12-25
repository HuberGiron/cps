---
title: 01 — Introducción a Sistemas Ciberfísicos (CPS)
parent: Semana 01 — Fundamentos CPS + Benchmarks + Web + Just-the-Docs
nav_order: 1
---

# Introducción a Sistemas Ciberfísicos (CPS)

**Meta del documento:** que puedas describir CPS con precisión, distinguirlo de IoT, y aterrizarlo a un proyecto concreto.

---

## Metadatos (estilo tutorial)
- Autor(es): (Equipo ___)
- Curso/Lab: Sistemas Ciberfísicos
- Licencia: CC BY 4.0 (si aplica)
- Última revisión: (fecha)

---

## Resumen
Un **Cyber-Physical System (CPS)** es la **integración de cómputo con procesos físicos**, típicamente con bucles de retroalimentación donde lo físico afecta el cómputo y viceversa. citeturn2search4

En la literatura docente clásica se menciona que el término “cyber-physical systems” fue acuñado por **Helen Gill (2006)**. citeturn2search1

---

## ¿Qué incluye un CPS?
Checklist de componentes (mínimo):
- **Planta física** (fenómeno real: motor, temperatura, posición, flujo, etc.)
- **Sensores/actuadores**
- **Computación embebida** (MCU, SBC, edge)
- **Comunicación** (buses, red, mensajería)
- **Control/decisión** (lógica, control, IA/LLM con políticas)
- **Humano en el lazo** (UI, HMI, seguridad operativa)

---

## CPS vs IoT (diferencia práctica)
**IoT** se suele definir (NIST) como dispositivos de usuario o industriales conectados a Internet (incluye sensores, controladores, electrodomésticos). citeturn2search2

Diferencia operativa para el curso:
- **IoT**: énfasis en conectividad + captura/uso de datos (muchas veces “monitoring”).
- **CPS**: énfasis en **dinámica + control + seguridad + tiempo real**; el sistema “vive” en el acoplamiento entre lo físico y lo computacional. citeturn2search4

**Regla rápida:**
- Si la latencia/jitter/pérdida **cambian el comportamiento físico** (y tu diseño lo contempla), estás en terreno CPS.

---

## Actividad (obligatoria)
1. Elige un sistema real (ejemplos):
   - robot móvil / brazo,
   - HVAC de edificio,
   - celda de manufactura con PLC + HMI,
   - monitoreo + control de bomba/valvulería.
2. Escribe 10–15 líneas:
   - ¿Por qué es CPS y no solo IoT?
   - ¿Cuál es la variable física crítica?
   - ¿Qué pasa si latencia p95 sube a 200 ms?
3. Dibuja 1 diagrama simple:
   - sensores/actuadores → cómputo → red → UI.

---

## Evidencia / entregable
- 1 página en Just-the-Docs con:
  - definición (con fuentes),
  - CPS vs IoT,
  - tu sistema elegido,
  - diagrama embebido (imagen o diagrama textual).

---

## Referencias mínimas
- Ptolemy/UC Berkeley — definición CPS. citeturn2search4
- Lee & Seshia — origen del término (Helen Gill, 2006). citeturn2search1
- NIST CSRC — definición IoT. citeturn2search2
