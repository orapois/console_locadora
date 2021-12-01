import db

#Iniciando a conexão
conexao = db.iniciar_conexao()

print ("Locadora", end='\n\n')

print('Para pesquisar filmes por ano digite 1\n'
      'nome 2\n'
      'ator 3\n'
      'genero 4\n'
      'tudo 5'
      )

pesquisa = int(input())
if pesquisa == 5:
      lista = db.mostrar_tudo(conexao)
      for c in lista:
            print("Filme:", c[0], "| Genero:", c[1], "| Ano:", c[2])
if pesquisa == 4:
      genero = input("Digite o genero: ")
      lista = db.por_genero(conexao,genero)
      for c in lista:
            print("Filme:", c[0],"| Genero:", c[1], "| Ano:", c[2])
if pesquisa == 3:
      ator = input("Digite o nome do ator: ")
      lista = db.por_ator(conexao,ator)
      for c in lista:
            print("Filme:", c[0],"| Genero:", c[1], "| Ano:", c[2])
if pesquisa == 2:
      filme = input("Digite o nome do filme: ")
      lista = db.por_filme(conexao,filme)
      for c in lista:
            print("Filme:", c[0],"| Genero:", c[1], "| Ano:", c[2])
if pesquisa == 1:
      ano = input("Digite o ano do filme: ")
      lista = db.por_ano(conexao,ano)
      for c in lista:
            print("Filme:", c[0],"| Genero:", c[1], "| Ano:", c[2])

