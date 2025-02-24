from modelos.restaurante import Restaurante

restaurante_praça = Restaurante("praça", "gourmet")
restaurante_praça.receber_avaliacao("Gian", 10)
restaurante_praça.receber_avaliacao("John", 6)
restaurante_praça.receber_avaliacao("Maria", 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()