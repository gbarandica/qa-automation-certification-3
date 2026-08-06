# Reto teórico 2 — Performance, seguridad, a11y, mantenimiento y mapa S9–S10

> **Formato:** 14 preguntas de selección única (una correcta, tres incorrectas).  
> **Tiempo sugerido:** 25–30 minutos · **Aprobación sugerida:** 11 de 14 (~79%).  
> **Nivel:** medio.  
> Las respuestas están en `../respuestas/teorico-2.md` (instructor) y en `../RETOS_COMPLETOS.md`.

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
