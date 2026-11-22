# Portal de Estudiantes

Proyecto integrador del curso IIT4013 Desarrollo de Aplicaciones Web, Universidad José Cecilio del Valle (III período 2026). Grupo 1.

## Descripción del sistema

Aplicación web que centraliza la información académica del estudiante: perfil, materias matriculadas, calificaciones y avisos. Un administrador mantiene actualizados los registros académicos. El sistema usa datos de prueba y no se conecta con sistemas institucionales.

## Problema que busca resolver

Cuando la información académica está dispersa, es más difícil para los estudiantes dar seguimiento a sus materias, notas y avisos. El portal permite consultarla en un mismo lugar.

## Objetivo general

Desarrollar un portal web responsive con Django y PostgreSQL en Supabase para consultar información estudiantil y administrar cursos, matrículas, calificaciones y avisos, con control de acceso por roles, historial de colaboración en GitHub y publicación en Render.

## Tecnologías utilizadas

- Python 3.13 y Django
- PostgreSQL en Supabase
- HTML5, CSS3 y JavaScript
- Git y GitHub
- Render (despliegue)

## Estado actual del proyecto

En desarrollo. Está creada la estructura base del proyecto Django con sus aplicaciones. La base de datos en Supabase, los modelos y las pantallas están en construcción.

## Integrantes

- Herson
- Robert
- Paola
- Amaris
- Antonid

## Estructura del proyecto

- `config/`: configuración de Django.
- `apps/usuarios/`: autenticación, roles y perfil.
- `apps/academico/`: carreras, períodos, cursos, matrículas y calificaciones.
- `apps/avisos/`: avisos académicos.
- `apps/principal/`: panel principal y navegación.
- `templates/`, `static/`, `media/`: plantillas, estilos y archivos.
- `tests/`: pruebas.

## Cómo ejecutar el proyecto

1. Clonar el repositorio y entrar a la carpeta:

   ```
   git clone https://github.com/hersonortiz05-ctrl/PortalEstudiante.git
   cd PortalEstudiante
   ```

2. Crear y activar el entorno virtual (Windows):

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instalar las dependencias:

   ```
   pip install -r requirements.txt
   ```

4. Crear el archivo `.env` a partir del ejemplo y completar sus valores:

   ```
   copy .env.example .env
   ```

   `SECRET_KEY` se genera con `python -c "import secrets; print(secrets.token_urlsafe(50))"`. Si `DATABASE_URL` queda vacío, se usa SQLite local. La cadena de conexión a Supabase la entrega el responsable del repositorio y no se sube a GitHub.

5. Iniciar el servidor y abrir http://127.0.0.1:8000:

   ```
   python manage.py runserver
   ```

## Enlaces

- Repositorio: https://github.com/hersonortiz05-ctrl/PortalEstudiante
- Aplicación publicada: pendiente de despliegue