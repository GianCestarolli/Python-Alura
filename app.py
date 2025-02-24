from modelos.restaurante import Restaurante

restaurante_praça = Restaurante("praça", "gourmet")
restaurante_mexicano = Restaurante("Mexican Food", "Mexicano")
restaurante_japones = Restaurante("Japão", "Japonesa")

restaurante_mexicano.alterar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()