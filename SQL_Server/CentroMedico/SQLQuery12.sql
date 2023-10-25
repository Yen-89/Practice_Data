
CREATE TABLE MedicoEspecialidad (
		idMedico int NOT NULL,
		idEspecialidad int NOT NULL,
		Descripcion varchar(50)
		
		PRIMARY KEY (idMedico, idEspecialidad, Descripcion)
)