#Os quatro passos que tem que ocorrer:
#1º Passo: Importar o pyodbc e criar uma Conexao
#2º Passo: Criar um Cursor
#3º Passo: Executar o comando que voce quer que o Cursor execute
#4º Passo: Depois de codar tudo, finalizar o Cursor ea Conexao

import pyodbc

#print(pyodbc.drivers())
#Print feito para conferir os drivers instalados na maquina

dados_conexao = ("Driver={SQLite3 ODBC Driver};"
           "Server=localhost;"
           "DataBase=salarios.sqlite;")

#Caso precise de login e senha:
#dados_conexao = ("Driver={Seu_Driver};"
#           "Server=Seu_Servido;" exemplo: "Server=localhost;"
#           "DataBase=Nome_Base_Dados;")
#           "UID=Login;"
#           "PWD=Senha;"

conexao = pyodbc.connect(dados_conexao)

#Cursor é onde fica tudo armazenado, o Cursos que comanda a integração do "pyodbc" com o "MySQL"
cursor = conexao.cursor() #quem vai executar os códigos SQL


#Comando que le o banco de dados e tras para o Python
cursor.execute("SELECT * FROM Salaries") #Achar a tabela "Salaries" pelo DB Browser

#Ver as informações do banco de dados
valores = cursor.fetchall()

#Lista muito grande, entao coloquei o limite até os 10 primeiros [:10]
#É apresentado em tuplas, cada tupla representa uma linha do nosso banco de dados
print(valores[:10])

cursor.close()
conexao.close()