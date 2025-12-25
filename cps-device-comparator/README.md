# Comparador de dispositivos (CPS)

Este mini‑sitio es una herramienta didáctica para **explorar** y **comparar** dispositivos por categoría (Computadora/Procesador, Embebido, PLC), protocolos y capacidades de I/O.

## Estructura

- `index.html` — Sitio (single-page) con vistas **Explorar** y **Comparar**.
- `assets/css/styles.css` — Estilos responsivos (sin frameworks).
- `assets/js/app.js` — Lógica (vanilla JS).
- `data/devices.json` — Base de datos local (se carga con `fetch`).
- `data/devices.csv` — Alternativa editable en tabla.
- `tools/csv_to_json.py` — Convierte CSV → JSON (regenera IDs/rutas).
- `assets/img/*.svg` — Imágenes placeholder por dispositivo (reemplázalas por fotos reales si quieres).
- `datasheets/*.pdf` — PDFs placeholder por dispositivo (reemplázalos por hojas de datos reales).

## Cómo correrlo

### Opción A — Simple (servidor local)
Por seguridad del navegador, `fetch("data/devices.json")` necesita servidor. Dos opciones rápidas:

**Python (recomendado):**
```bash
cd cps-device-comparator
python -m http.server 8000
```
Luego abre: `http://localhost:8000`

**VS Code Live Server:** abrir carpeta y “Go Live”.

### Opción B — GitHub Pages
1. Sube todo el contenido del proyecto a un repo.
2. Activa Pages (Settings → Pages → Deploy from branch).
3. Accede a tu URL.

## Cómo agregar o editar dispositivos (recomendación práctica)

### Camino 1: Editar `data/devices.csv` (más cómodo)
1. Abre `data/devices.csv` en Excel/Sheets.
2. Agrega/edita filas.
3. Regenera JSON:
```bash
python tools/csv_to_json.py
```

### Camino 2: Editar `data/devices.json` directo
Edita el arreglo `devices`. Cada objeto usa:
- `id` (único)
- `model`, `category`, `frequency`, `ram`, `storage`, `protocols`, `io`
- `image` (ruta dentro del repo)
- `datasheet` (ruta dentro del repo)

## Reemplazar imágenes y hojas de datos

- Imágenes: reemplaza `assets/img/<id>.svg` por `assets/img/<id>.jpg` (o `.png`) y actualiza el campo `image` en CSV/JSON.
- PDFs: reemplaza `datasheets/<id>.pdf` por el PDF real (mismo nombre) y la liga ya funcionará.

## Sugerencia arquitectónica: JSON vs Firebase

Dado que mencionas que habrá **pocas modificaciones** tras cargar el dataset inicial, **JSON local** es la opción más eficiente:

- Muy simple (cero backend, cero autenticación).
- Se despliega perfecto en GitHub Pages.
- Offline-friendly / portable.
- Control de versiones natural (Git).

Usa **Firebase (Firestore + Storage + Hosting)** solo si:
- Necesitas que varias personas editen en web sin tocar el repo,
- quieres un panel de administración (CRUD) con login,
- esperas crecimiento continuo del dataset y trazabilidad (quién cambió qué),
- quieres analítica y control de acceso.

Si te interesa, se puede extender este proyecto con:
- Firestore como fuente de datos,
- Storage para PDFs/imágenes,
- reglas de seguridad y Auth para un “admin”.

## Licencia
Uso educativo.
