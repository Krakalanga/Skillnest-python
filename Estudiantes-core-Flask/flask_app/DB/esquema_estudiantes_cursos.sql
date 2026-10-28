CREATE DATABASE IF NOT EXISTS esquema_estudiantes_cursos
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE esquema_estudiantes_cursos;


CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);


CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    edad INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    curso_id INT,

    CONSTRAINT fk_estudiantes_cursos
        FOREIGN KEY (curso_id)
        REFERENCES cursos(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);