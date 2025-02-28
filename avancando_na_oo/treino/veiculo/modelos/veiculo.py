class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'{self._marca} | {self._modelo} | {self.ligado}'

    @property
    def ligado(self):
        if self._ligado:
            return "Ligado"
        else:
            return "Desligado"

    def ligar(self):
        self._ligado = not self._ligado