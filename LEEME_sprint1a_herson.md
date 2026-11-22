# Sprint 1a · Herson

Modelos, restricciones, datos demo y base de integración.

Base revisada: repositorio hersonortiz05-ctrl/PortalEstudiante, main, commit 9493481206bafee27cb1d53f07a64374f6d99d36. Fecha objetivo del paquete: 23/11/2026. El código y los documentos fueron preparados por Codex; deben ser revisados y comprendidos por el integrante antes de presentar trabajo propio.

Orden obligatorio: Herson → Antonid → Amaris → Paola → Robert. Cada paquete se integra por PR a develop antes de que la siguiente persona actualice su copia. No extraer los cinco ZIP a la vez sobre una rama personal. Nunca aplicar estos ZIP al portal anterior con apps accounts/academics/notices.

## Archivos y propósito

- `.env.example`: Enumera variables a completar en privado; no contiene credenciales.
- `apps/academico/admin.py`: Registra los modelos para su gestión en Django Admin.
- `apps/academico/management/__init__.py`: Permite a Python reconocer este paquete.
- `apps/academico/management/commands/__init__.py`: Permite a Python reconocer este paquete.
- `apps/academico/management/commands/cargar_datos_demo.py`: Carga datos ficticios con contraseña desde el entorno.
- `apps/academico/models.py`: Define tablas, relaciones y restricciones del contrato.
- `apps/academico/tests.py`: Prueba integridad de los modelos y los conteos de datos demo.
- `apps/academico/urls.py`: Conecta rutas públicas con las vistas de la app.
- `apps/avisos/admin.py`: Registra los modelos para su gestión en Django Admin.
- `apps/avisos/models.py`: Define tablas, relaciones y restricciones del contrato.
- `apps/avisos/urls.py`: Conecta rutas públicas con las vistas de la app.
- `apps/principal/templates/principal/dashboard.html`: Plantilla HTML; define la pantalla sin implementar lógica de base de datos.
- `apps/principal/urls.py`: Conecta rutas públicas con las vistas de la app.
- `apps/principal/views.py`: Procesa solicitudes y entrega datos a las pantallas.
- `apps/usuarios/urls.py`: Conecta rutas públicas con las vistas de la app.
- `config/settings.py`: Conserva configuración del repo, exige PostgreSQL y define clases de mensajes.
- `config/urls.py`: Incluye las rutas de las cuatro apps.

## Preparación y accesos

Cada persona usa su propia cuenta GitHub y acepta la invitación del propietario. La cuenta GitHub y la cuenta de estudiante del portal son distintas. No compartir contraseñas, tokens ni .env.

El ZIP no es un proyecto completo independiente: se extrae en la raíz de un clon del repositorio oficial. Si el repositorio cambió desde el commit indicado, comparar los archivos antes de reemplazar. git status debe estar limpio; si hay trabajo pendiente, guardarlo y coordinar antes de extraer.

Necesitás Python 3.13, Git y un entorno virtual activado. Usar PostgreSQL de desarrollo con permiso CREATEDB para las pruebas. La suite crea y elimina una base test_…; no ejecutarla contra Supabase productivo. Instalar dependencias con `python -m pip install -r requirements.txt`.

Copiar .env.example a .env solo si aún no existe; completar SECRET_KEY, DATABASE_URL, DEBUG y DEMO_PASSWORD en un editor privado. Para Supabase usar Session pooler con TLS; para PostgreSQL local indicar DATABASE_SSL_REQUIRE=False. No mandar capturas del archivo.

## Crear develop una sola vez

Al revisar el remoto solo existía main. Primero comprobar si Herson u otro integrante ya creó develop. Si no existe, Herson ejecuta en CMD:

```bat
cd "RUTA_DEL_REPO"
git fetch origin
git checkout main
git pull --ff-only origin main
git status
git checkout -b develop
git push -u origin develop
```

El propietario debe invitar a sus compañeros y definir develop como destino de sus PR. No se creó ni publicó esa rama desde Codex.

## Comandos en CMD · computadora y cuenta propias

Ejecutar por bloques y detenerse si un comando falla. Cambiar RUTA_DEL_REPO. Guardar el ZIP recibido en Descargas.

