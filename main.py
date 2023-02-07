import tkinter
from tkinter import *
from tkinter import Canvas
from tkinter import PhotoImage

"""class Pessoa:
    def __init__(self, NumCad, cadastro):
        self.Numcad = 0
        self.cadastro = cadastro()
        self.endereco = endereco()
        self.contato = contato()
    # pessoa
    def cadastro(self, Nome, DN, Idade, CPF):
        self.nome = Nome
        self.dn = DN
        self.idade = Idade
        self.cpf = CPF

# endereço
    def endereco(self, CEP, Rua, Numero, Bairro, Complemento):
        self.cep = CEP
        self.rua = Rua
        self.num = Numero
        self.bairro = Bairro
        self.comp = Complemento
# contatos
    def contato(self, Telefone1, Telefone2, EMail):
        self.tel1 = Telefone1
        self.tel2 = Telefone2
        self.email = EMail

class Repositorio:
    def __init__(self):

    def criar(self):

    def adicionar(self):

    def procurar(self):
        ENTRY.insert(
            0,
            '{}'.format(busca[4]))
        ENTRY.insert(
            '1.0',
            '{}'.format(busca[5]))
    def modificar(self):

    def excluir(self):"""

class Criar(tkinter.Frame):
    def __init__(self, parent):
        global bg
        super().__init__(parent)
        self.height = 1440
        self.width = 1025
        bg = PhotoImage(file='BACKGROUND.png')
        back = Label(image=bg)
        back.place(x=-2, y=0)

    def texto(self, nomes,  text, x, y):
        self.nomes = tkinter.Label(text)
        self.nomes.place(x, y)

"""    def entry(self):
        ENTRY = tk.Entry()
        ENTRY.place()
    def entry_text(self):
        EntDesc = tk.Text()
        EntDesc.place()

    def botao(self):
        BtProcurar = PhotoImage()
        btProcurar = tk.Button(
            image=BtProcurar,
            command=procurar)
        btProcurar.place(
            x=310,
            y=430)

    def outrajan(self):
        toplevel()
"""
if __name__ == "__main__":
    raiz = Tk()
    raiz.title("LM Cadastro de Clientes")
    frame = Criar(raiz)
    raiz.mainloop()
    raiz.Criar.texto(nomes, text="Nome", x=100, y=100)
