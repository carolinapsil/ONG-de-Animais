import PySimpleGUI as sg
from PySimpleGUI import Button


class TelaAdocao:

    def __init__(self, controlador_adocao):
        self.__controlador_adocao = controlador_adocao
        self.__window = None
        self.__window2 = None
        self.__window3 = None
        self.__window4 = None
        self.init_components()

    @property
    def window(self):
        return self.__window

    @property
    def window2(self):
        return self.__window2

    @property
    def window3(self):
        return self.__window3

    @property
    def window4(self):
        return self.__window4

    def init_components(self):
        sg.ChangeLookAndFeel('BlueMono')

        botoes = [
                    [sg.Button('Incluir', size=(20, 2), key=1, button_color='#7B68EE')],
                    [sg.Button('Alterar', size=(20, 2), key=2, button_color='#7B68EE')],
                    [sg.Button('Listar', size=(20, 2), key=3, button_color='#7B68EE')],
                    [sg.Button('Excluir', size=(20, 2), key=4, button_color='#7B68EE')],
                    [sg.Button('Retornar', size=(20, 2), key=0, button_color='#7B68EE')]
        ]

        layout = [
                    [sg.Text("ADOÇÃO", justification='center', size=(20, 1), font=("Helvetica", 15))],
                    [sg.Text("O que deseja fazer?", justification='center', size=(20, 1), font=("Helvetica", 10))],
                    [sg.Column(botoes, vertical_alignment='center', justification='center')]
        ]

        self.__window = sg.Window('Tela Adoção', default_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def pega_dados_adocao(self):
        sg.ChangeLookAndFeel('BlueMono')

        entrada = [
                    [sg.Text("Adotante")],
                    [sg.InputText(size=(20, 2), key="adotante")],
                    [sg.Text("Animal")],
                    [sg.InputText(size=(20, 2), key="animal")],
                    [sg.Text('Data da adoção')],
                    [sg.InputText(size=(20, 2), key="data")],
                    [sg.Text('Código da adoção')],
                    [sg.InputText(size=(20, 2), key="codigo")],
                ]

        layout = [
                  [sg.Text('Adoção', size=(10,1), font=("Helvetica", 25), justification='center')],
                  [sg.Column(entrada, vertical_alignment='center', justification='center', k='-C-')]
        ]

        self.__window2 = sg.Window("Adoção", default_element_size=(30, 1)).Layout(layout)

    def abrir_cadastro_adocao(self):
        self.pega_dados_adocao()
        button, values = self.__window2.Read()
        return values

    def fechar_cadastro_adocao(self):
        if self.__window2 != None:
            self.__window2.Close()
        self.__window2 = None

    def mostra_adocao(self, dados_adocao):
        sg.ChangeLookAndFeel('BlueMono')

        dados = [[sg.Text("ADOTANTE: ", dados_adocao["adotante"], font=("Helvetica", 25), justification='center')],
                 [sg.Text("ANIMAL: ", dados_adocao["animal"], font=("Helvetica", 25), justification='center')],
                 [sg.Text("DATA ADOÇÃO: ", dados_adocao["data"], font=("Helvetica", 25), justification='center')],
                 [sg.Text("CÓDIGO DA ADOÇÃO: ", dados_adocao["codigo"], font=("Helvetica", 25), justification='center')]]

        layout = [[sg.Text('Adoções', size=(10, 1), font=("Helvetica", 25), justification='center')],
                  [sg.Column(dados, vertical_alignment='center', justification='center', k='-C-')]]

        self.__window3 = sg.Window("Adoção", default_element_size=(30, 1)).Layout(layout)

    def seleciona_adocao(self):
        sg.ChangeLookAndFeel('BlueMono')

        layout = [[sg.Text("Digite o código da adoção que deseja selecionar")],
                  [sg.InputText(size=(20, 2), key="codigo")]]

        self.__window4 = sg.Window("Adoção", default_element_size=(30, 1)).Layout(layout)
