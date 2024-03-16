import sqlite3

banco = sqlite3.connect('banco_de_dados.db') #cria banco de dados#
cursor = banco.cursor() #conecta o cursor

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(nome text, cpf text, senha text)") ##Cria tabela "usuarios" se não existir##

#
class Usuario:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

def lin():
    print('-=' * 10)

def menu():

    ##Função de Registro##
    def registro():
        lin()
        print('Registro')
        lin()
        nome = str(input('Seu nome:')).title()
        cpf = str(input('CPF:'))

        ##Tratamento de erro de cpf##
        while len(cpf) != 11:
            print('Digite um cpf válido!')
            cpf = str(input('CPF:'))
        cursor.execute("SELECT * FROM usuarios")
        usuarios = [usuario for usuario in cursor.fetchall()]
        cpfs = []
        for usuario in usuarios:
            cpfs.append(usuario[1])
        while cpf in cpfs:
            print('CPF Já utilizado!')
            cpf = str(input('CPF:'))
            while len(cpf) != 11:
                print('Digite um cpf válido!')
                cpf = str(input('CPF:'))

        senha = str(input('Senha:'))

        ##Tratamento de erro de senha##
        while len(senha) < 6 or senha.isnumeric() == False:
            lin()
            print('Erro!')
            lin()
