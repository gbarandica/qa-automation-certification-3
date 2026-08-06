# Retos completos — Certificación 3

> Paquete único para compartir: teórico 1 + respuestas, teórico 2 + respuestas,
> y reto práctico con explicación y URL de GitHub.
>
> **Curso:** Ingeniería de Automatización — APIs, Performance y Seguridad.

---

# Reto teórico 1 — Diseño, scripts, APIs y CI/CD (S1–S5)

> **Formato:** 14 preguntas de selección única (una correcta, tres incorrectas).  
> **Tiempo sugerido:** 25–30 minutos · **Aprobación sugerida:** 11 de 14 (~79%).  
> **Nivel:** medio.  

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

---

# Respuestas — Reto teórico 1 (solo instructor)

| # | Correcta | Justificación breve |
|---|----------|---------------------|
| 1 | **b** | BVA en el límite inferior del rango (0; 10_000]: primer válido 0.01 e inválido 0 (o ≤0). |
| 2 | **b** | Pairwise reduce combinaciones cubriendo pares; no es exhaustivo de N-way. |
| 3 | **b** | Test zombie = TC sin REQ. Hueco = REQ sin TC. |
| 4 | **b** | POM centraliza UI; un cambio de locator se arregla en la page object. |
| 5 | **b** | Screenplay: Actor / Ability / Task; POM se centra en páginas. |
| 6 | **b** | Data-driven: misma lógica, muchos datasets externos. |
| 7 | **b** | 404 = recurso no encontrado; distinto de 5xx o 401. |
| 8 | **b** | Newman corre colecciones Postman en CLI/CI. |
| 9 | **b** | JSON Schema valida estructura del contrato, no solo “hay JSON”. |
| 10 | **b** | Fixture de sesión = setup caro compartido. |
| 11 | **b** | Mínimo privilegio: contents:read. |
| 12 | **b** | Concurrency cancela corridas viejas del mismo ref/grupo. |
| 13 | **b** | Docker espejo de CI = paridad de ambiente. |
| 14 | **b** | Verde = pasó lo configurado; no implica seguridad/a11y total. |

**Aprobación sugerida:** 11 de 14 (~79%).

---

# Reto teórico 2 — Performance, seguridad, a11y, mantenimiento y mapa S9–S10

> **Formato:** 14 preguntas de selección única (una correcta, tres incorrectas).  
> **Tiempo sugerido:** 25–30 minutos · **Aprobación sugerida:** 11 de 14 (~79%).  
> **Nivel:** medio.  

---

**1.** En K6, ¿cuál es la diferencia clave entre un **check** y un **threshold**?

- a) No hay diferencia: son sinónimos
- b) El check registra si una condición se cumplió; el threshold decide si el proceso/job falla (gate)
- c) El threshold solo mide CPU; el check solo mide RAM
- d) Los checks solo existen en JMeter

**2.** Un smoke de K6 en cada PR y un load más pesado en nocturno refleja el mismo criterio de:

- a) Mutation score 100%
- b) Costo/beneficio: barato y frecuente vs. caro y justificado
- c) Ignorar p95
- d) Usar solo Burp Suite

**3.** Para un endpoint con p95 medido en baseline de 180 ms, un threshold razonable en CI suele ser:

- a) p95 < 1 ms siempre
- b) Baseline + buffer (ej. p95 < 250 ms), no un número inventado
- c) Solo el promedio (avg), nunca percentiles
- d) p95 > 5000 ms para “dar margen”

**4.** OWASP ZAP **baseline** (como en el lab) se caracteriza por:

- a) Ataque activo agresivo a producción
- b) Spider corto + reglas pasivas; apto para repetir en PR
- c) Reemplazar por completo un pentest manual
- d) Solo analizar código fuente (SAST)

**5.** En `rules.tsv` de ZAP, poner una alerta en **FAIL** significa:

- a) Se ignora siempre
- b) El hallazgo puede hacer fallar el job (gate de seguridad)
- c) Solo se imprime en consola, nunca afecta el exit code
- d) Convierte ZAP en SAST

**6.** ¿Por qué el curso usa Juice Shop local y no SauceDemo para ZAP?

- a) SauceDemo no tiene HTTPS
- b) Escaneo ético y reproducible: Juice Shop es vulnerable a propósito y es target controlado
- c) ZAP no soporta sitios públicos
- d) Docker no puede abrir localhost

**7.** Según WCAG, el principio **Perceptible** se viola típica y claramente cuando:

- a) El CSS usa demasiado azul
- b) Una imagen informativa no tiene texto alternativo (`alt`)
- c) El servidor responde 200
- d) El test de K6 falla

**8.** Axe en CI automatiza sobre todo:

- a) Auditorías completas con usuarios reales
- b) Regresiones de accesibilidad detectables en el DOM (contraste, alt, lang, etc.)
- c) Performance de red
- d) Firma de contratos Pact

**9.** CrossBrowserTesting fue discontinuado; en el mapa del curso el reemplazo práctico es:

- a) Recheck
- b) LambdaTest (junto con BrowserStack / Sauce Labs)
- c) mutmut
- d) Newman

**10.** Un test “flaky” se caracteriza por:

- a) Fallar siempre por el mismo assert correcto
- b) Pasar o fallar sin cambios en el código, por no-determinismo (tiempo, random, orden, estado)
- c) Tener 100% de cobertura
- d) Usar solo `get_by_role`

**11.** ¿Por qué el lab de mutación usa **cosmic-ray** y no **mutmut**?

- a) mutmut no entiende Python
- b) mutmut 3.x requiere `fork` y no corre nativo en Windows; cosmic-ray sí es multiplataforma
- c) cosmic-ray solo corre en Java
- d) mutmut está prohibido por OWASP

