import sqlite3
from sqlite3.dbapi2 import Cursor

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

def mostrar_tudo(conexao):
    filme = None
    try:
         cursor = conexao.cursor()
         cursor.execute("SELECT titulo, genero.nome, ano from filme, genero WHERE genero.id = filme.id")
         filme = cursor.fetchall()
    except sqlite3.Error as e:
        print("Ocorreu um erro:", e)
    finally:
        return filme

def por_ator(conexao, txt):
    filme = None
    try:
        var_select = "SELECT titulo, genero.nome, ano from filme, genero, atuacao, ator WHERE ator.nome = '"+ txt +"' and ator.id = atuacao.id_ator"
        cursor = conexao.cursor()
        cursor.execute(var_select)
        filme = cursor.fetchall()
    except sqlite3.Error as e:
        print("Ocorreu um erro:", e)
    finally:
        return filme