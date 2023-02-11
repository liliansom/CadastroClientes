import pyodbc


# BACK-END
class Pessoa:
    def __init__(self, cad, nome, data, cpf, cep, rua, num, bairro, comp,
                 cidade, estado, pais, tel1, tel2, email, obs):
        self.cad = cad
        self.nome = nome
        self.data = data
        self.cpf = cpf
        self.cep = cep
        self.rua = rua
        self.num = num
        self.bairro = bairro
        self.comp = comp
        self.cid = cidade
        self.estado = estado
        self.pais = pais
        self.tel1 = tel1
        self.tel2 = tel2
        self.email = email
        self.obs = obs
        self.busca = []

    def adicionar(self):
        dadosconnect = "Driver={SQL Server};Server=.;Database=BDCadastro;"
        connection = pyodbc.connect(dadosconnect)
        cursor = connection.cursor()
        cursor.execute(f''' INSERT INTO Cadastro2 (Nome, DataNascimento, CPF, CEP, Logradouro, 
        Número, Bairro, Complemento, Cidade, Estado, País, Telefone1, Telefone2, Email, Observação)
                            VALUES('{self.nome}', 
                            '{self.data}', 
                            '{self.cpf}',
                            '{self.cep}',
                            '{self.rua}', 
                            '{self.num}', 
                            '{self.bairro}', 
                            '{self.comp}', 
                            '{self.cid}', 
                            '{self.estado}', 
                            '{self.pais}', 
                            '{self.tel1}', 
                            '{self.tel2}',
                            '{self.email}',
                            '{self.obs}'); ''')
        cursor.commit()
        cursor.close()
        connection.close()

    def excluir(self):
        dadosconnect = "Driver={SQL Server};Server=.;Database=BDCadastro;"
        connection = pyodbc.connect(dadosconnect)
        cursor = connection.cursor()
        # INSERIR MESSAGEBOX PARA CONFIRMAR AÇÃO
        cursor.execute(f''' DELETE FROM 
                                Cadastro2
                            WHERE 
                                NumCad='{self.cad}'; ''')
        cursor.commit()
        cursor.close()
        connection.close()

    def procurar(self):
        dadosconnect = "Driver={SQL Server};Server=.;Database=BDCadastro;"
        connection = pyodbc.connect(dadosconnect)
        cursor = connection.cursor()
        cursor.execute(f'''
                    SELECT 
                        NumCad, Nome, DataNascimento, CPF, CEP, Logradouro, 
                        Número, Bairro, Complemento, Cidade, Estado, 
                        País, Telefone1, Telefone2, Email, Observação
                    FROM 
                        Cadastro2 
                    WHERE
                        NumCad=? OR
                        Nome=?
                    ''', (self.cad, self.nome))

        self.busca = cursor.fetchone()
        cursor.close()
        connection.close()
        return self.busca


