from db import *
from tkinter import *
from tkinter import ttk

root=Tk()

class Aplicacao():
    def __init__(self):
        self.root=root
        self.tela()
        self.Frame()
        root.mainloop()
    def tela(self):
        self.root.title('Gerenciador')
        self.root.configure(background='black')
        self.root.geometry('400x300')

    def Frame(self):
        self.Main = Frame(self.root, bg='white', highlightbackground='black')
        self.Main.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

Aplicacao()