-- EJEMPLOS para base de desarrollo con migraciones y datos ficticios.
-- Sin contraseñas ni conexiones. Ejecutar como propietario de las tablas.
-- Cada transacción termina en ROLLBACK para no conservar cambios.

-- SELECT: matrícula y nota; LEFT JOIN conserva matrículas sin calificación.
SELECT e.codigo, u.username, c.codigo AS curso, p.nombre AS periodo, n.nota
FROM academico_matricula m
JOIN academico_estudiante e ON e.id = m.estudiante_id
JOIN auth_user u ON u.id = e.user_id
JOIN academico_curso c ON c.id = m.curso_id
JOIN academico_periodo p ON p.id = m.periodo_id
LEFT JOIN academico_calificacion n ON n.matricula_id = m.id
ORDER BY e.codigo, c.codigo;

-- SELECT: avisos generales publicados y vigentes.
SELECT titulo FROM avisos_aviso
WHERE publicado = TRUE AND curso_id IS NULL
AND fecha_publicacion <= CURRENT_TIMESTAMP
AND (fecha_fin IS NULL OR fecha_fin >= CURRENT_TIMESTAMP);

-- INSERT, SELECT, UPDATE y DELETE de un curso temporal sin dependencias.
BEGIN;
INSERT INTO academico_curso (codigo, nombre, descripcion)
VALUES ('S1A_SQL_TEMP', 'Curso ficticio SQL', 'Ejercicio temporal');
SELECT codigo, nombre FROM academico_curso WHERE codigo = 'S1A_SQL_TEMP';
UPDATE academico_curso SET nombre = 'Curso SQL editado' WHERE codigo = 'S1A_SQL_TEMP';
SELECT codigo, nombre FROM academico_curso WHERE codigo = 'S1A_SQL_TEMP';
DELETE FROM academico_curso WHERE codigo = 'S1A_SQL_TEMP';
SELECT COUNT(*) AS restantes FROM academico_curso WHERE codigo = 'S1A_SQL_TEMP';
ROLLBACK;

-- Pruebas que capturan errores esperados sin dejar abortada la transacción.
BEGIN;
DO $$
DECLARE curso_id bigint;
BEGIN
  INSERT INTO academico_curso (codigo, nombre, descripcion)
  VALUES ('S1A_SQL_CHECK', 'Prueba de restricciones', '') RETURNING id INTO curso_id;
  BEGIN
    INSERT INTO academico_curso (id, codigo, nombre, descripcion)
    VALUES (curso_id, 'S1A_SQL_OTRO', 'PK duplicada', '');
    RAISE EXCEPTION 'FALLO: PK permitió duplicado';
  EXCEPTION WHEN unique_violation THEN RAISE NOTICE 'PK: duplicado rechazado'; END;
  BEGIN
    INSERT INTO academico_curso (codigo, nombre, descripcion)
    VALUES ('S1A_SQL_CHECK', 'Código repetido', '');
    RAISE EXCEPTION 'FALLO: UNIQUE permitió duplicado';
  EXCEPTION WHEN unique_violation THEN RAISE NOTICE 'UNIQUE: código repetido rechazado'; END;
  BEGIN
    INSERT INTO academico_curso (codigo, nombre, descripcion)
    VALUES ('S1A_SQL_NULL', NULL, '');
    RAISE EXCEPTION 'FALLO: NOT NULL permitió NULL';
  EXCEPTION WHEN not_null_violation THEN RAISE NOTICE 'NOT NULL: nombre nulo rechazado'; END;
  BEGIN
    INSERT INTO academico_periodo (nombre, fecha_inicio, fecha_fin)
    VALUES ('S1A_SQL_FALLA', DATE '2026-12-01', DATE '2026-01-01');
    RAISE EXCEPTION 'FALLO: CHECK permitió fechas inválidas';
  EXCEPTION WHEN check_violation THEN RAISE NOTICE 'CHECK: fechas inválidas rechazadas'; END;
  BEGIN
    -- Django crea FK diferibles: forzar evaluación dentro del bloque.
    INSERT INTO academico_matricula (estudiante_id, curso_id, periodo_id, fecha_registro)
    VALUES (-999999, curso_id, -999999, CURRENT_TIMESTAMP);
    SET CONSTRAINTS ALL IMMEDIATE;
    RAISE EXCEPTION 'FALLO: FK permitió relación inexistente';
  EXCEPTION WHEN foreign_key_violation THEN RAISE NOTICE 'FK: relación inexistente rechazada'; END;
END $$;
ROLLBACK;