**12.** Mutation score 50% con suite “verde” y alta cobertura demuestra que:

- a) La cobertura garantiza asserts fuertes
- b) Cobertura ≠ calidad: muchos mutantes sobrevivieron porque los asserts son débiles
- c) Hay que borrar todos los tests
- d) El CI está mal configurado necesariamente

**13.** Ante un rediseño que cambia ids/clases pero el botón sigue diciendo “Ingresar”, el selector más robusto es:

- a) `#login-btn`
- b) `.btn-primary:nth-child(3)`
- c) Rol + texto visible (`get_by_role("button", name="Ingresar")`)
- d) Coordenadas x,y absolutas

**14.** En el mapa S9–S10 del plan, Appium/Maestro y la regresión visual encajan en el gate como:

- a) Reemplazo total de las pruebas de API
- b) Capas adicionales (móvil / visual) sobre la misma puerta de calidad de release
- c) Solo documentación Word
- d) Obligación de usar únicamente Healenium en Docker

---

# Respuestas — Reto teórico 2 (solo instructor)

| # | Correcta | Justificación breve |
|---|----------|---------------------|
| 1 | **b** | Check observa; threshold gatea el exit code / job. |
| 2 | **b** | Smoke frecuente y barato; load cuando justifica el costo. |
| 3 | **b** | Threshold = baseline + buffer, no un número mágico. |
| 4 | **b** | Baseline = spider + pasivo; apto para PR. |
| 5 | **b** | FAIL en rules.tsv puede tumbar el job. |
| 6 | **b** | Juice Shop = target ético y local; no escanear terceros. |
| 7 | **b** | Sin alt, la info no es perceptible para lector de pantalla. |
| 8 | **b** | Axe = regresiones WCAG automatizables en DOM. |
| 9 | **b** | CBT discontinuado → LambdaTest (mapa con BrowserStack/Sauce). |
| 10 | **b** | Flaky = resultado inestable sin cambio de código. |
| 11 | **b** | mutmut necesita fork/WSL; cosmic-ray corre en Windows nativo. |
| 12 | **b** | Score bajo con cobertura alta = asserts débiles. |
| 13 | **c** | Rol + nombre visible sobrevive rediseños de id/clase. |
| 14 | **b** | Móvil/visual son etapas más del mismo gate, no reemplazan API. |

**Aprobación sugerida:** 11 de 14 (~79%).

---

# Reto práctico — QA Release Gate (Certificación 3)

> **Modalidad:** individual · **Tiempo sugerido:** 60–90 minutos · **Nivel:** medio.  
> **Evidencia de que funcionó:** `uv run pytest -v` → **14 passed** (el score es automático).  
> **Código en GitHub:** https://github.com/dsolisp/curso/tree/main/retos/reto-practico

## Contexto

Sos QA en el equipo del **QA Release Gate** del curso. Ya tenés métricas de:

- Suite API/UI (pass rate)
- Performance K6 (p95)
- Seguridad ZAP (`FAIL-NEW` vs `WARN-NEW`)
- Mutation testing (mutation score)
- Accesibilidad Axe (violaciones *critical*)

Te piden un módulo Python que, con los umbrales del curso, decida si el release **pasa** o se **bloquea**.

El esqueleto ya existe. Tu trabajo es implementar **6 funciones** marcadas con `TODO` en `src/release_gate.py`. Una suite de pytest valida cada una: cuando todo está bien, los **14 tests** pasan.

## Umbrales

| Chequeo | Umbral | Sesión |
|---------|--------|--------|
| Pass rate | falla si **< 0.95** | S4/S5 |
| p95 (ms) | falla si **> 500** | S6 |
| ZAP FAIL-NEW | falla si **> 0** (WARN no bloquea) | S7 |
| Mutation score | falla si **< 0.90** | S8 |
| Axe critical | falla si **> 0** | S7 |

## Funciones a implementar

1. `pass_rate(passed, total)`
2. `p95_ok(p95_ms, threshold_ms=None)`
3. `zap_gate(fail_new, warn_new=0, fail_limit=None)`
4. `mutation_score(killed, total_mutants)`
5. `a11y_critical_ok(critical_violations)`
6. `release_gate(metrics)` → `{"checks": {...}, "passed": bool}`

Cada función tiene docstring con casos borde. Leelos antes de programar.

## Cómo correrlo

> **Requisito:** `uv` instalado (mismo del curso).

```bash
# Desde esta carpeta (reto-practico/)

uv sync
uv run pytest -v          # al inicio falla: es esperado
# Implementá función por función hasta ver:
# 14 passed
```

Cuando el gate esté listo, también podés verlo decidir:

```bash
uv run python -m src.release_gate
```

Salida esperada (release de ejemplo con mutation score roto: 40/50 = 0.80 < 0.90):

```json
{
  "checks": {
    "pass_rate": true,
    "p95": true,
    "zap": true,
    "mutation": false,
    "a11y": true
  },
  "passed": false
}
```

## Entregable

- [ ] `uv run pytest -v` → **14 passed**
- [ ] `uv run python -m src.release_gate` → JSON con `"passed": false` y solo `mutation` en `false`
- [ ] Explicá en una frase por qué ese release se bloquea

## Reglas

- No modifiques `tests/test_release_gate.py` ni `THRESHOLDS`.
- Sin librerías externas: solo biblioteca estándar.
- Si un test no te pasa, leé el nombre del test y su assert.

### Notas del instructor (práctico)

- Solución de referencia: `retos/respuestas/release_gate_solucion.py`
- Criterio: `uv run pytest -v` → **14 passed**
- El release de ejemplo debe bloquear solo por **mutation** (score 0.80 < 0.90)
- URL del código: https://github.com/dsolisp/curso/tree/main/retos/reto-practico
