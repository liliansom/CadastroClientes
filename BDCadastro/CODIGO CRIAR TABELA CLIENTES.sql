CREATE TABLE Clientes(
	NumCad INT IDENTITY (1,1) PRIMARY KEY,
	Nome VARCHAR (50),
	Sobrenome VARCHAR (50),
	DataNascimento DATE,
	CPF INT,
	Idade INT,
	Telefone1 INT,
	Telefone2 VARCHAR (50),
	EMail VARCHAR (50),
	Endere�o VARCHAR (50),
	N�mero INT,
	Complemento VARCHAR (50),
	Cidade VARCHAR (50),
	Estado VARCHAR (50),
	Bairro VARCHAR (50),
	CEP VARCHAR (50),
	Observa��o VARCHAR (200))
