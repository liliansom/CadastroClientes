import tkinter as tk
class Pessoa:
    def __init__(self, Nome, DataNascimento, Idade, CPF):
        self.Numcad = 0
# pessoa
        self.nome = Nome
        self.dn = DataNascimento
        self.idade = Idade
        self.cpf = CPF
# endereço
        self.cep = CEP
        self.rua = Rua
        self.num = Numero
        self.bairro = Bairro
        self.comp = Complemento
# contatos
        self.tel1 = Telefone1
        self.tel2 = Telefone2
        self.email = EMail

    def adicionar(self):

    def procurar(self):

    def modificar(self):

    def excluir(self):


class Front:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry(x=1440, y=1024)

    def entry(self):

    def label(self):

    def outrajan(self):
        toplevel()


if __name__ == '__main__':
    Front()
