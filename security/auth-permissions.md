---
title: Permisos, auth, CORS y secrets
nav_order: 1
parent: Seguridad
---

# Permisos entre servidores y APIs

## Objetivo
Evitar que cualquier cliente:
- envíe comandos a actuadores,
- inyecte eventos falsos,
- lea datos sensibles.

## Nivel mínimo recomendado (curso)
1. **API Token** para endpoints de control (`/command`).
2. **Roles** (viewer / operator):
   - viewer: solo lectura
   - operator: comandos
3. **CORS** restringido a tu dominio de dashboard (cuando aplique).
4. **Secrets** por entorno:
   - local: `.env` (no se sube)
   - nube: variables del proveedor (Render/VPS)

## Service-to-service
- Gateway local → API nube: token dedicado
- UI → API nube: token de usuario/rol

## Firebase (Semana 12)
- Usar reglas (Firestore Rules) para limitar lectura/escritura por usuario/rol.
- Documentar:
  - estructura de colecciones
  - reglas
  - ejemplo de acceso permitido y denegado

> En el curso, el criterio de aceptación es: demostrar un request permitido y otro bloqueado.
