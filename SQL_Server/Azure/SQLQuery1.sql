-- DDL
-- CREATE, ALTER, DROP, RENAME
CREATE TABLE Product
(
	ID INT PRIMARY KEY,
	Name VARCHAR(20) NOT NULL,
	Price DECIMAL NULL
);

SELECT * FROM Product;

--DCL
-- permiso para que el usuario1 pueda seleccionar, insertar y eliminar de la tabla Product
GRANT SELECT, INSERT, UPDATE
ON Product
To user1;


--DML
-- SELECT , INSERT, UPDATE, DELETE
