# ⚽ Torneo de Fútbol del Instituto

**Proyecto Final de Trimestre - DAW**

## 📋 Descripción
Aplicación web para gestionar un torneo de fútbol del instituto organizado por clases, con sistema de grupos por horarios (mañana/tarde) y fase eliminatoria.

## 🛠️ Stack Tecnológico
- **Backend:** PHP 8.2 + Symfony 7.4 LTS
- **Base de Datos:** MySQL 8.0
- **Frontend:** Twig + CSS + JavaScript
- **Servidor Web:** Nginx
- **Containerización:** Docker + Docker Compose

## 🏆 Estructura del Torneo

### Fase de Grupos
- **Grupos Horario Mañana:** Solo juegan entre equipos de mañana
- **Grupos Horario Tarde:** Solo juegan entre equipos de tarde
- **Clasificación:** Los 2 mejores de cada grupo pasan a eliminatorias

### Fase Eliminatoria
- Los equipos clasificados (mañana y tarde) se pueden enfrentar
- Formato: Cuartos de Final → Semifinales → Final

## 👥 Roles de Usuario
- **Admin:** Control total del sistema (gestión de equipos, partidos, usuarios)
- **Árbitros:** Registro y actualización de resultados de partidos
- **Usuarios:** Consulta de información, clasificaciones y calendario

## 📦 Estructura del Proyecto
```
torneo-futbol/
├── docker/                 # Configuración Docker
├── src/                    # Código fuente Symfony
├── config/                 # Configuración de Symfony
├── templates/              # Plantillas Twig
├── public/                 # Archivos públicos
├── migrations/             # Migraciones de BD
└── docker-compose.yml      # Orquestación de contenedores
```

## 🚀 Instalación y Despliegue

### Requisitos
- Docker Desktop
- Git

### Pasos
1. Clonar el repositorio
2. Ejecutar `docker-compose up -d`
3. Acceder a `http://localhost:8080`

## 📝 Funcionalidades Principales
- ✅ Gestión de equipos (clases)
- ✅ Creación y gestión de grupos por horario
- ✅ Calendario de partidos
- ✅ Registro de resultados
- ✅ Clasificaciones automáticas
- ✅ Generación automática de eliminatorias
- ✅ Sistema de autenticación por roles
- ✅ Panel de administración

## 👨‍💻 Autor
Abel Hernández Porcel - DAW

## 📅 Fecha
Trimestre 2 - 2026
