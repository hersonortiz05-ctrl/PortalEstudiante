# Sprint 1a · Amaris

CRUD de catálogos, análisis y ejercicios SQL.

Base revisada: repositorio hersonortiz05-ctrl/PortalEstudiante, main, commit 9493481206bafee27cb1d53f07a64374f6d99d36. Fecha objetivo del paquete: 23/11/2026. El código y los documentos fueron preparados por Codex; deben ser revisados y comprendidos por el integrante antes de presentar trabajo propio.

Orden obligatorio: Herson → Antonid → Amaris → Paola → Robert. Cada paquete se integra por PR a develop antes de que la siguiente persona actualice su copia. No extraer los cinco ZIP a la vez sobre una rama personal. Nunca aplicar estos ZIP al portal anterior con apps accounts/academics/notices.

## Archivos y propósito

- `apps/academico/forms.py`: Valida la entrada en formularios de Django.
- `apps/academico/gestion.py`: Comparte listas, formularios y borrado protegido entre entidades.
- `apps/academico/templates/gestion/base.html`: Plantilla HTML; define la pantalla sin implementar lógica de base de datos.
- `apps/academico/templates/gestion/confirmar_eliminar.html`: Plantilla HTML; define la pantalla sin implementar lógica de base de datos.
- `apps/academico/templates/gestion/form.html`: Plantilla HTML; define la pantalla sin implementar lógica de base de datos.
- `apps/academico/templates/gestion/lista.html`: Plantilla HTML; define la pantalla sin implementar lógica de base de datos.
- `apps/academico/test_catalogos.py`: Prueba el CRUD de los tres catálogos y sus validaciones.
- `apps/academico/urls.py`: Conecta rutas públicas con las vistas de la app.
- `apps/academico/views.py`: Procesa solicitudes y entrega datos a las pantallas.
- `docs/entrega_1/analisis_requisitos.md`: Documento de guía o plantilla; completar evidencias solo con trabajo real.
- `docs/entrega_1/modelo_diccionario.md`: Documento de guía o plantilla; completar evidencias solo con trabajo real.
- `docs/entrega_1/navegacion.md`: Documento de guía o plantilla; completar evidencias solo con trabajo real.
- `docs/tarea_3_1/LEEME.md`: Documento de guía o plantilla; completar evidencias solo con trabajo real.
- `docs/tarea_3_1/consultas_y_restricciones.sql`: Ejercicios SQL transaccionales de consulta y restricciones, sin credenciales.

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
git checkout -b feature/S1A-A-catalogos
powershell -Command "Expand-Archive -Path '%USERPROFILE%\Downloads\sprint1a_amaris.zip' -DestinationPath . -Force"
git status
python manage.py check
python manage.py migrate
python manage.py test apps.academico
```

Revisar cambios y después preparar el commit con rutas explícitas:

```bat
git diff
git add "apps/academico/forms.py"
git add "apps/academico/gestion.py"
git add "apps/academico/templates/gestion/base.html"
git add "apps/academico/templates/gestion/confirmar_eliminar.html"
git add "apps/academico/templates/gestion/form.html"
git add "apps/academico/templates/gestion/lista.html"
git add "apps/academico/test_catalogos.py"
git add "apps/academico/urls.py"
git add "apps/academico/views.py"
git add "docs/entrega_1/analisis_requisitos.md"
git add "docs/entrega_1/modelo_diccionario.md"
git add "docs/entrega_1/navegacion.md"
git add "docs/tarea_3_1/LEEME.md"
git add "docs/tarea_3_1/consultas_y_restricciones.sql"
git add "LEEME_sprint1a_amaris.md"
git diff --cached
git commit -m "S1A-A: crud de catálogos, análisis y ejercicios sql"
git push -u origin feature/S1A-A-catalogos
```

## Cómo probar y qué está disponible

Ejecutar `python manage.py runserver`. Como demo.admin visitar /gestion/carreras/, /gestion/periodos/, /gestion/cursos/. Crear registro ficticio sin dependencias, editar y eliminar; probar código duplicado y fecha final anterior. Como demo.ana visitar la misma URL: debe devolver 403.

Probar búsqueda y paginación; intentar eliminar un curso matriculado debe conservarlo y mostrar mensaje comprensible. Los SQL se ejecutan solo en desarrollo siguiendo docs/tarea_3_1/LEEME.md. No se incluyen modelos ni migraciones en este paquete.

Las plantillas de respaldo en apps/academico/templates/gestion permiten trabajar sin esperar a Paola. Usan sus clases CSS, no crean estilos propios. En 1b Paola podrá aportar templates/gestion/* con prioridad de carga, sin sobrescribir archivos de Amaris.

## Pull Request hacia develop

Título propuesto: S1A-A: crud de catálogos, análisis y ejercicios sql.

Descripción para completar tras trabajar:

- Alcance del paquete y revisión personal realizada: ______
- Archivos modificados respecto del material asistido: ______
- Pruebas realmente ejecutadas y resultado: ______
- Evidencias y limitaciones: ______
- Revisor solicitado: Herson.

No copiar resultados de Codex como si fueran propios. No usar --author ni la cuenta de otro integrante.

## Preguntas para la defensa

1. ¿Cómo se reutilizan las vistas y plantillas del CRUD?
2. ¿Qué pasa cuando un curso tiene matrículas y se intenta eliminar?
3. ¿Dónde se validan duplicados y fechas?
4. ¿Por qué los ejercicios SQL terminan en ROLLBACK?

## Peticiones y dependencias

PETICIÓN A HERSON: integrar modelos, migraciones y include de apps.academico.urls. PETICIÓN A ANTONID: integrar permisos antes de este paquete. PETICIÓN A PAOLA: conservar las clases comunes y en 1b aportar plantillas definitivas en templates/gestion. No se requieren cambios del esquema para este paquete.

## Registro individual (dejar en blanco hasta ejecutarlo)

Fecha real: ______  ·  Tiempo real: ______  ·  Actividad propia: ______  ·  Prueba/resultado: ______  ·  Commit/PR propio: ______  ·  Evidencia: ______
