CREATE TABLE estudiantes (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(25),
    apellido VARCHAR(25),
    edad INT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
