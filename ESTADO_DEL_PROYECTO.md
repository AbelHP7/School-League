# Objetivos del Proyecto
**Nombre:** Abel Hernández Porcel

## A. Funcionalidades Mínimas (MVP - Core del Proyecto)
Estas funcionalidades constituyen la base del sistema y garantizan el aprobado del proyecto.

**Sistema de Autenticación y Autorización (RBAC):**
*   **Login seguro:** Implementación de tokens (JWT) y encriptación de contraseñas robusta (PBKDF2 de Django, estándar actual para máxima seguridad).
*   **Roles diferenciados:**
    *   Admin/Profesor: Acceso total al panel de control (CRUD completo).
    *   Usuario/Alumno: Acceso de lectura, perfil propio y capacidad de ver detalles de su equipo.
    *   Árbitro (Opcional): Rol específico con permisos limitados solo a la edición de actas de partido.

**Gestión Integral de Equipos y Jugadores:**
*   **CRUD Avanzado:** Alta, baja y modificación de equipos con validaciones (ej. máximo de jugadores por equipo, evitar duplicados).
*   **Fichas Técnicas:** Subida de imágenes (escudos de equipo) y vinculación de jugadores a sus cursos/clases correspondientes.
*   **Historial:** Visualización de la plantilla actual y sus dorsales.

**Gestión de Competición y Calendario:**
*   **Generador de Jornadas:** Herramienta para crear enfrentamientos, asignando fecha, hora y pista/campo de juego. *(Implementado con un potente motor de generación automatizada sin conflictos)*.
*   **Estados del Partido:** Control de estados lógicos: "Programado", "En Juego", "Finalizado" o "Suspendido".
*   **Algoritmo Formato "Sistema Suizo/Champions":** Programación de un algoritmo de asignación compleja de partidos usando transacciones en base de datos.

**Gestión de Resultados y Actas:**
*   **Input de Marcador:** Formulario protegido para introducir goles locales y visitantes.
*   **Validación de Acta:** Cierre del partido para evitar modificaciones posteriores no autorizadas una vez validado el resultado.

**Motor de Clasificación Automatizado:**
*   **Algoritmo de Ordenación:** La tabla se recalcula instantáneamente tras cada resultado, ordenando por: 1º Puntos, 2º Diferencia de Goles, 3º Goles a Favor.
*   **Indicadores Visuales:** Colores en la tabla para indicar zonas de clasificación (ej. zona de Play-off en verde, zona de eliminación en rojo, implementado de forma dinámica adaptándose al nº de equipos).

---

## Logros Técnicos Extra (Implementados fuera del MVP)
*   **Refactorización Completa del Diseño con Tailwind CSS:** Transición exitosa a un framework profesional "Utility-First", creando interfaces modernas adaptables (Mobile-First) y componentes estéticos (Glassmorphism).
*   **Arquitectura Profesional (Separación Backend/Frontend):** Reestructuración de todo el proyecto para separar de forma estricta las plantillas visuales de la lógica de negocio, siguiendo buenas prácticas empresariales.
*   **Panel de Administración Extendido (Jazzmin):** Integración de un panel de control avanzado que facilita a los profesores la gestión de datos masivos.

---

## B. Features Extra Opcionales (Mejoras para fases posteriores)

**Módulo de Tiempo Real (Live Score):**
*   Uso de WebSockets (Socket.io) para que, cuando el árbitro anote un gol en su dispositivo, el marcador se actualice automáticamente en las pantallas de todos los usuarios conectados sin necesidad de recargar la página.

**Centro de Estadísticas Avanzadas (Data Visualization):**
*   **Rankings:** Tablas automáticas de "Pichichi" (goleadores), "Zamora" (porteros) y "Fair Play" (tarjetas).
*   **Gráficos:** visualizar la racha de los equipos (ej. Ganado-Empatado-Perdido en los últimos 5 partidos).

**Documentación y Exportación:**
*   **Generación de PDF/Excel:** Botón para que los profesores descarguen el calendario completo o las actas de los partidos para imprimirlas.
*   **Códigos QR:** Generación automática de un QR por equipo para que los alumnos lo escaneen y vayan directos a su ficha.

**Gestión de Fase Final (Play-offs):**
*   **Generador de Brackets:** Algoritmo que toma a los clasificados de la fase regular y genera visualmente el cuadro de semifinales y final automáticamente.

**Notificaciones y Social:**
*   **Avisos:** Notificaciones vía email o internas en la web cuando se publica un horario nuevo o se modifica un partido.
*   **MVP del Partido:** Posibilidad de que el árbitro vote al "Mejor Jugador del Partido" y quede registrado en el perfil del alumno.

---

## ✅ COMPLETADO para enseñar
*(Para que tengas claro qué partes de la lista anterior ya están 100% funcionando en tu código actual)*

1.  **Todo el Sistema de Autenticación y Autorización (RBAC)** (Logins, Encriptación y Roles de Admin/Alumno/Árbitro).
2.  **Toda la Gestión Integral de Equipos y Jugadores** (Admin CRUD, Subida de Escudos, Plantillas y Dorsales).
3.  **Toda la Gestión de Competición y Calendario** (Generador Automático de 8 Jornadas sin conflictos, Estados de Partidos y el nuevo Sistema Suizo/Champions).
4.  **Toda la Gestión de Resultados y Actas** (Validación de Resultados por el Árbitro y Cierre de Actas).
5.  **Todo el Motor de Clasificación Automatizado** (Cálculo automático de puntos, victorias y diferencia de goles con visualización por colores (Champions/Descenso)).



