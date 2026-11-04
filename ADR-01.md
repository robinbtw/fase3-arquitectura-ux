# ADR-01: Centralización de estilos y componentes visuales

- **Estado:** Implementada como PoC académica local.
- **Contexto:** La Fase 2 plantea que diferencias de colores, tipografías, formas y estados entre secciones pueden afectar la previsibilidad y la carga cognitiva.
- **Decisión:** Construir dos variantes de una misma interfaz: estilos dispersos (legacy) y reglas centralizadas mediante variables y reglas CSS compartidas (centralized).
- **Consecuencias esperadas:** La centralización facilita mantener patrones visuales coherentes. La mejora en percepción y satisfacción debe comprobarse con usuarios.
- **Limitaciones:** No se implementan microfrontends reales ni un Design System distribuido. La PoC representa el principio de centralización en una aplicación pequeña.
