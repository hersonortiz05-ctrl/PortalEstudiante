# Sprint 1a · Antonid

Autenticación, grupos, permisos y pruebas de acceso.

Base revisada: repositorio hersonortiz05-ctrl/PortalEstudiante, main, commit 9493481206bafee27cb1d53f07a64374f6d99d36. Fecha objetivo del paquete: 23/11/2026. El código y los documentos fueron preparados por Codex; deben ser revisados y comprendidos por el integrante antes de presentar trabajo propio.

Orden obligatorio: Herson → Antonid → Amaris → Paola → Robert. Cada paquete se integra por PR a develop antes de que la siguiente persona actualice su copia. No extraer los cinco ZIP a la vez sobre una rama personal. Nunca aplicar estos ZIP al portal anterior con apps accounts/academics/notices.

## Archivos y propósito

- `apps/usuarios/forms.py`: Valida la entrada en formularios de Django.
- `apps/usuarios/management/__init__.py`: Permite a Python reconocer este paquete.
- `apps/usuarios/management/commands/__init__.py`: Permite a Python reconocer este paquete.
- `apps/usuarios/management/commands/crear_grupos.py`: Prepara grupos y permisos sin asignarlos a cuentas ajenas.
- `apps/usuarios/permisos.py`: Comprueba roles antes de permitir acceso a una vista.
- `apps/usuarios/templates/usuarios/login.html`: Plantilla HTML; define la pantalla sin implementar lógica de base de datos.
- `apps/usuarios/templatetags/__init__.py`: Permite a Python reconocer este paquete.
- `apps/usuarios/templatetags/roles.py`: Permite consultar los roles desde las plantillas.
- `apps/usuarios/tests.py`: Prueba acceso por roles, sesión, CSRF y redirecciones seguras.
- `apps/usuarios/urls.py`: Conecta rutas públicas con las vistas de la app.
- `apps/usuarios/views.py`: Procesa solicitudes y entrega datos a las pantallas.

## Preparación y accesos

Cada persona usa su propia cuenta GitHub y acepta la invitación del propietario. La cuenta GitHub y la cuenta de estudiante del portal son distintas. No compartir contraseñas, tokens ni .env.

El ZIP no es un proyecto completo independiente: se extrae en la raíz de un clon del repositorio oficial. Si el repositorio cambió desde el commit indicado, comparar los archivos antes de reemplazar. git status debe estar limpio; si hay trabajo pendiente, guardarlo y coordinar antes de extraer.

Necesitás Python 3.13, Git y un entorno virtual activado. Usar PostgreSQL de desarrollo con permiso CREATEDB para las pruebas. La suite crea y elimina una base test_…; no ejecutarla contra Supabase productivo. Instalar dependencias con `python -m pip install -r requirements.txt`.

Copiar .env.example a .env solo si aún no existe; completar SECRET_KEY, DATABASE_URL, DEBUG y DEMO_PASSWORD en un editor privado. Para Supabase usar Session pooler con TLS; para PostgreSQL local indicar DATABASE_SSL_REQUIRE=False. No mandar capturas del archivo.

## Comandos en CMD · computadora y cuenta propias

Ejecutar por bloques y detenerse si un comando falla. Cambiar RUTA_DEL_REPO. Guardar el ZIP recibido en Descargas.

```bat
cd "RUTA_DEL_REPO"
git fetch origin
git checkout develop
git pull origin develop
git status
git checkout -b feature/S1A-A-acceso
powershell -Command "Expand-Archive -Path '%USERPROFILE%\Downloads\sprint1a_antonid.zip' -DestinationPath . -Force"
git status
python manage.py check
python manage.py migrate
python manage.py crear_grupos
python manage.py test apps.usuarios
```

Revisar cambios y después preparar el commit con rutas explícitas:

```bat
git diff
git add "apps/usuarios/forms.py"
git add "apps/usuarios/management/__init__.py"
git add "apps/usuarios/management/commands/__init__.py"
git add "apps/usuarios/management/commands/crear_grupos.py"
git add "apps/usuarios/permisos.py"
git add "apps/usuarios/templates/usuarios/login.html"
git add "apps/usuarios/templatetags/__init__.py"
git add "apps/usuarios/templatetags/roles.py"
git add "apps/usuarios/tests.py"
git add "apps/usuarios/urls.py"
git add "apps/usuarios/views.py"
git add "LEEME_sprint1a_antonid.md"
git diff --cached
git commit -m "S1A-A: autenticación, grupos, permisos y pruebas de acceso"
git push -u origin feature/S1A-A-acceso
```

## Cómo probar y qué está disponible

Ejecutar `python manage.py runserver`, abrir /login/, probar demo.ana con clave válida/incorrecta, logout y acceso privado posterior. Las claves están en DEMO_PASSWORD de cada entorno. Un autenticado sin rol obtiene 403; un anónimo es redirigido a login; un estudiante autenticado recibe 403 en vistas administrativas protegidas.

crear_grupos crea permisos de modelos para Administrador y ninguno global para Estudiante; no añade cuentas a grupos. Para Django Admin, además del grupo Administrador, hace falta is_staff. El CRUD propio usa el grupo, no is_staff como atajo. Perfil y edición de estudiantes son del Sprint 1b.

## Pull Request hacia develop

Título propuesto: S1A-A: autenticación, grupos, permisos y pruebas de acceso.

Descripción para completar tras trabajar:

- Alcance del paquete y revisión personal realizada: ______
- Archivos modificados respecto del material asistido: ______
- Pruebas realmente ejecutadas y resultado: ______
- Evidencias y limitaciones: ______
- Revisor solicitado: Herson.

No copiar resultados de Codex como si fueran propios. No usar --author ni la cuenta de otro integrante.

## Preguntas para la defensa

1. ¿Qué diferencia hay entre iniciar sesión y tener permiso?
2. ¿Por qué ocultar botones no protege los datos?
3. ¿Por qué logout usa POST con CSRF?
4. ¿Qué sucede con una cuenta sin grupo o con ambos grupos?

## Peticiones y dependencias

PETICIÓN A HERSON: integrar primero sus modelos/configuración y migraciones. Ya incluye apps.usuarios.urls. PETICIÓN A PAOLA: mantener csrf_token en ambos formularios POST; cargar roles para mostrar menú. No se requieren cambios nuevos en archivos compartidos.

## Registro individual (dejar en blanco hasta ejecutarlo)

Fecha real: ______  ·  Tiempo real: ______  ·  Actividad propia: ______  ·  Prueba/resultado: ______  ·  Commit/PR propio: ______  ·  Evidencia: ______