```bat
cd "RUTA_DEL_REPO"
git fetch origin
git checkout develop
git pull origin develop
git status
git checkout -b feature/S1A-H-modelos
powershell -Command "Expand-Archive -Path '%USERPROFILE%\Downloads\sprint1a_herson.zip' -DestinationPath . -Force"
git status
python manage.py check
python manage.py makemigrations academico avisos
python manage.py migrate
python manage.py cargar_datos_demo
python manage.py makemigrations --check --dry-run
python manage.py test apps.academico.tests
```

Revisar cambios y después preparar el commit con rutas explícitas:

```bat
git diff
git add ".env.example"
git add "apps/academico/admin.py"
git add "apps/academico/management/__init__.py"
git add "apps/academico/management/commands/__init__.py"
git add "apps/academico/management/commands/cargar_datos_demo.py"
git add "apps/academico/models.py"
git add "apps/academico/tests.py"
git add "apps/academico/urls.py"
git add "apps/avisos/admin.py"
git add "apps/avisos/models.py"
git add "apps/avisos/urls.py"
git add "apps/principal/templates/principal/dashboard.html"
git add "apps/principal/urls.py"
git add "apps/principal/views.py"
git add "apps/usuarios/urls.py"
git add "config/settings.py"
git add "config/urls.py"
git add "LEEME_sprint1a_herson.md"
git add "apps/academico/migrations" "apps/avisos/migrations"
git diff --cached
git commit -m "S1A-H: modelos, restricciones, datos demo y base de integración"
git push -u origin feature/S1A-H-modelos
```

## Cómo probar y qué está disponible

Con Herson solo se verifican configuración, modelos, migraciones y carga de datos. Las rutas provisionales vacías aún no tienen login. Después de Antonid: /login/ y /. Después de Amaris: CRUD de /gestion/carreras/, /gestion/periodos/ y /gestion/cursos/. /admin/ está disponible con demo.admin y contraseña privada DEMO_PASSWORD.

En una base inicialmente vacía deben existir 1 administrador, 3 estudiantes, 2 carreras, 2 períodos, 4 cursos, 6 matrículas, 4 calificaciones y 4 avisos. Repetir cargar_datos_demo no debe duplicar datos. No vaciar una base ajena para obtener esos conteos.

Las migraciones NO están en el ZIP. Generarlas solo Herson, revisarlas y commitearlas en su PR; los compañeros ejecutan migrate, no regeneran las iniciales. Las migraciones utilizadas por Codex para verificar permanecen en una copia aislada y no se entregan.

## Pull Request hacia develop

Título propuesto: S1A-H: modelos, restricciones, datos demo y base de integración.

Descripción para completar tras trabajar:

- Alcance del paquete y revisión personal realizada: ______
- Archivos modificados respecto del material asistido: ______
- Pruebas realmente ejecutadas y resultado: ______
- Evidencias y limitaciones: ______
- Revisor solicitado: Amaris.

No copiar resultados de Codex como si fueran propios. No usar --author ni la cuenta de otro integrante.

## Preguntas para la defensa

1. ¿Por qué Estudiante vive en academico y no en usuarios?
2. ¿Qué diferencia hay entre validación del formulario y CHECK de PostgreSQL?
3. ¿Qué impide duplicar una matrícula y borrar su curso?
4. ¿Por qué las migraciones se generan una sola vez y se comparten en Git?

## Peticiones y dependencias

PETICIÓN A ANTONID: reemplazar únicamente apps/usuarios/urls.py provisional. PETICIÓN A AMARIS: reemplazar apps/academico/urls.py provisional. Mantener apps/avisos/urls.py vacío hasta 1b. PETICIÓN AL EQUIPO: no editar settings, models, migraciones ni apps/principal. No ejecutar este ZIP nuevamente después de integrar otros: restauraría URLs provisionales.

## Registro individual (dejar en blanco hasta ejecutarlo)

Fecha real: ______  ·  Tiempo real: ______  ·  Actividad propia: ______  ·  Prueba/resultado: ______  ·  Commit/PR propio: ______  ·  Evidencia: ______
