CREATE DATABASE SEMILLERO;
USE SEMILLERO;

CREATE TABLE DIA_MADRE(
Nombre VARCHAR (50),
Regalo VARCHAR (50)
);

SELECT * FROM DIA_MADRE;

INSERT INTO DIA_MADRE (Nombre, Regalo)
VALUES ('Luisa','Regalo'),
('Andres', 'Restaurante'),
('Camila','Comida en casa'),
('Juliana','Regalo'),
('Juan David','Mariachis'),
('Leidy','Comida en casa'),
('Christian','Regalo'),
('Andrea','Regalo'),
('Olga','Paseo'),
('Daniel','Restaurante'),
('Wilmar','Comida en casa'),
('Oscar','Mariachis'),
('Juan Fernando','Paseo'),
('Natalia','Regalo'),
('Manuel','Regalo'),
('Lina','Mariachis'),
('Eliana','Comida en casa'),
('Jorge','Restautante'),
('Adriana','Paseo')
;

SELECT * FROM DIA_MADRE;

ALTER TABLE DIA_MADRE RENAME COLUMN Regalo TO Detalle;

SELECT DISTINCT Detalle FROM DIA_MADRE;

-- Cantidad por cada detalle
SELECT Detalle, COUNT(*) AS Cantidad
FROM DIA_MADRE
GROUP BY Detalle;

UPDATE DIA_MADRE
SET Detalle = 'Restaurante'
WHERE Detalle = 'Restautante' AND Nombre = 'Jorge';

SELECT * FROM DIA_MADRE;

-- MAX
SELECT Detalle, COUNT(*) AS Cantidad
FROM DIA_MADRE
GROUP BY Detalle
HAVING COUNT(*) = (SELECT MAX(CountDetalle) FROM (SELECT COUNT(*) AS CountDetalle FROM DIA_MADRE GROUP BY Detalle) AS DetalleCounts);

-- MIN
SELECT Detalle, COUNT(*) AS Cantidad
FROM DIA_MADRE
GROUP BY Detalle
HAVING COUNT(*) = (SELECT MIN(CountDetalle) FROM (SELECT COUNT(*) AS CountDetalle FROM DIA_MADRE GROUP BY Detalle) AS DetalleCounts);


-- El detalle que más se repite
SELECT Detalle, COUNT(*) AS Cantidad
FROM DIA_MADRE
GROUP BY Detalle
ORDER BY Cantidad DESC
LIMIT 1;

-- El detalle que menos se repite 
SELECT Detalle, COUNT(*) AS Cantidad
FROM DIA_MADRE
GROUP BY Detalle
ORDER BY Cantidad ASC
LIMIT 1;

-- No puedo scar la media / promedio ya que tengo datos de texto

DROP DATABASE semillero;





-- MODA



