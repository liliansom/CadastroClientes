from Projeto import Criar
from tkinter import Tk
from Pessoa import Pessoa


def main():
    raiz = Tk()
    raiz.title("LM Cadastro de Clientes")
    frame = Criar(raiz)
    raiz.mainloop()


if __name__ == '__main__':
    main()
    
