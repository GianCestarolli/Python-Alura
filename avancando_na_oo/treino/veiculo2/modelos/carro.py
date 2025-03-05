from modelos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor

    def __str__(self):
        return f'{self._marca} | {self._modelo} | {self._cor}'

    def ligar(self):
        pass