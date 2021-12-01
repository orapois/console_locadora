import db
conexao = db.iniciar_conexao()


def verificacao(numero):
    while numero == 1:
        print('Para pesquisar filmes por ano digite 1\n'
        'nome 2\n'
        'ator 3\n'
        'genero 4\n'
        'tudo 5'
        )
        pesquisa = int(input())
        pesquisa_filme(pesquisa, conexao)
    else:
        print("Você digitou alguma opção errada")
        print ("Para Buscar um filme digite 1\n para adicionar um filme ao catalogo digite 2.")
        c = input(int())
        if c == 1:
            verificacao(c)
    
def pesquisa_filme(numero, conexao):
    while numero >= 1 and numero <= 5:
        if numero == 5:
            lista = db.mostrar_tudo(conexao)
            for c in lista:
                print("Filme:", c[0], "| Genero:", c[1], "| Ano:", c[2])
            break
        if numero == 4:
            genero = input("Digite o genero: ")
            lista = db.por_genero(conexao,genero)
            for c in lista:
                print("Filme:", c[0],"| Genero:", c[1], "| Ano:", c[2])
            break
        if numero == 3:
            ator = input("Digite o nome do ator: ")
            lista = db.por_ator(conexao,ator)
            for c in lista:
                print("Filme:", c[0],"| Genero:", c[1], "| Ano:", c[2])
            break
        if numero == 2:
            filme = input("Digite o nome do filme: ")
            lista = db.por_filme(conexao,filme)
            for c in lista:
                print("Filme:", c[0],"| Genero:", c[1], "| Ano:", c[2])
            break
        if numero == 1:
            ano = input("Digite o ano do filme: ")
            lista = db.por_ano(conexao,ano)
            for c in lista:
                print("Filme:", c[0],"| Genero:", c[1], "| Ano:", c[2])
            break
        else:
            print("Você digitou alguma opção errada")