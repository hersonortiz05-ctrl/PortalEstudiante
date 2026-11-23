# Sprint 1a · Paola

Sistema visual compartido, login y dashboard.

Base revisada: repositorio hersonortiz05-ctrl/PortalEstudiante, main, commit 9493481206bafee27cb1d53f07a64374f6d99d36. Fecha objetivo del paquete: 23/11/2026. El código y los documentos fueron preparados por Codex; deben ser revisados y comprendidos por el integrante antes de presentar trabajo propio.

Orden obligatorio: Herson → Antonid → Amaris → Paola → Robert. Cada paquete se integra por PR a develop antes de que la siguiente persona actualice su copia. No extraer los cinco ZIP a la vez sobre una rama personal. Nunca aplicar estos ZIP al portal anterior con apps accounts/academics/notices.

## Archivos y propósito

- `docs/paola/sprint1a/etiquetas_django.md`: Documento de guía o plantilla; completar evidencias solo con trabajo real.
- `docs/paola/sprint1a/guia_estilos.md`: Documento de guía o plantilla; completar evidencias solo con trabajo real.
- `static/css/styles.css`: Define las clases CSS compartidas y adaptación responsive.
- `templates/base.html`: Plantilla HTML; define la pantalla sin implementar lógica de base de datos.
- `templates/principal/dashboard.html`: Plantilla HTML; define la pantalla sin implementar lógica de base de datos.
- `templates/usuarios/login.html`: Plantilla HTML; define la pantalla sin implementar lógica de base de datos.

## Preparación y accesos

Cada persona usa su propia cuenta GitHub y acepta la invitación del propietario. La cuenta GitHub y la cuenta de estudiante del portal son distintas. No compartir contraseñas, tokens ni .env.

El ZIP no es un proyecto completo independiente: se extrae en la raíz de un clon del repositorio oficial. Si el repositorio cambió desde el commit indicado, comparar los archivos antes de reemplazar. git status debe estar limpio; si hay trabajo pendiente, guardarlo y coordinar antes de extraer.

## GitHub Desktop · sin comandos

1. Iniciar sesión con tu propia cuenta y aceptar la invitación. File > Clone repository > seleccionar PortalEstudiante y una carpeta local.
2. Current branch > develop. Pulsar Fetch origin y Pull origin si aparece. Si no existe develop, avisar a Herson.
3. Comprobar que Changes está vacío. Si no, detenerse y revisar con Herson; no descartar trabajo.
4. Current branch > New branch > escribir `feature/S1A-P-interfaz`. Crear desde develop.
5. En Descargas, clic derecho sobre `sprint1a_paola.zip` > Extraer todo. Abrir la carpeta extraída y copiar SU CONTENIDO en la raíz del repositorio, donde está manage.py. No copiar la carpeta exterior entera. Aceptar reemplazos solo de los archivos listados arriba y si la base coincide.
6. Volver a GitHub Desktop. En Changes, marcar únicamente los archivos propios listados en esta guía y el LEEME. Si aparece .env u otro archivo privado, no marcarlo y avisar.
7. Summary: `S1A-P: sistema visual compartido, login y dashboard`. Description: explicar qué revisaste/cambiaste realmente. Pulsar Commit to la rama.
8. Publish branch (o Push origin si ya fue publicada). Luego Create pull request.
9. En GitHub seleccionar base develop y compare feature/S1A-P-interfaz. Agregar descripción y pedir revisión a Amaris. No elegir main.
10. Esperar revisión e integración antes de actualizar develop para otra tarea. No integrar PR ajenos por cuenta propia.

## Cómo probar y qué está disponible

Pedir a Herson/Antonid que arranque el portal y facilite cuentas ficticias. Abrir /login/ y /; revisar estudiante con materias, Sofía sin matrículas y administrador. Probar tamaños 360, 768 y 1366 con ayuda del navegador. Comprobar foco con Tab, labels, contraste y mensajes de error. No se requiere ejecutar Python ni modificar backend.

Máximo orientativo: 3–4 horas por semana. Priorizar revisión y comprensión de las tres plantillas y styles.css. Las plantillas de perfil/gestión/avisos corresponden a 1b. No hay enlaces a rutas todavía inexistentes.

## Pull Request hacia develop

Título propuesto: S1A-P: sistema visual compartido, login y dashboard.

Descripción para completar tras trabajar:

- Alcance del paquete y revisión personal realizada: ______
- Archivos modificados respecto del material asistido: ______
- Pruebas realmente ejecutadas y resultado: ______
- Evidencias y limitaciones: ______
- Revisor solicitado: Amaris.

No copiar resultados de Codex como si fueran propios. No usar --author ni la cuenta de otro integrante.

## Preguntas para la defensa

1. ¿Qué hacen Flexbox y Grid en estas pantallas?
2. ¿Cómo funciona extends y el bloque content?
3. ¿Para qué sirven labels, foco visible y csrf_token?
4. ¿Cómo revisás que una tabla se adapte al móvil?

## Peticiones y dependencias

PETICIÓN A HERSON: mantener MESSAGE_TAGS de su paquete. PETICIÓN A ANTONID: mantener filtros roles y rutas login/logout. PETICIÓN A AMARIS: integrar rutas de catálogos antes del menú. No se pide a Paola editar archivos Python.

## Registro individual (dejar en blanco hasta ejecutarlo)

Fecha real: ______  ·  Tiempo real: ______  ·  Actividad propia: ______  ·  Prueba/resultado: ______  ·  Commit/PR propio: ______  ·  Evidencia: ______
