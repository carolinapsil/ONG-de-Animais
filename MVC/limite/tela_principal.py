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
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao