CREATE DATABASE AZURE;

USE AZURE

CREATE TABLE Customer (
	ID INT PRIMARY KEY NOT NULL,
	Nombre VARCHAR (20),
	Apellido VARCHAR (20),
	Ciudad VARCHAR (20),
	Edad INT,
	Cargo VARCHAR (50),
)

SELECT * FROM Customer;

INSERT INTO Customer(ID,Nombre, Apellido,Ciudad, Edad,Cargo)
VALUES (1,'Andrea', 'Ospina', 'Bello', 32 , 'Ingenieria de datos'),
		(2,'Manuel', 'Cardozo', 'Medellin', 43, 'Ingenierio de sistemas'),
		(3,'Maria', 'Cortez', 'Bogota', 25, 'Ingenieria de datos'),
		(4,'Lyda', 'Osorio', 'Bello', 47, 'Ingenieria de sistemas'),
		(5,'Daniel', 'Guos', 'Medellin', 29, 'Ingeniero de datos'),
		(6,'Alejandro', 'Garcia', 'Bello', 39, 'Ingeniero de sistemas')

SELECT*
FROM Customer
WHERE Ciudad = 'Bello';

SELECT Nombre, Edad, Cargo , Ciudad
FROM Customer
WHERE Ciudad = 'Medellin'
ORDER BY Nombre;

SELECT Nombre, Edad, Cargo , Ciudad
FROM Customer
ORDER BY Nombre;

