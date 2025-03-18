-- Lucio Eduardo Santiago Moreno - S5A
-- No de control: 23270042
-- dbTaller

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
