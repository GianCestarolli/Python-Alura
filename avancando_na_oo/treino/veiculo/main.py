from modelos.veiculo import Veiculo
from modelos.moto import Moto
from modelos.carro import Carro

moto_crf = Moto("Honda", "CRF 250", "Off Road")
carro_mobi = Carro("Fiat", "Mobi", 4)
carro_ka = Carro ("Ford", "Ka", 4)
carro_mobi.ligar()

print(moto_crf)
print(carro_mobi)
print(carro_ka)