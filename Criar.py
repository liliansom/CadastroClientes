import tkinter
import tkinter.ttk
from tkinter import *
from tkinter import PhotoImage
from Pessoa import Pessoa
from Requisitar import Requisitar


"""Criação do layout do programa"""
class Criar:
    def __init__(self, telaprincipal):
        self.telaprincipal = telaprincipal
        global bg
        self.height = 1440
        self.width = 1025
        bg = PhotoImage(file='BACKGROUND.png')
        back = Label(image=bg)
        back.place(x=-2, y=0)
        self.frame = tkinter.Frame(bg='#D4FFF7')
        self.frame.place(
            x=0,
            y=170,
            width=165,
            height=1000)
        self.botoes()
        self.entradas()
        self.labels()

    # Criação dos botões
    def botoes(self):
        self.botao = tkinter.Button()
        self.botao.place(
            x=20,
            y=244,
            height=40,
            width=120)
        self.botao.configure(text='Adicionar',
                             font='Jost', command=self.clicadc)

        self.botao1 = tkinter.Button()
        self.botao1.place(
            x=20,
            y=304,
            height=40,
            width=120)
        self.botao1.configure(text='Editar', font='Jost', command=self.cliceditar)

        self.botao2 = tkinter.Button()
        self.botao2.place(
            x=20,
            y=364,
            height=40,
            width=120)
        self.botao2.configure(text='Limpar', font='Jost', command=self.cliclimpar)

        self.botao3 = tkinter.Button()
        self.botao3.place(
            x=20,
            y=424,
            height=40,
            width=120)
        self.botao3.configure(text='Procurar', font='Jost', command=self.clicprocurar)

        self.botao4 = tkinter.Button()
        self.botao4.place(
            x=20,
            y=484,
            height=40,
            width=120)
        self.botao4.configure(text='Excluir', font='Jost', command=self.clicdeletar)

        self.botao5 = tkinter.Button()
        self.botao5.place(
            x=20,
            y=544,
            height=40,
            width=120)
        self.botao5.configure(text='Sair', font='Jost', command=self.telaprincipal.destroy)

        self.botao6 = tkinter.Button()
        self.botao6.place(
            x=177,
            y=310,
            height=30,
            width=40)
        self.botao6.configure(text='CEP', font='Jost', command=self.cliccep)

    # Criação das entradas de dados
    def entradas(self):
        self.entcad = tkinter.Entry(self.telaprincipal, relief="solid")
        self.entcad.place(
            x=230,
            y=209,
            width=75,
            height=30)
        self.entnome = tkinter.Entry(self.telaprincipal, relief="solid")
        self.entnome.place(
            x=330,
            y=209,
            width=300,
            height=30)
        self.entdata = tkinter.Entry(self.telaprincipal, relief="solid")
        self.entdata.place(
            x=650,
            y=209,
            width=175,
            height=30)

        self.entcpf = tkinter.Entry(relief="solid")
        self.entcpf.place(
            x=850,
            y=209,
            width=250,
            height=30)
        self.entcep = tkinter.Entry(relief="solid")
        self.entcep.place(
            x=230,
            y=309,
            width=100,
            height=30)
        self.entrua = tkinter.Entry(relief="solid")
        self.entrua.place(
            x=380,
            y=309,
            width=300,
            height=30)
        self.entnum = tkinter.Entry(relief="solid")
        self.entnum.place(
            x=730,
            y=309,
            width=100,
            height=30)
        self.entbairro = tkinter.Entry(relief="solid")
        self.entbairro.place(
            x=880,
            y=309,
            width=220,
            height=30)
        self.entcomplem = tkinter.Entry(relief="solid")
        self.entcomplem.place(
            x=230,
            y=384,
            width=250,
            height=30)
        self.entcid = tkinter.Entry(relief="solid")
        self.entcid.place(
            x=530,
            y=384,
            width=150,
            height=30)
        self.entest = tkinter.Entry(relief="solid")
        self.entest.place(
            x=730,
            y=384,
            width=150,
            height=30)
        self.entpais = tkinter.Entry(relief="solid")
        self.entpais.place(
            x=930,
            y=384,
            width=170,
            height=30)
        self.enttel1 = tkinter.Entry(relief="solid")
        self.enttel1.place(
            x=230,
            y=484,
            width=150,
            height=30)
        self.enttel2 = tkinter.Entry(relief="solid")
        self.enttel2.place(
            x=455,
            y=484,
            width=150,
            height=30)
        self.entemail = tkinter.Entry(relief="solid")
        self.entemail.place(
            x=680,
            y=484,
            width=200,
            height=30)
        self.entobs = tkinter.Text(relief="solid")
        self.entobs.place(
            x=230,
            y=559,
            width=400,
            height=80)
        self.entretorna = tkinter.Text(relief="solid")
        self.entretorna.place(
            x=800,
            y=559,
            width=300,
            height=80)
        return self

    # Métodos auxiliares
    # Criação das etiquetas
    def labels(self):  
        self.labelcad = tkinter.Label(text="Cadastro", background='white')
        self.labelcad.place(
            x=230,
            y=184)
        self.labelmenu = tkinter.Label(text="Menu", background='#D4FFF7', font='Jost')
        self.labelmenu.place(
            x=55,
            y=194)
        self.labelnome = tkinter.Label(text="Nome", background='white')
        self.labelnome.place(
            x=330,
            y=184)
        self.labeldn = tkinter.Label(text="Data de Nascimento", background='white')
        self.labeldn.place(
            x=650,
            y=184)
        self.labelcpf = tkinter.Label(text="CPF", background='white')
        self.labelcpf.place(
            x=850,
            y=184)
        self.labelend = tkinter.Label(text="Endereço Residencial", background='white')
        self.labelend.place(
            x=230,
            y=259)
        self.labelcep = tkinter.Label(text="CEP", background='white')
        self.labelcep.place(
            x=230,
            y=285)
        self.labelrua = tkinter.Label(text="Logradouro", background='white')
        self.labelrua.place(
            x=380,
            y=285)
        self.labelnum = tkinter.Label(text="Número", background='white')
        self.labelnum.place(
            x=730,
            y=285)
        self.labelbairro = tkinter.Label(text="Bairro", background='white')
        self.labelbairro.place(
            x=880,
            y=285)
        self.labelcomplem = tkinter.Label(text="Complemento", background='white')
        self.labelcomplem.place(
            x=230,
            y=359)
        self.labelcid = tkinter.Label(text="Cidade", background='white')
        self.labelcid.place(
            x=530,
            y=359)
        self.labelest = tkinter.Label(text="Estado", background='white')
        self.labelest.place(
            x=730,
            y=359)
        self.labelest = tkinter.Label(text="País", background='white')
        self.labelest.place(
            x=930,
            y=359)
        self.labelest = tkinter.Label(text="Contatos", background='white')
        self.labelest.place(
            x=230,
            y=434)
        self.labeltel1 = tkinter.Label(text="Telefone 1", background='white')
        self.labeltel1.place(
            x=230,
            y=459)
        self.labeltel2 = tkinter.Label(text="Telefone 1", background='white')
        self.labeltel2.place(
            x=455,
            y=459)
        self.labelemail = tkinter.Label(text="E-mail", background='white')
        self.labelemail.place(
            x=680,
            y=459)
        self.labelobs = tkinter.Label(text="Observações", background='white')
        self.labelobs.place(
            x=230,
            y=534)
        self.labelobs = tkinter.Label(text="Busca", background='white')
        self.labelobs.place(
            x=800,
            y=534)

    #Método para transformar entrada em string
    def trataent(self):
        self.cad = str(self.entcad.get())
        self.nome = str(self.entnome.get())
        self.data = str(self.entdata.get())
        self.cpf = str(self.entcpf.get())
        self.cep = str(self.entcep.get())
        self.rua = str(self.entrua.get())
        self.num = str(self.entnum.get())
        self.bairro = str(self.entbairro.get())
        self.comp = str(self.entcomplem.get())
        self.cid = str(self.entcid.get())
        self.estado = str(self.entest.get())
        self.pais = str(self.entpais.get())
        self.tel1 = str(self.enttel1.get())
        self.tel2 = str(self.enttel2.get())
        self.email = str(self.entemail.get())
        self.obs = str(self.entobs.get('1.0', 'end'))
        return self.cad, self.nome, self.data, self.cpf, self.cep, self.rua, \
               self.num, self.bairro, self.comp, self.cid, self.estado, \
               self.pais, self.tel1, self.tel2, self.email, self.obs

    # Método para buscar os valores das entradas
    def buscaent(self):
        self.cad = self.entcad.get()
        self.nome = self.entnome.get()
        self.data = self.entdata.get()
        self.cpf = self.entcpf.get()
        self.cep = self.entcep.get()
        self.rua = self.entrua.get()
        self.num = self.entnum.get()
        self.bairro = self.entbairro.get()
        self.comp = self.entcomplem.get()
        self.cid = self.entcid.get()
        self.estado = self.entest.get()
        self.pais = self.entpais.get()
        self.tel1 = self.enttel1.get()
        self.tel2 = self.enttel2.get()
        self.email = self.entemail.get()
        self.obs = self.entobs.get('1.0', 'end')
        return self.cad, self.nome, self.data, self.cpf, self.cep, self.rua, \
               self.num, self.bairro, self.comp, self.cid, self.estado, \
               self.pais, self.tel1, self.tel2, self.email, self.obs

    # Método para limpar as entradas
    def limpeza(self):
        self.entcad.delete('0', 'end')
        self.entnome.delete('0', 'end')
        self.entdata.delete('0', 'end')
        self.entidade.delete('0', 'end')
        self.entcpf.delete('0', 'end')
        self.entcep.delete('0', 'end')
        self.entrua.delete('0', 'end')
        self.entnum.delete('0', 'end')
        self.entbairro.delete('0', 'end')
        self.entcomplem.delete('0', 'end')
        self.entcid.delete('0', 'end')
        self.entest.delete('0', 'end')
        self.entpais.delete('0', 'end')
        self.enttel1.delete('0', 'end')
        self.enttel2.delete('0', 'end')
        self.entemail.delete('0', 'end')
        self.entobs.delete('1.0', 'end')
        self.entretorna.delete('1.0', 'end')

    # Método para retornar valores para o usuário
    def inserir(self, pessoa):
        self.entcad.delete('0', 'end')
        self.entnome.delete('0', 'end')
        self.entcad.insert(0, '{}'.format(pessoa.cad))
        self.entnome.insert(0, '{}'.format(pessoa.nome))
        self.entdata.insert(0, '{}'.format(pessoa.data))
        self.entcpf.insert(0, '{}'.format(pessoa.cpf))
        self.entcep.insert(0, '{}'.format(pessoa.cep))
        self.entrua.insert(0, '{}'.format(pessoa.rua))
        self.entnum.insert(0, '{}'.format(pessoa.num))
        self.entbairro.insert(0, '{}'.format(pessoa.bairro))
        self.entcomplem.insert(0, '{}'.format(pessoa.comp))
        self.entcid.insert(0, '{}'.format(pessoa.cid))
        self.entest.insert(0, '{}'.format(pessoa.estado))
        self.entpais.insert(0, '{}'.format(pessoa.pais))
        self.enttel1.insert(0, '{}'.format(pessoa.tel1))
        self.enttel2.insert(0, '{}'.format(pessoa.tel2))
        self.entemail.insert(0, '{}'.format(pessoa.email))
        self.entobs.insert('1.0', '{}'.format(pessoa.obs))

    # Métodos com funções de cada botão 
    # Método para função do botão Adicionar
    def clicadc(self):
        dadosstr = self.trataent()
        self.pessoa = Pessoa(*dadosstr)
        self.pessoa.adicionar()

    # Método para função do botão limpar
    def cliclimpar(self):
        self.limpeza()

    # Método para função do botão excluir
    def clicdeletar(self):
        dadosstr = self.trataent()
        self.pessoa = Pessoa(*dadosstr)
        self.pessoa.excluir()

    # Método para função do botão procurar
    def clicprocurar(self):
        dados = self.buscaent()
        self.pessoa = Pessoa(*dados)
        self.pessoa.procurar()
        self.inserir(self.pessoa)

    # Método para função do botão editar
    def cliceditar(self):
        dados = self.buscaent()
        self.pessoa = Pessoa(*dados)
        self.pessoa.procurar()
        dadosnovos = self.buscaent()
        self.pessoanova = Pessoa(*dadosnovos)
        self.pessoanova.editar()
        print(f'{self.pessoanova}')
        
    def cliccep(self):
        dados = self.buscaent()
        pessoa = dados[4]
        self.residencia = Requisitar(pessoa)
        self.residencia.request()
        self.entrua.insert(0, '{}'.format(self.residencia.rua))
        self.entbairro.insert(0, '{}'.format(self.residencia.bairro))
        self.entcid.insert(0, '{}'.format(self.residencia.cidade))
        self.entest.insert(0, '{}'.format(self.residencia.estado))
        self.entpais.insert(0, 'Brasil')
        return
        
