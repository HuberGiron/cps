# How to Make Almost Cyber-Physical (CPS)

Este repositorio es el sitio del curso (Just-the-Docs) y el espacio de documentación tipo FabAcademy:
cada semana produce un entregable verificable + benchmarks para justificar decisiones de protocolo/arquitectura.

## Publicar en GitHub Pages (rápido)
1. Crea un repo en GitHub y sube estos archivos.
2. En GitHub: Settings → Pages → Build and deployment → Source: `Deploy from a branch`
3. Selecciona rama `main` y carpeta `/ (root)`.
4. Espera a que Pages genere el sitio (Actions te mostrará el estado).

## Correr local (opcional)
Si tienes Ruby/Jekyll instalado:
- `bundle install`
- `bundle exec jekyll serve`

## Estructura
- `weeks/` — Guías semanales (objetivo, pasos, pruebas, checklist, evidencias)
- `stack/` — Arquitectura, contratos de datos, decisiones
- `bench/` — Metodología y resultados de benchmarks (latencia, jitter, pérdida, throughput)
- `infra/` — Docker y despliegue
- `security/` — Auth, permisos, CORS, secrets, reglas Firebase
- `resources/` — Matrices de protocolos y dispositivos (derivadas del Excel)

