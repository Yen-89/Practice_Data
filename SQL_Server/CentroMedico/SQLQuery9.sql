
CREATE TABLE Pago(
		idPago int IDENTITY (1,1) NOT NULL PRIMARY KEY,
		concepto tinyint NOT NULL,
		fecha datetime NOT NULL,
		monto money NOT NULL,
		estado tinyint NOT NULL,
		obs varchar(1000)
)