-- Lucio Eduardo Santiago Moreno - S5A - 25/02/2025
-- No de control: 23270042
-- Practica06-Rubricas

DROP DATABASE IF EXISTS dbTaller_23270042;

CREATE DATABASE dbTaller_23270042;

USE dbTaller_23270042;

CREATE TABLE lineaInvestigacion (
    clave_linea VARCHAR(7) PRIMARY KEY
);

CREATE TABLE tipoProyecto (
    id_tipo INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(2) NOT NULL
);

CREATE TABLE revisor (
    id_revisor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(220) NOT NULL
);

CREATE TABLE profesor (
    id_profesor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(220) NOT NULL
);

CREATE TABLE asesor (
    id_asesor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(220) NOT NULL
);

CREATE TABLE institucion (
    id_institucion INT AUTO_INCREMENT PRIMARY KEY,
    nombre_institucion VARCHAR(255) NOT NULL,
    UNIQUE (nombre_institucion)
);

CREATE TABLE proyecto (
    clave_proyecto CHAR(100) PRIMARY KEY,
    nombre VARCHAR(220) NOT NULL,
    lineainvestigacion_clave_linea VARCHAR(7),
    tipoproyecto_id_tipo INT,
    profesor_id_profesor INT,
    asesor_id_asesor INT,
    institucion_id_institucion INT,
    FOREIGN KEY (lineainvestigacion_clave_linea) REFERENCES lineaInvestigacion(clave_linea),
    FOREIGN KEY (tipoproyecto_id_tipo) REFERENCES tipoProyecto(id_tipo),
    FOREIGN KEY (profesor_id_profesor) REFERENCES profesor(id_profesor),
    FOREIGN KEY (asesor_id_asesor) REFERENCES asesor(id_asesor),
    FOREIGN KEY (institucion_id_institucion) REFERENCES institucion(id_institucion)
);

CREATE TABLE rubrica (
    id_rubrica INT PRIMARY KEY AUTO_INCREMENT,
    materia VARCHAR(255) NOT NULL,
    proyecto_clave_proyecto CHAR(100) UNIQUE,  -- Un proyecto solo puede tener una rúbrica
    FOREIGN KEY (proyecto_clave_proyecto) REFERENCES proyecto(clave_proyecto)
);

CREATE TABLE indicador (
    id_indicador INT PRIMARY KEY AUTO_INCREMENT,
    rubrica_id INT,  -- Relación con la rúbrica
    numero INT NOT NULL,  -- Número único del indicador
    descripcion VARCHAR(255),
    FOREIGN KEY (rubrica_id) REFERENCES rubrica(id_rubrica)
);

CREATE TABLE descripcion_indicador (
    id_descripcion INT PRIMARY KEY AUTO_INCREMENT,
    indicador_id INT,  -- Relación con el indicador
    descripcion VARCHAR(255) NOT NULL,
    ponderacion DECIMAL(5,2) NOT NULL,  -- Ponderación de la descripción
    FOREIGN KEY (indicador_id) REFERENCES indicador(id_indicador)
);

CREATE TABLE evaluacion_indicador (
    id_evaluacion INT PRIMARY KEY AUTO_INCREMENT,
    indicador_id INT,  -- Relación con el indicador
    evaluacion VARCHAR(255) NOT NULL,  -- Evaluación única para cada indicador
    FOREIGN KEY (indicador_id) REFERENCES indicador(id_indicador)
);

CREATE TABLE alumno (
    num_control CHAR(10) PRIMARY KEY,
    nombre VARCHAR(220) NOT NULL,
    proyecto_clave_proyecto CHAR(7),
    FOREIGN KEY (proyecto_clave_proyecto) REFERENCES proyecto(clave_proyecto)
);

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(220) NOT NULL,
    perfil ENUM('alumno', 'profesor', 'administrativo') NOT NULL,
    permisos TEXT,
    num_control CHAR(10),
    profesor_id INT,
    FOREIGN KEY (num_control) REFERENCES alumno(num_control),
    FOREIGN KEY (profesor_id) REFERENCES profesor(id_profesor)
);

CREATE TABLE proyecto_revisor (
    proyecto_clave_proyecto CHAR(100),
    revisor_id_revisor INT,
    PRIMARY KEY (proyecto_clave_proyecto, revisor_id_revisor),
    FOREIGN KEY (proyecto_clave_proyecto) REFERENCES proyecto(clave_proyecto),
    FOREIGN KEY (revisor_id_revisor) REFERENCES revisor(id_revisor)
);

CREATE TEMPORARY TABLE TempProyectos (
    clave_proyecto CHAR(100),
    nombre_proyecto VARCHAR(255),
    linea_investigacion VARCHAR(7),
    tipo VARCHAR(2),
    institucion VARCHAR(255),
    num_control CHAR(10),
    nombre_alumno VARCHAR(255),
    asesor VARCHAR(255),
    revisor_1 VARCHAR(255),
    revisor_2 VARCHAR(255),
    docente VARCHAR(255)
);

LOAD DATA LOCAL INFILE 'C:\\ABD\\Practica04_23270042.csv'
INTO TABLE TempProyectos
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY ';';

