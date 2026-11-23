# Portal de Estudiantes · Análisis de la Entrega 1

Grupo 1 · IIT4013 · Universidad José Cecilio del Valle. Integrantes: Herson, Amaris, Antonid, Paola y Robert. Fecha objetivo de Entrega 1: 03/12/2026. Este borrador fue preparado con asistencia de Codex; el equipo debe revisarlo y completar evidencias reales.

## Problema y objetivos

La información académica dispersa dificulta consultar matrículas, calificaciones y avisos. Objetivo general: centralizar consultas estudiantiles y gestión administrativa en una aplicación Django con PostgreSQL Supabase, código versionado en GitHub y despliegue Render.

Objetivos específicos: autenticar por roles, limitar registros por estudiante, organizar matrículas por período, validar notas y duplicados, publicar comunicaciones generales o por curso, ofrecer una interfaz responsive y demostrar integridad mediante pruebas.

## Alcance

Incluye perfiles, contacto, cursos matriculados, notas, avisos, dashboard y CRUD administrativo. No incluye pagos, matrícula autoservicio, recuperación de contraseña por correo ni integración automática con sistemas oficiales de la universidad. Los datos son ficticios.

## Requisitos funcionales

RF01 login/logout POST; RF02 roles Administrador/Estudiante y rechazo 403 a autenticados sin permiso; RF03 perfil propio y edición solo teléfono/dirección; RF04 materias con búsqueda y período; RF05 detalle de matrícula propia; RF06 notas propias; RF07 avisos publicados/vigentes generales o de cursos matriculados; RF08 dashboard; RF09 CRUD siete entidades; RF10 validación de formularios y eliminación protegida.

## Requisitos no funcionales

RNF01 Django/Python, HTML5/CSS3 y JS mínimo; RNF02 PostgreSQL Supabase sin fallback SQLite; RNF03 secretos fuera del repositorio; RNF04 CSRF y escape HTML; RNF05 responsive 360/768/1366; RNF06 separación apps/forms/views/templates; RNF07 Git con commits personales reales y PR hacia develop; RNF08 Render con HTTPS/estáticos; RNF09 pruebas reproducibles; RNF10 accesibilidad básica y mensajes comprensibles.

## Criterios de aceptación

El estudiante no puede obtener datos ajenos cambiando un ID; únicamente administración cambia datos académicos. No se admiten matrículas duplicadas ni notas fuera de 0–100. Se protege el borrado de entidades relacionadas. Las contraseñas nunca se guardan en texto plano. Un aviso de curso solo llega a estudiantes matriculados; uno vencido o borrador no se muestra.

## Estado por paquete

Sprint 1a entrega modelos, datos, acceso, permisos, dashboard base, CRUD de tres catálogos, estilo y documentación. Perfil editable, CRUD de estudiantes/matrículas/notas/avisos, consultas completas y despliegue se completan en 1b/2 según contrato. No afirmar que una función futura está implementada. Conexión Supabase y URL Render deben verificarse en sus cuentas.
