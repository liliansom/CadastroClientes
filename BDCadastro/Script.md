Caso tenho problemas para rodar o banco de dados, você precisará:

1) Instalar o SQL Server e o SQL Server Management Studio.
https://www.microsoft.com/pt-br/sql-server/sql-server-downloads

https://learn.microsoft.com/pt-br/sql/ssms/download-sql-server-management-studio-ssms?redirectedfrom=MSDN&view=sql-server-ver16

2) Criar um Banco de Dados, clicando com o botão direito do mouse em Banco de Dados e Novo Banco de Dados.

3) Criar o Banco de Dados "BDCadastro";

4) Clicar em Nova Consulta;

5) Certificar-se de que o Banco de Dados Disponível (Ctrl + U) é o BDCadastro;

6) Inserir o código a seguir:
CREATE TABLE Cadastro2(
	NumCad INT IDENTITY (1,1) PRIMARY KEY,
	Nome VARCHAR (50),
	Sobrenome VARCHAR (50),
	DataNascimento DATE,
	CPF INT,
	Idade INT,
	Telefone1 INT,
	Telefone2 VARCHAR (50),
	EMail VARCHAR (50),
	Endereço VARCHAR (50),
	Número INT,
	Complemento VARCHAR (50),
	Cidade VARCHAR (50),
	Estado VARCHAR (50),
	Bairro VARCHAR (50),
	CEP VARCHAR (50),
	Observação VARCHAR (200));

7) Clicar em Executar.

Após esses passos, você poderá criar uma Nova Consulta e verificar se sua tabela foi criada com o código:
SELECT
    *
FROM
    Cadastro2

Volte para seu editor de códigos e rode o programa.