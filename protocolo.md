# Protocolo de ejecución y recolección de datos

## Objetivo
Ejecutar una PoC que permita observar dos variantes visuales y comprobar la recolección de métricas técnicas.

## Procedimiento reproducible
1. Iniciar `python server.py`.
2. Abrir los dos modos en el mismo navegador y equipo.
3. Realizar las mismas interacciones en cada modo.
4. Exportar las mediciones del navegador en JSON.
5. Ejecutar `python benchmark.py` en otra terminal para medir 30 solicitudes por modo al endpoint local.
6. Ejecutar `python analisis.py` para resumir exclusivamente las mediciones reales del benchmark.
7. Conservar CSV, JSON y capturas junto al código.

## Métricas
- LCP: tiempo hasta el mayor elemento de contenido visible; se registra desde el navegador.
- Latencia HTTP: duración observada al solicitar el endpoint local.
- P95: percentil 95 de las latencias observadas.
- Errores HTTP: solicitudes fallidas divididas para solicitudes intentadas.

## Tabla de resultados
Completar con los archivos generados:
| Modo | Solicitudes | Latencia media (ms) | P95 (ms) | Errores (%) |
|---|---:|---:|---:|---:|
| Sin Design System | — | — | — | — |
| Con Design System | — | — | — | — |

## Evidencia subjetiva
SUS, confianza visual y tiempo de reconocimiento requieren participantes reales. No se incluyen respuestas inventadas.

## Interpretación y límites
Ambos modos utilizan el mismo endpoint y backend, por lo que no se espera que el estilo CSS modifique sustancialmente la latencia HTTP. La PoC sirve para probar la interfaz y el proceso de medición, no para afirmar causalidad entre microfrontends y UX.
