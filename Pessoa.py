import pyodbc


# BACK-END
class Pessoa:
    dadosconnect = "Driver={SQL Server};Server=.;Database=BDCadastro;"

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
        connection = pyodbc.connect(self.dadosconnect)
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
        connection = pyodbc.connect(self.dadosconnect)
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
        connection = pyodbc.connect(self.dadosconnect)
        cursor = connection.cursor()
        cursor.execute(f'''
                    SELECT 
                        *
                    FROM 
                        Cadastro2 
                    WHERE
                        Nome='{self.nome}' ''')

        result = cursor.fetchone()
        self.cad = str(result[0])
        self.nome = str(result[1])
        self.data = str(result[2])
        self.cpf = str(result[3])
        self.cep = str(result[4])
        self.rua = str(result[5])
        self.num = str(result[6])
        self.bairro = str(result[7])
        self.comp = str(result[8])
        self.cid = str(result[9])
        self.estado = str(result[10])
        self.pais = str(result[11])
        self.tel1 = str(result[12])
        self.tel2 = str(result[13])
        self.email = str(result[14])
        self.obs = str(result[15])
        cursor.close()
        connection.close()
        return

    def editar(self):
        connection = pyodbc.connect(self.dadosconnect)
        cursor = connection.cursor()
        cursor.execute(f'''
                            UPDATE 
                                Cadastro2
                            SET
                                Nome = '{self.nome}',
                                DataNascimento = '{self.data}', 
                                CPF = '{self.cpf}',
                                CEP = '{self.cep}',
                                Logradouro = '{self.rua}', 
                                Número = '{self.num}', 
                                Bairro = '{self.bairro}', 
                                Complemento = '{self.comp}', 
                                Cidade = '{self.cid}', 
                                Estado = '{self.estado}', 
                                País = '{self.pais}', 
                                Telefone1 = '{self.tel1}', 
                                Telefone2 = '{self.tel2}',
                                Email = '{self.email}',
                                Observação = '{self.obs}'
                                
                            WHERE
                                NumCad='{self.cad}' OR Nome='{self.nome}'
                            ''')
        cursor.commit()
        print(f'{self.nome}')
        cursor.close()
        connection.close()
        return