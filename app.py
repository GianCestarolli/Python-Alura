from modelos.restaurante import Restaurante

restaurante_praça = Restaurante("praça", "gourmet")
restaurante_praça.alterar_estado()
restaurante_praça.receber_avaliacao("Gian", 5)
restaurante_praça.receber_avaliacao("John", 4)
restaurante_praça.receber_avaliacao("Maria", 20)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()