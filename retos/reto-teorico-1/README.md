# Reto teórico 1 — Diseño, scripts, APIs y CI/CD (S1–S5)

> **Formato:** 14 preguntas de selección única (una correcta, tres incorrectas).  
> **Tiempo sugerido:** 25–30 minutos · **Aprobación sugerida:** 11 de 14 (~79%).  
> **Nivel:** medio.  
> Las respuestas están en `../respuestas/teorico-1.md` (instructor) y en `../RETOS_COMPLETOS.md`.

---

**1.** Un campo acepta montos de (0; 10_000]. Según BVA, ¿cuál conjunto es el más adecuado para el límite inferior?

- a) 0, 1 y 5000
- b) 0.01 (primer válido) y 0 (inválido)
- c) Solo valores aleatorios dentro del rango
- d) −1, 0 y 0.01 sin justificar el rango

**2.** Pairwise testing se usa principalmente porque:

- a) Garantiza cobertura de todas las combinaciones de N factores
- b) La mayoría de defectos vienen de interacciones de a lo sumo 2 parámetros, y reduce el número de casos
- c) Reemplaza por completo las tablas de decisión
- d) Solo aplica a pruebas de performance

**3.** En la matriz de trazabilidad del curso, un “test zombie” es:

- a) Un test que falla siempre
- b) Un TC sin REQ asociado (no se sabe qué prueba ni por qué existe)
- c) Un REQ sin ningún TC
- d) Un defecto sin severidad

**4.** ¿Cuál es la ventaja principal del Page Object Model (POM)?

- a) Hace que los tests corran más rápido en CI
- b) Centraliza selectores y acciones de UI para que un cambio de pantalla se arregle en un solo lugar
- c) Elimina la necesidad de asserts
- d) Reemplaza a pytest

**5.** Screenplay se diferencia de POM en que:

- a) No usa el navegador
- b) Modela actores, habilidades y tareas (quién hace qué) en lugar de solo “páginas”
- c) Solo funciona con Java
- d) Prohíbe el uso de datos externos

**6.** Separar datos de prueba en JSON/YAML (data-driven) aporta sobre todo:

- a) Menos cobertura de código
- b) Reutilizar la misma lógica de test con muchos insumos sin duplicar código
- c) Que los tests no necesiten asserts
- d) Que Newman deje de ser necesario

**7.** En REST, un cliente recibe `404` al hacer GET de un recurso. La interpretación correcta es:

- a) El servidor siempre está caído
- b) El recurso no existe (o no es visible) en esa URL; no es lo mismo que un error 500
- c) La autenticación falló siempre
- d) El body es inválido según JSON Schema

**8.** Newman en el curso se usa para:

- a) Reemplazar GitHub Actions
- b) Ejecutar colecciones Postman desde CLI/CI de forma automatizable
- c) Escanear seguridad OWASP
- d) Medir p95 de latencia

**9.** Un contrato JSON Schema en las pruebas de API sirve para:

- a) Sustituir todos los asserts de status code
- b) Validar la forma/estructura del payload (tipos, campos requeridos), no solo “que haya JSON”
- c) Generar el frontend automáticamente
- d) Configurar Docker Compose

**10.** En pytest, una fixture con scope de sesión se usa típicamente para:

- a) Ejecutar un assert una sola vez
- b) Compartir un recurso costoso (cliente HTTP, datos) entre muchos tests sin recrearlo cada vez
- c) Marcar tests como xfail
- d) Desactivar el plugin de Playwright

**11.** En GitHub Actions, `permissions: contents: read` en un workflow de QA suele indicar:

- a) Que el job puede borrar el repositorio
- b) Principio de mínimo privilegio: el job solo necesita leer el código
- c) Que no se pueden usar secrets
- d) Que el workflow solo corre en Windows

**12.** `concurrency` con `cancel-in-progress: true` en un workflow sirve para:

- a) Paralelizar todos los jobs del mundo
- b) Cancelar corridas viejas del mismo grupo cuando llega un push/PR nuevo (evitar colas inútiles)
- c) Forzar mutación testing
- d) Ignorar fallos de pytest

**13.** Correr la misma suite de API dentro de Docker (`ci-lab`) y en GitHub Actions aporta:

- a) Que no haga falta escribir tests
- b) Paridad: “en mi máquina” ≈ “en CI”, reduciendo sorpresas de ambiente
- c) Solo mejora la cobertura de mutación
- d) Reemplaza K6

**14.** Un PR verde en CI significa, en el marco de este curso:

- a) Que la app es 100% segura y accesible
- b) Que los chequeos configurados del gate (lint/tests/etc.) pasaron — no que no existan riesgos fuera de esos chequeos
- c) Que ya se puede omitir code review
- d) Que el mutation score es necesariamente 100%
