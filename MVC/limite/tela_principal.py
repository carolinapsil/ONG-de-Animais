class TelaPrincipal():

    def __init__(self):
        pass

    def mostra_opcoes(self):
        print("1 - Doacoes")
        print("2 - Animais")
        print("3 - Adotante")
        print("4 - Doador")
        print("5 - Voluntario")
        print("6 - Adocoes")
        print("7 - Lar Temporario")
        print("8 - Pesquisar animais disponíveis para adoção")
        print("0 - Finalizar sistema")

        while True:

            try:
                opcoes_validas = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                opcao = int(input("Escolha uma opção: "))
                print('\n')
                if opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print('Opcao invalida!')
                print('\n')
