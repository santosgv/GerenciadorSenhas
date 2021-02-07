import sqlite3

class Banco():
    def conecta(self):
        self.conn=sqlite3.connect("senhas.db")
        self.cursor=self.conn.cursor();print('Conectado')

    def  desconecta(self):
        self.desconectar=self.conn.close()

    def login(self):
        self.conecta()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS login(
        cod integer primary key,
        login char(20) not null,
        senha char(20)
        );
        ''')

    def montar(self):
        self.conecta()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS SENHAS(
        cod integer primary key,
        site char(100) not null,
        senha char(100)
        );
        ''')
        self.conn.commit()
        self.desconecta()

    def novologin(self,login,senha):
        self.conn.execute(f''' insert into login values(%{login}%,%{senha}%)
        ''')
        self.conn.commit()
        self.desconecta()

    def checklogin(self,login,senha):
        consulta=self.cursor.execute(f'''
        SELECT * FROM SENHAS where site like ("%{login}% and ("%{senha}%")")
        ''')
        for login in consulta.fetchone():
            print(login)

    def inserirsenha(self,site,senha):
        self.conn.execute(f''' insert into SENHA values(%{site}%,%{senha}%)
        ''')
        self.conn.commit()
        self.desconecta()

    def checksenha(self,site):
        consulta=self.cursor.execute(f'''
        SELECT * FROM SENHAS where site like ("%{site}%")
        ''')
        for resultado in consulta.fetchone():
            print(resultado)