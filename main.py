import db

#Iniciando a conexão
conexao = db.iniciar_conexao()

print ("Locadora", end='\n\n')

print('Para pesquisar filmes por ano digite 1\n'
      'nome 2\n'
      'ator 3\n'
      'genero 4\n'
      'tudo 4'
      )

pesquisa = int(input())
if pesquisa == 4:
      lista = db.mostrar_tudo(conexao)
      for c in lista:
            print("Filme:", c[0], "| Genero:", c[1], "| Ano:", c[2])

