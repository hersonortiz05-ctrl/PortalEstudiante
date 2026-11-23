# Tarea 3.1 · Ejercicios SQL

Fecha objetivo: 23/11/2026. Ejecutar consultas_y_restricciones.sql solo sobre base de desarrollo con migraciones aplicadas. No usar la base de producción. No contiene CREATE TABLE: las tablas pertenecen a las migraciones de Herson.

Abrir el archivo en un cliente PostgreSQL o el SQL Editor de un proyecto Supabase de pruebas. Ejecutar primero SELECT y luego las transacciones por separado. La consulta usa los nombres exactos del contrato. Las transacciones usan ROLLBACK y no conservan filas. PostgreSQL puede consumir números de secuencia aunque se revierta la transacción: los saltos de ID son normales.

El bloque de restricciones emite avisos de PK, FK, UNIQUE, NOT NULL y CHECK si cada rechazo esperado ocurre; no se escriben resultados anticipados. Las FK Django pueden ser diferibles y se fuerzan con SET CONSTRAINTS ALL IMMEDIATE dentro del bloque de prueba.

Registrar fecha real, servidor sin URI privada, resultado observado y captura sin credenciales. Si los códigos S1A_SQL_TEMP o S1A_SQL_CHECK ya existen, usar otra base de pruebas o investigar su origen; no borrar registros ajenos para ejecutar el ejercicio.

Fecha real de ejecución: ______
Ejecutor: ______
Resultado observado: ______
Evidencia: ______
