# Fase 3: Ejecución, recolección de datos y construcción de artefactos

## 1. Construcción de la prueba de concepto
Se preparó una aplicación web local para comparar dos variantes de interfaz: una con estilos visuales dispersos y otra con reglas de presentación centralizadas. La aplicación contiene un panel de acciones y un endpoint HTTP que devuelve una respuesta controlada. La finalidad es demostrar el flujo de interacción y la posibilidad de recopilar métricas técnicas relacionadas con la experiencia de usuario.

## 2. Configuración y ejecución
La aplicación se ejecuta mediante Python, sin dependencias externas. Se inicia con `python server.py` y se accede desde el navegador en `http://127.0.0.1:8000`. Los modos se consultan mediante `?mode=legacy` y `?mode=centralized`.

## 3. Recolección de datos
El proyecto incorpora `benchmark.py`, que ejecuta solicitudes HTTP al endpoint local en ambos modos y registra fecha, iteración, latencia, estado y código HTTP. El archivo `analisis.py` calcula cantidad de solicitudes, latencia media, P95 y porcentaje de errores a partir del CSV generado. La interfaz también permite exportar observaciones de LCP y latencias de interacción desde el navegador.

**Completar después de ejecutar:** número de solicitudes realizadas, resultados obtenidos y condiciones del equipo/navegador.

## 4. Almacenamiento y disponibilidad
El código fuente, el protocolo y los artefactos de medición se organizan en un repositorio GitHub público. Incorporar aquí la URL real del repositorio una vez creado. Los datos deben subirse después de ejecutar las pruebas.

**Repositorio:** [PEGAR URL REAL DE GITHUB]

## 5. Evidencias y estado de ejecución
Incluir capturas de: aplicación en modo legacy, aplicación en modo centralized, terminal con benchmark ejecutado, archivos CSV/JSON generados y repositorio GitHub. Identificar navegador, sistema operativo y fecha de ejecución.

## 6. Limitaciones
La PoC representa la centralización de estilos en una aplicación local y no implementa microfrontends distribuidos. Las mediciones HTTP corresponden al endpoint local y no equivalen a LCP ni a crash rate de sesiones. Las métricas subjetivas SUS y confianza visual requieren participantes reales y no se estiman sin aplicar los instrumentos.

## 7. Conclusión
La PoC permite demostrar la ejecución de una interfaz con dos variantes visuales y establecer un procedimiento reproducible para recopilar métricas técnicas. Las conclusiones cuantitativas deberán redactarse a partir de los resultados obtenidos en la ejecución, evitando atribuir mejoras que no hayan sido observadas.
