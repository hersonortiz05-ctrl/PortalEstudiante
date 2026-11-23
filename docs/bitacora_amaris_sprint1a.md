# Bitácora de Amaris · Sprint 1a

Fecha del trabajo: 22/11/2026, America/Tegucigalpa.

## Actividad realizada

Se revisó el repositorio oficial PortalEstudiante, la rama local `dev/amaris`, el paquete `sprint1a_amaris.zip` y su LEEME. La rama se actualizó localmente hasta el estado actual de `develop`, que incluye la integración previa de Herson. Después se extrajo el ZIP mediante el comando `Expand-Archive` indicado en el LEEME.

El paquete aporta el CRUD administrativo de carreras, períodos y cursos; formularios; búsqueda; paginación; borrado protegido; plantillas reutilizables; análisis de Entrega 1; modelo/diccionario; mapa de navegación; y ejercicios SQL documentados para Tarea 3.1.

## Archivos creados por el paquete

- `LEEME_sprint1a_amaris.md`
- `apps/academico/forms.py`
- `apps/academico/gestion.py`
- `apps/academico/test_catalogos.py`
- `apps/academico/templates/gestion/base.html`
- `apps/academico/templates/gestion/lista.html`
- `apps/academico/templates/gestion/form.html`
- `apps/academico/templates/gestion/confirmar_eliminar.html`
- `docs/entrega_1/analisis_requisitos.md`
- `docs/entrega_1/modelo_diccionario.md`
- `docs/entrega_1/navegacion.md`
- `docs/tarea_3_1/LEEME.md`
- `docs/tarea_3_1/consultas_y_restricciones.sql`

## Archivos modificados por el paquete

- `apps/academico/urls.py`
- `apps/academico/views.py`

## Verificación realizada

- Se inspeccionaron los modelos y migraciones existentes de Herson, sin modificarlos.
- Se comprobó estáticamente que `config/urls.py` ya incluye `apps.academico.urls` y que las rutas del paquete coinciden con los nombres usados por las vistas y plantillas.
- Se revisó el diff para confirmar que no contiene migraciones, configuración de base de datos, modelos, archivos de compañeros ni secretos.
- Se analizó la sintaxis de los cinco archivos Python de Amaris con el parser de Python 3.13 y se ejecutó `git diff --check`; no se detectaron errores de sintaxis ni espacios en blanco inválidos.
- No se ejecutaron `makemigrations`, `migrate`, `cargar_datos_demo` ni `python manage.py test`, conforme a la instrucción del proyecto.

## Resultado obtenido

Los archivos del paquete de Amaris quedaron aplicados únicamente en la copia local de `dev/amaris`, sin commits ni push.

## Evidencia que Amaris debe capturar

- `git branch --show-current` mostrando `dev/amaris`.
- `git status` antes y después de preparar el commit, sin `.env` ni archivos de otros integrantes.
- La lista de cambios de la rama o Pull Request mostrando solo archivos de Amaris.
- Cuando Antonid esté integrado: las vistas `/gestion/carreras/`, `/gestion/periodos/` y `/gestion/cursos/`; un formulario inválido; una búsqueda; y el mensaje al intentar eliminar un curso relacionado.
- Ejecución de los SQL únicamente sobre la base de desarrollo, sin URI ni credenciales visibles.

## Pendientes y dependencia detectada

El archivo `apps/academico/gestion.py` depende de `apps.usuarios.permisos.SoloAdministradorMixin`. Ese archivo no existe todavía en `develop` ni en la rama remota actual de Antonid. Esta bitácora no declara el CRUD ejecutable ni aprobado. Herson debe integrar primero el paquete de Antonid en `develop`; entonces Amaris debe actualizar `dev/amaris`, revisar el conflicto si aparece y realizar las verificaciones permitidas.

También están pendientes las pruebas manuales de interfaz y la ejecución real de Tarea 3.1. No se generaron evidencias ni resultados de esas actividades.
