---
title: 04 — Web básica: HTML, CSS y JavaScript para dashboards
parent: Semana 01 — Fundamentos CPS + Benchmarks + Web + Just-the-Docs
nav_order: 4
---

# Web básica: HTML, CSS y JavaScript para dashboards

MDN es una referencia recomendada para fundamentos web. citeturn2search3turn2search20

## Entregable
Crear `web-demo/` con:
- `index.html`
- `style.css`
- `app.js`

## Código base
### index.html
```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>CPS Dashboard (Semana 1)</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header>
    <h1>CPS Dashboard (Semana 1)</h1>
    <p>Telemetría simulada (placeholder)</p>
  </header>

  <main class="grid">
    <section class="card"><h2>Latencia p95 (ms)</h2><div id="lat95" class="big">—</div></section>
    <section class="card"><h2>Pérdida (%)</h2><div id="loss" class="big">—</div></section>
    <section class="card"><h2>Throughput (Mbps)</h2><div id="thr" class="big">—</div></section>
    <section class="card"><h2>Estado</h2><div id="status" class="big ok">OK</div></section>
  </main>

  <footer><small>Curso CPS — Semana 1</small></footer>
  <script src="app.js"></script>
</body>
</html>
```

### style.css
```css
:root { font-family: system-ui, Arial, sans-serif; }
body { margin: 0; padding: 24px; background: #f6f7fb; }
header { margin-bottom: 16px; }
.grid { display: grid; gap: 12px; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }
.card { background: #fff; border-radius: 12px; padding: 14px; box-shadow: 0 2px 12px rgba(0,0,0,.06); }
.big { font-size: 36px; font-weight: 700; }
.ok { color: #0b6; }
.bad { color: #c00; }
```

### app.js
```js
function rand(min, max) { return (Math.random() * (max - min) + min); }

function tick() {
  const lat95 = rand(5, 120);
  const loss = rand(0, 3);
  const thr = rand(0.1, 2.5);

  document.getElementById("lat95").textContent = lat95.toFixed(1);
  document.getElementById("loss").textContent = loss.toFixed(2);
  document.getElementById("thr").textContent = thr.toFixed(3);

  const status = document.getElementById("status");
  const bad = (loss > 1.0) || (lat95 > 100.0);
  status.textContent = bad ? "DEGRADADO" : "OK";
  status.className = "big " + (bad ? "bad" : "ok");
}

setInterval(tick, 1000);
tick();
```
