import sqlite3


class Banco():
    def conecta(self):
        self.conn = sqlite3.connect("senhas.db")
        self.cursor = self.conn.cursor();
        print('Conectado')

    def desconecta(self):
        self.desconectar = self.conn.close()

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

    def inserirsenha(self, cod, site, senha):
        self.conecta()
        self.conn.execute(f'''
        INSERT INTO SENHAS VALUES ({cod},'{site}','{senha}')
        '''), self.conn.commit(),print('senha comitada'), self.desconecta()

    def checksenha(self, site):
        self.conecta()
        consulta = self.cursor.execute(f'''
        SELECT * FROM SENHAS where site like ("%{site}%")
        ''')
        for resultado in consulta.fetchall():
            self.desconecta()
            return resultado

    def vertudo(self):
        self.conecta()
        tudo = self.cursor.execute(f'''
        select * from SENHAS
    ''')
        for i in tudo.fetchall():
            self.desconecta()
            print(i)
            return i


b=Banco()
b.vertudo()