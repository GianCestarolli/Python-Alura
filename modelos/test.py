class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self.disponivel}'

    def emprestar(self):
        self._disponivel = not self._disponivel

    @property
    def disponivel(self):
        if self._disponivel:
            return "Disponível"
        else:
            return "Não disponível"

livro_1984 = Livro("1984", "George Orwell", "1949")
livro_noites_brancas = Livro("Noites Brancas", "Fiodor Dostoievsk", "1848")
livro_noites_brancas.emprestar()

print(livro_1984)
print(livro_noites_brancas)



    
        
