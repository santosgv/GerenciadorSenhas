from db import *
from tkinter import *
from tkinter import ttk
from db import Banco

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

            self.btadd=Button(self.Main,text='Adicionar',command=self.addsenha)
            self.btadd.place(relx=0.45, rely=0.35)

            self.lbverificar = Label(self.Main, text='Verificar senhas salvas')
            self.lbverificar.place(relx=0.01, rely=0.45)

            self.btshow=Button(self.Main,text='Mostrar senhas',command=self.showsenha)
            self.btshow.place(relx=0.45, rely=0.45)

    def addsenha(self):
        self.btshow.destroy()
        self.lbverificar.destroy()
        self.btadd.destroy()
        self.lbaddsenha.destroy()

        self.lbsite=Label(self.Main,text='Sites')
        self.lbsite.place(relx=0.1,rely=0.1)

        self.lbsenhas=Label(self.Main,text='Senhas')
        self.lbsenhas.place(relx=0.6, rely=0.1)

    def showsenha(self):
        self.btshow.destroy()
        self.lbverificar.destroy()
        self.btadd.destroy()
        self.lbaddsenha.destroy()

        self.showsenhas=Label(self.Main,text='Mostrando senhas')
        self.showsenhas.place(relx=0.1, rely=0.1)

        self.checksenhasite=Entry(self.Main)
        self.checksenhasite.place(relx=0.1, rely=0.20)

        self.btexibir=Button(self.Main,text='Exibir',command=self.senhadb)
        self.btexibir.place(relx=0.40, rely=0.20)

    def senhadb(self):
        b=Banco()
        b.conecta()
        site=self.checksenhasite.get()
        senhasdobanco =str(b.checksenha(site))
        self.lbsenhasbanco = Label(self.Main,text='')
        self.lbsenhasbanco.place(relx=0.1, rely=0.30,relwidth=0.60,relheight=0.60)
        self.lbsenhasbanco['text']=str(senhasdobanco)



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