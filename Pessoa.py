# BACK-END
class Pessoa:
    def __init__(self, nome):
        self.nome = self.entnome


    def adicionar():
        dadosconnect = "Driver={SQL Server};Server=DESKTOP-AB1DE95;Database=BDCadastro;"
        connection = pyodbc.connect(dadosconnect)
        cursor = connection.cursor()
        cursor.execute(f'''
          INSERT INTO 
              Clientes (
              Nome)
          VALUES(
              '{self.nome.get().strip().upper()}' ''')
        cursor.commit()
        connection.close()
        cursor.close()


'''    def procurar(self):

    def modificar(self):

    def excluir(self):

    def limpar(self):
'''
