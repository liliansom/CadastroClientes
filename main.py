# This is a sample Python script.
from Criar import *
from tkinter import Tk


def main():
    raiz = Tk()    
    raiz.title("LM Cadastro de Clientes")
    raiz.geometry('1440x1024')
    frame = Criar(raiz)
    raiz.mainloop()


if __name__ == '__main__':
    main()
    
    