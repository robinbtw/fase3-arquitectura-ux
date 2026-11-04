# Fase 3 — PoC de Arquitectura de Software y UX

## Relación con la Fase 2
La Fase 2 propone estudiar la relación entre decisiones arquitectónicas, consistencia visual y experiencia de usuario. Esta PoC implementa una interfaz web con dos variantes visuales: estilos dispersos (legacy) y estilos centralizados (centralized). Incluye un endpoint HTTP local y herramientas para medir latencia.

## Requisitos
Python 3 instalado. No requiere paquetes externos.

## Ejecutar
1. Descomprimir el proyecto.
2. Abrir una terminal en esta carpeta.
3. Ejecutar `python server.py`.
4. Abrir `http://127.0.0.1:8000/?mode=legacy` y `http://127.0.0.1:8000/?mode=centralized`.

## Medición empírica local
Con el servidor activo, abrir otra terminal en la misma carpeta y ejecutar:
`python benchmark.py`
Genera `resultados/benchmark_real.csv` y `resultados/resumen_real.json` con mediciones HTTP de este equipo.
Después ejecutar `python analisis.py` para obtener `resultados/analisis_real.json`.

La prueba automatizada realiza 30 solicitudes al endpoint por cada modo. Como ambos modos comparten el mismo backend, no se debe interpretar la latencia como evidencia de una mejora arquitectónica del servidor. La comparación principal de esta PoC es visual; la latencia es una comprobación del endpoint y del proceso de medición.

## Datos sintéticos de demostración
`python generar_sinteticos.py` crea `resultados/datos_sinteticos_demo.csv`. Este archivo es SINTÉTICO y sirve únicamente para verificar el procesamiento de datos. No debe presentarse como observación de usuarios ni como medición real.

## LCP y experiencia subjetiva
El navegador puede exportar LCP mediante el botón de la interfaz. Para medir LCP de forma comparable, repetir las cargas en el mismo navegador, equipo y condiciones. El cuestionario SUS (10 ítems), confianza visual y tiempo de reconocimiento requieren participantes reales; esta PoC no fabrica respuestas.

## Límites
- No es una arquitectura de microfrontends distribuida; es una PoC local de centralización de estilos CSS.
- Latencia de endpoint local no equivale a LCP.
- Error de solicitudes no equivale a crash rate de sesiones.
- Los resultados son exploratorios y no permiten generalización sin un diseño experimental más amplio.
- No declarar cumplimiento de umbrales sin mediciones correspondientes.

## Estructura
- `server.py`: servidor y endpoint.
- `static/`: interfaz y estilos.
- `benchmark.py`: medición HTTP local real.
- `analisis.py`: resumen de los datos reales.
- `generar_sinteticos.py`: dataset sintético identificado.
- `docs/ADR-01.md`: decisión arquitectónica.
- `docs/protocolo.md`: protocolo y límites.
- `resultados/`: carpeta para CSV/JSON generados.
