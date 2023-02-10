import tkinter
import tkinter.ttk
from tkinter import *
from tkinter import PhotoImage
from Pessoa import Pessoa
import pyodbc


class Criar(tkinter.Frame):
    def __init__(self, parent):
        global bg
        super().__init__(parent)
        self.height = 1440
        self.width = 1025
        bg = PhotoImage(file='BACKGROUND.png')
        back = Label(image=bg)
        back.place(x=-2, y=0)
        self.frame = tkinter.Frame(bg='#D4FFF7')
        self.frame.place(
            x=0,
            y=136,
            width=165,
            height=1000)
        self.botoes()
        self.entradas()
        self.labels()
        self.clickadc()

    def botoes(self):
        self.botao = tkinter.Button()
        self.botao.place(
                x=20,
                y=210,
                height=40,
                width=120)
        self.botao.configure(text='Adicionar',font='Jost',command=Criar.clickadc)

        self.botao1 = tkinter.Button()
        self.botao1.place(
                x=20,
                y=270,
                height=40,
                width=120)
        self.botao1.configure(text='Editar', font='Jost')

        self.botao2 = tkinter.Button()
        self.botao2.place(
                x=20,
                y=330,
                height=40,
                width=120)
        self.botao2.configure(text='Limpar',font='Jost')

        self.botao3 = tkinter.Button()
        self.botao3.place(
                x=20,
                y=390,
                height=40,
                width=120)
        self.botao3.configure(text='Procurar', font='Jost')

        self.botao4 = tkinter.Button()
        self.botao4.place(
                x=20,
                y=450,
                height=40,
                width=120)
        self.botao4.configure(text='Clientes',font='Jost')

        self.botao5 = tkinter.Button()
        self.botao5.place(
                x=20,
                y=520,
                height=40,
                width=120)
        self.botao5.configure(text='Sair',font='Jost')

    def entradas(self, Nome):
        self.entcad = tkinter.Entry(relief="solid")
        self.entcad.place(
            x=200,
            y=175,
            width=75,
            height=30)
        self.entnome = tkinter.Entry(relief="solid")
        self.entnome.place(
            x=300,
            y=175,
            width=300,
            height=30)
        Nome = self.entnome
        self.entdn = tkinter.Entry(relief="solid")
        self.entdn.place(
            x=620,
            y=175,
            width=150,
            height=30)
        self.entidade = tkinter.Entry(relief="solid")
        self.entidade.place(
            x=820,
            y=175,
            width=100,
            height=30)
        self.entcpf = tkinter.Entry(relief="solid")
        self.entcpf.place(
            x=970,
            y=175,
            width=100,
            height=30)
        self.entcep = tkinter.Entry(relief="solid")
        self.entcep.place(
            x=200,
            y=275,
            width=100,
            height=30)
        self.entrua = tkinter.Entry(relief="solid")
        self.entrua.place(
            x=350,
            y=275,
            width=300,
            height=30)
        self.entnum = tkinter.Entry(relief="solid")
        self.entnum.place(
            x=700,
            y=275,
            width=100,
            height=30)
        self.entbairro = tkinter.Entry(relief="solid")
        self.entbairro.place(
            x=850,
            y=275,
            width=220,
            height=30)
        self.entcomplem = tkinter.Entry(relief="solid")
        self.entcomplem.place(
            x=200,
            y=350,
            width=250,
            height=30)
        self.entcid = tkinter.Entry(relief="solid")
        self.entcid.place(
            x=500,
            y=350,
            width=150,
            height=30)
        self.entest = tkinter.Entry(relief="solid")
        self.entest.place(
            x=700,
            y=350,
            width=150,
            height=30)
        self.entpais = tkinter.Entry(relief="solid")
        self.entpais.place(
            x=900,
            y=350,
            width=170,
            height=30)
        self.enttel1 = tkinter.Entry(relief="solid")
        self.enttel1.place(
            x=200,
            y=450,
            width=150,
            height=30)
        self.enttel2 = tkinter.Entry(relief="solid")
        self.enttel2.place(
            x=425,
            y=450,
            width=150,
            height=30)
        self.entemail = tkinter.Entry(relief="solid")
        self.entemail.place(
            x=650,
            y=450,
            width=200,
            height=30)
        self.entobs = tkinter.Text(relief="solid")
        self.entobs.place(
            x=200,
            y=525,
            width=400,
            height=100)
        self.entretorna = tkinter.Text(relief="solid")
        self.entretorna.place(
            x=770,
            y=525,
            width=300,
            height=100)
        return Nome

    def labels(self):
        self.labelcad = tkinter.Label(text="Cadastro", background='white')
        self.labelcad.place(
            x=198,
            y=150)
        self.labelmenu = tkinter.Label(text="Menu", background='#D4FFF7',font='Jost')
        self.labelmenu.place(
            x=55,
            y=160)
        self.labelnome = tkinter.Label(text="Nome", background='white')
        self.labelnome.place(
            x=300,
            y=150)
        self.labeldn = tkinter.Label(text="Data de Nascimento", background='white')
        self.labeldn.place(
            x=620,
            y=150)
        self.labelidade = tkinter.Label(text="Idade", background='white')
        self.labelidade.place(
            x=820,
            y=150)
        self.labelcpf = tkinter.Label(text="CPF", background='white')
        self.labelcpf.place(
            x=970,
            y=150)
        self.labelend = tkinter.Label(text="Endereço Residencial", background='white')
        self.labelend.place(
            x=198,
            y=225)
        self.labelcep = tkinter.Label(text="CEP", background='white')
        self.labelcep.place(
            x=198,
            y=250)
        self.labelrua = tkinter.Label(text="Logradouro", background='white')
        self.labelrua.place(
            x=350,
            y=250)
        self.labelnum = tkinter.Label(text="Número", background='white')
        self.labelnum.place(
            x=700,
            y=250)
        self.labelbairro = tkinter.Label(text="Bairro", background='white')
        self.labelbairro.place(
            x=850,
            y=250)
        self.labelcomplem = tkinter.Label(text="Complemento", background='white')
        self.labelcomplem.place(
            x=198,
            y=325)
        self.labelcid = tkinter.Label(text="Cidade", background='white')
        self.labelcid.place(
            x=500,
            y=325)
        self.labelest = tkinter.Label(text="Estado", background='white')
        self.labelest.place(
            x=700,
            y=325)
        self.labelest = tkinter.Label(text="País", background='white')
        self.labelest.place(
            x=900,
            y=325)
        self.labelest = tkinter.Label(text="Contatos", background='white')
        self.labelest.place(
            x=200,
            y=400)
        self.labeltel1 = tkinter.Label(text="Telefone 1", background='white')
        self.labeltel1.place(
            x=200,
            y=425)
        self.labeltel2 = tkinter.Label(text="Telefone 1", background='white')
        self.labeltel2.place(
            x=425,
            y=425)
        self.labelemail= tkinter.Label(text="E-mail", background='white')
        self.labelemail.place(
            x=650,
            y=425)
        self.labelobs= tkinter.Label(text="Observações", background='white')
        self.labelobs.place(
            x=200,
            y=500)
        self.labelobs= tkinter.Label(text="Busca", background='white')
        self.labelobs.place(
            x=770,
            y=500)

    def getnome(self):
        nome = Criar.entradas

    def clickadc(self):
        self.pessoa = Pessoa.adicionar()
        Criar.entradas.{'entnome'}.get()


def main():
    raiz = Tk()
    raiz.title("LM Cadastro de Clientes")
    frame = Criar(raiz)
    raiz.mainloop()
