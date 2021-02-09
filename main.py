from db import *
from tkinter import *
from tkinter import ttk

root=Tk()
login=('vitor','senha123@')



class Funcoes():
    def validar(self):
        valida=(self.entlogin.get(),self.entsenha.get())

        if valida ==login:
            self.entlogin.destroy()
            self.entsenha.destroy()
            self.lblogin.destroy()
            self.lbsenha.destroy()
            self.btloga.destroy()

            self.lbaddsenha = Label(self.Main, text='Adicionar novas senhas')
            self.lbaddsenha.place(relx=0.01, rely=0.35)

            self.btadd=Button(self.Main,text='Adicionar')
            self.btadd.place(relx=0.45, rely=0.35)

            self.lbverificar = Label(self.Main, text='Verificar senhas salvas')
            self.lbverificar.place(relx=0.01, rely=0.45)

            self.btshow=Button(self.Main,text='Mostrar senhas')
            self.btshow.place(relx=0.45, rely=0.45)







class Aplicacao(Funcoes):
    def __init__(self):
        self.root=root
        self.tela()
        self.Frame()
        self.login()
        root.mainloop()

    def tela(self):
        self.root.title('Gerenciador')
        self.root.configure(background='black')
        self.root.geometry('400x300')

    def Frame(self):
        self.Main = Frame(self.root, bg='white', highlightbackground='black')
        self.Main.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def login(self):
        self.lblogin=Label(self.Main,text='Login')
        self.lblogin.place(relx=0.25, rely=0.35)

        self.entlogin=Entry(self.Main)
        self.entlogin.place(relx=0.40, rely=0.35)


        self.lbsenha=Label(self.Main,text='Senha')
        self.lbsenha.place(relx=0.25,rely=0.45)

        self.entsenha = Entry(self.Main,show='*')
        self.entsenha.place(relx=0.40, rely=0.45)

        self.btloga=Button(self.Main,text='Logar',command=self.validar)
        self.btloga.place(relx=0.50, rely=0.55)



Aplicacao()