-- Insertar registros en las tablas relacionadas
INSERT INTO lineaInvestigacion (clave_linea)
SELECT DISTINCT linea_investigacion
FROM TempProyectos
WHERE linea_investigacion IS NOT NULL
ON DUPLICATE KEY UPDATE clave_linea = VALUES(clave_linea);

INSERT INTO tipoProyecto (tipo)
SELECT DISTINCT tipo
FROM TempProyectos
WHERE tipo IS NOT NULL
ON DUPLICATE KEY UPDATE tipo = VALUES(tipo);

INSERT INTO institucion (nombre_institucion)
SELECT DISTINCT institucion
FROM TempProyectos
WHERE institucion IS NOT NULL
ON DUPLICATE KEY UPDATE nombre_institucion = VALUES(nombre_institucion);

INSERT INTO asesor (nombre)
SELECT DISTINCT asesor
FROM TempProyectos
WHERE asesor IS NOT NULL
ON DUPLICATE KEY UPDATE nombre = VALUES(nombre);

INSERT INTO revisor (nombre)
SELECT DISTINCT revisor_1
FROM TempProyectos
WHERE revisor_1 IS NOT NULL
ON DUPLICATE KEY UPDATE nombre = VALUES(nombre);

INSERT INTO revisor (nombre)
SELECT DISTINCT revisor_2
FROM TempProyectos
WHERE revisor_2 IS NOT NULL
ON DUPLICATE KEY UPDATE nombre = VALUES(nombre);

INSERT INTO profesor (nombre)
SELECT DISTINCT docente
FROM TempProyectos
WHERE docente IS NOT NULL
ON DUPLICATE KEY UPDATE nombre = VALUES(nombre);

INSERT INTO proyecto (clave_proyecto, nombre, lineainvestigacion_clave_linea, tipoproyecto_id_tipo, profesor_id_profesor, asesor_id_asesor)
SELECT
    clave_proyecto,
    nombre_proyecto,
    (SELECT clave_linea FROM lineaInvestigacion WHERE clave_linea = linea_investigacion LIMIT 1),
    (SELECT id_tipo FROM tipoProyecto WHERE tipo = tipo LIMIT 1),
    (SELECT id_profesor FROM profesor WHERE nombre = docente LIMIT 1),
    (SELECT id_asesor FROM asesor WHERE nombre = asesor LIMIT 1)
FROM TempProyectos
WHERE clave_proyecto IS NOT NULL;

-- Insertar la rúbrica para cada proyecto
INSERT INTO rubrica (materia, proyecto_clave_proyecto)
SELECT 'MateriaEjemplo', clave_proyecto
FROM TempProyectos
WHERE clave_proyecto IS NOT NULL;

-- Insertar indicadores, descripciones y evaluaciones (aquí puedes ajustar los valores a insertar según el archivo de entrada)
INSERT INTO indicador (rubrica_id, numero, descripcion)
SELECT id_rubrica, 1, 'Indicador 1'
FROM rubrica
WHERE proyecto_clave_proyecto = (SELECT clave_proyecto FROM TempProyectos WHERE clave_proyecto IS NOT NULL LIMIT 1);

-- Insertar descripciones e indicadores
INSERT INTO descripcion_indicador (indicador_id, descripcion, ponderacion)
SELECT id_indicador, 'Descripción 1', 10
FROM indicador
WHERE rubrica_id = (SELECT id_rubrica FROM rubrica WHERE proyecto_clave_proyecto = 'clave_proyecto');

-- Insertar evaluaciones
INSERT INTO evaluacion_indicador (indicador_id, evaluacion)
SELECT id_indicador, 'Evaluación de indicador 1'
FROM indicador
WHERE rubrica_id = (SELECT id_rubrica FROM rubrica WHERE proyecto_clave_proyecto = 'clave_proyecto');

INSERT INTO alumno (num_control, nombre)
SELECT num_control, nombre_alumno
FROM TempProyectos
WHERE num_control IS NOT NULL;

-- Insertar usuarios con sus perfiles y permisos
INSERT INTO usuario (nombre, perfil, permisos, num_control)
SELECT nombre_alumno, 'alumno', 'permisos_estudiante', num_control
FROM TempProyectos
WHERE num_control IS NOT NULL;

INSERT INTO usuario (nombre, perfil, permisos, profesor_id)
SELECT docente, 'profesor', 'permisos_profesor', (SELECT id_profesor FROM profesor WHERE nombre = docente LIMIT 1)
FROM TempProyectos
WHERE docente IS NOT NULL;

-- Asignar revisores a los proyectos
INSERT INTO proyecto_revisor (proyecto_clave_proyecto, revisor_id_revisor)
SELECT 
    clave_proyecto,
    (SELECT id_revisor FROM revisor WHERE nombre = revisor_1 LIMIT 1)
FROM TempProyectos
WHERE revisor_1 IS NOT NULL;

INSERT INTO proyecto_revisor (proyecto_clave_proyecto, revisor_id_revisor)
SELECT 
    clave_proyecto,
    (SELECT id_revisor FROM revisor WHERE nombre = revisor_2 LIMIT 1)
FROM TempProyectos
WHERE revisor_2 IS NOT NULL;

DROP TEMPORARY TABLE IF EXISTS TempProyectos;
