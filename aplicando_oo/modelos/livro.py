class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self.disponivel}'
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self.disponivel}'

    def emprestar(self):
        self._disponivel = not self._disponivel

    @property
    def disponivel(self):
        if self._disponivel:
            return "Disponível"
        else:
            return "Não disponível"

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro.livros:
            if ano == livro._ano_publicacao and livro._disponivel:
                livros_disponiveis.append(livro)
        return livros_disponiveis
                

            





    
        
