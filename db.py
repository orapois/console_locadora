import sqlite3

#Nome do arquivo do db
arquivo = "locadora.db"

def iniciar_conexao():
    #Variavel de conexão vazia para tratamento de dados
    conexao = None

    try:
        #Conexão com o db
        conexao = sqlite3.connect(arquivo)
        print("Tudo Ok!", sqlite3.version)

    except sqlite3.Error as e:
        #Mostra o erro de conexão
        print("Ocorreu um erro:", e)
    
    return conexao

def fechar_conexao(conexao):
    if conexao:
        conexao.close()
        

#Iniciando a conexão
conexao = iniciar_conexao()

#Fechando a conexao
fechar_conexao(conexao)