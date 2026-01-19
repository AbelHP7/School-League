# ⚽ School League Manager

![Estado](https://img.shields.io/badge/Estado-En_Desarrollo-yellow?style=flat-square)
![Stack](https://img.shields.io/badge/MERN-Stack-blue?style=flat-square)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green?style=flat-square)

> **Proyecto de Fin de Ciclo (DAW)**
> Aplicación web integral para la digitalización y gestión de torneos de fútbol en centros educativos.

---

## 📖 Descripción del Proyecto

**School League Manager** es una solución web diseñada para modernizar la gestión de las ligas deportivas escolares. El objetivo principal es sustituir las actas en papel y las hojas de cálculo manuales por un sistema centralizado que automatice la clasificación y ofrezca información en tiempo real a alumnos y profesores.

El sistema permite a los coordinadores gestionar equipos, horarios y resultados, mientras que la comunidad educativa puede consultar clasificaciones y estadísticas desde cualquier dispositivo móvil.

## ✨ Funcionalidades Principales

### 🔹 Módulo de Administración (Backoffice)
- **Gestión de Usuarios (RBAC):** Sistema de roles (Admin/Profesor y Alumno) con autenticación segura (JWT).
- **Gestión de Equipos:** CRUD completo de equipos, escudos y asignación de jugadores por clase.
- **Planificador de Torneos:** Generación de jornadas, asignación de horarios y pistas.
- **Acta Digital:** Introducción de resultados y validación de partidos finalizados.

### 🔹 Experiencia de Usuario (Pública)
- **Clasificación Automática:** Algoritmo que recalcula la tabla (Puntos > Diferencia de Goles > Goles a favor) instantáneamente tras cada resultado.
- **Perfil de Equipo:** Historial de partidos jugados y por jugar.
- **Diseño Responsive:** Interfaz optimizada para consulta rápida en móviles (Mobile First).

### 🚀 Roadmap (Futuras Mejoras)
- [ ] **Live Score:** Actualización de marcadores en tiempo real vía WebSockets.
- [ ] **Estadísticas Avanzadas:** Rankings de "Pichichi" y "Zamora".
- [ ] **Exportación:** Generación de calendarios y actas en PDF.
- [ ] **Brackets:** Generación visual de cuadros para fases eliminatorias (Play-offs).

## 🛠️ Stack Tecnológico

El proyecto sigue una arquitectura basada en **Componentes** y **API REST**:

| Área | Tecnología | Descripción |
| :--- | :--- | :--- |
| **Frontend** | ![React](https://img.shields.io/badge/-React-61DAFB?logo=react&logoColor=white) | Librería principal para la UI (con Vite). |
| **Estilos** | ![Tailwind](https://img.shields.io/badge/-Tailwind_CSS-38B2AC?logo=tailwind-css&logoColor=white) | Framework CSS utilitario para diseño rápido. |
| **Backend** | ![Node](https://img.shields.io/badge/-Node.js-339933?logo=node.js&logoColor=white) | Entorno de ejecución para la API REST. |
| **Base de Datos** | ![MySQL](https://img.shields.io/badge/-MySQL-4479A1?logo=mysql&logoColor=white) | Base de datos relacional para la integridad de los datos. |
| **Control de Versiones** | ![Git](https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white) | Gestión del código fuente. |

## 📦 Instalación y Despliegue Local

Sigue estos pasos para levantar el proyecto en tu máquina local:

### Prerrequisitos
- Node.js (v16 o superior)
- MySQL Server

### Pasos
1. **Clonar el repositorio**
   ```bash
   git clone [https://github.com/TU-USUARIO/school-league-manager.git](https://github.com/TU-USUARIO/school-league-manager.git)
   cd school-league-manager
