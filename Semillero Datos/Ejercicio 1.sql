CREATE DATABASE IF NOT EXISTS SEMILLERO_1;
USE SEMILLERO_1;

CREATE TABLE DIA_MADRES(
Nombre VARCHAR (50),
ValorRegalo FLOAT (10)
);

SELECT * FROM DIA_MADRES;

INSERT INTO DIA_MADRES (Nombre, ValorRegalo)
VALUES ('Andres', 100000),
('Jorge', 250000),
('Camila', 500000),
('Luis', 400000),
('Christian', 50000),
('Eliana', 100000),
('Alba', 70000),
('Fernanda', 600000),
('Manuel', 700000),
('Carlos', 350000),
('Fabricio', 100000),
('Cindy', 240000),
('Tatiana', 800000),
('Maria', 40000),
('Ricardo', 350000),
('Ana', 300000),
('Omar', 160000),
('Hector', 650000);

SELECT * FROM DIA_MADRES;

-- DE MENOR A MAYOR EN VALOR
SELECT Nombre, ValorRegalo
FROM DIA_MADRES
ORDER BY ValorRegalo ASC;

-- MAX y MIN
SELECT MAX(ValorRegalo) AS ValorMaximo, MIN(ValorRegalo) AS ValorMinimo
FROM DIA_MADRES;

-- MEDIA / PROMEDIO   Los dos son el valor central del conjunto de datos
SELECT AVG(ValorRegalo) AS Media, AVG(ValorRegalo) AS Promedio
FROM DIA_MADRES;

-- MEDIANA
SELECT t.ValorRegalo AS Mediana
FROM (
  SELECT ValorRegalo, @rownum:=@rownum+1 AS rownum, @total_rows:=@rownum
  FROM DIA_MADRES, (SELECT @rownum:=0) r
  ORDER BY ValorRegalo
) AS t
WHERE t.rownum IN (FLOOR((@total_rows+1)/2), FLOOR((@total_rows+2)/2));

-- MODA
SELECT ValorRegalo AS Moda, COUNT(ValorRegalo) AS Frecuencia
FROM DIA_MADRES
GROUP BY ValorRegalo
HAVING COUNT(ValorRegalo) = (
  SELECT MAX(Frecuencia)
  FROM (
    SELECT COUNT(ValorRegalo) AS Frecuencia
    FROM DIA_MADRES
    GROUP BY ValorRegalo
  ) AS T
);

-- VARIANZA / DESVIACIÓN
SELECT 
  AVG((ValorRegalo - media) * (ValorRegalo - media)) AS Varianza,
  SQRT(AVG((ValorRegalo - media) * (ValorRegalo - media))) AS DesviacionEst
FROM (
  SELECT ValorRegalo, 
         (SELECT AVG(ValorRegalo) FROM DIA_MADRES) AS media
  FROM DIA_MADRES
) AS subquery;

-- DISTINTOS DATOS
SELECT DISTINCT ValorRegalo
FROM DIA_MADRES;

-- PERCENTILES
SELECT
  PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY ValorRegalo) AS Cuartil_25,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY ValorRegalo) AS Cuartil_50,
  PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY ValorRegalo) AS Cuartil_75,
  PERCENTILE_CONT(1.0) WITHIN GROUP (ORDER BY ValorRegalo) AS Cuartil_100
FROM DIA_MADRES;
 



DELETE FROM DIA_MADRES;
ALTER TABLE DIA_MADRES CHANGE Detalle Nombre VARCHAR (50);
ALTER TABLE DIA_MADRES CHANGE ValorRegalo ValorRegalo FLOAT (10);






