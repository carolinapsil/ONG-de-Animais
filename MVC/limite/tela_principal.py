class TelaPrincipal():

    def __init__(self):
        pass

    def mostra_opcoes(self):
        print("1 - Doacoes")
        print("2 - Animais")
        print("3 - Adotante")
        print("4 - Doador")
        print("5 - Voluntario")
        opcao_escolhida = int(input("Escolha opcao:"))
        return opcao_escolhida