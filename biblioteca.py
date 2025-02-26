from modelos.livro import Livro

livro_1984 = Livro("1984", "George Orwell", 1949)
livro_noites_brancas = Livro("Noites Brancas", "Fiodor Dostoievsk", 1848)
livro_1984.emprestar()

for livro in Livro.livros:
    print (livro)

# livros_disponiveis_ano = Livro.verificar_disponibilidade(1949)

# for livro in livros_disponiveis_ano:
#     print (livro)