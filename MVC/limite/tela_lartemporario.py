import PySimpleGUI as sg
from PySimpleGUI import Button


class TelaLarTemporario:

    def __init__(self, controlador_lartemporario):
        self.__controlador_lartemporario = controlador_lartemporario
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
                    [sg.Text("LAR TEMPORÁRIO", justification='center', size=(20, 1), font=("Helvetica", 15))],
                    [sg.Text("O que deseja fazer?", justification='center', size=(20, 1), font=("Helvetica", 10))],
                    [sg.Column(botoes, vertical_alignment='center', justification='center')]
        ]

        self.__window = sg.Window('Tela Lar Temporario', default_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def pega_dados_lartemporario(self):
        sg.ChangeLookAndFeel('BlueMono')

        entrada = [
                    [sg.Text("Voluntário")],
                    [sg.InputText(size=(20, 2), key="voluntário")],
                    [sg.Text("Animal")],
                    [sg.InputText(size=(20, 2), key="animal")],
                    [sg.Text('Data da Entrada')],
                    [sg.InputText(size=(20, 2), key="data_entrada")],
                    [sg.Text('Código do Lar Temporario')],
                    [sg.InputText(size=(20, 2), key="codigo")],
                ]

        layout = [
                  [sg.Text('Lar Temporário', size=(10,1), font=("Helvetica", 25), justification='center')],
                  [sg.Column(entrada, vertical_alignment='center', justification='center', k='-C-')]
        ]

        self.__window2 = sg.Window("Lar Temporário", default_element_size=(30, 1)).Layout(layout)

    def abrir_cadastro_lartemporario(self):
        self.pega_dados_lartemporario()
        button, values = self.__window2.Read()
        return values

    def fechar_cadastro_lartemporario(self):
        if self.__window2 != None:
            self.__window2.Close()
        self.__window2 = None

    def mostra_lartemporario(self, dados_lartemporario):
        sg.ChangeLookAndFeel('BlueMono')

        dados = [[sg.Text("ADOTANTE: ", dados_lartemporario["voluntario"], font=("Helvetica", 25), justification='center')],
                 [sg.Text("ANIMAL: ", dados_lartemporario["animal"], font=("Helvetica", 25), justification='center')],
                 [sg.Text("DATA DE ENTRADA: ", dados_lartemporario["data_chegada"], font=("Helvetica", 25), justification='center')],
                 [sg.Text("CÓDIGO DO LAR TEMPORÁRIO: ", dados_lartemporario["codigo"], font=("Helvetica", 25), justification='center')]]

        layout = [[sg.Text('Lar Temporário', size=(10, 1), font=("Helvetica", 25), justification='center')],
                  [sg.Column(dados, vertical_alignment='center', justification='center', k='-C-')]]

        self.__window3 = sg.Window("Lar Temporário", default_element_size=(30, 1)).Layout(layout)

    def seleciona_lartemporario(self):
        sg.ChangeLookAndFeel('BlueMono')

        layout = [[sg.Text("Digite o código do lar temporário que deseja selecionar")],
                  [sg.InputText(size=(20, 2), key="codigo")]]

        self.__window4 = sg.Window("Lar Temporário", default_element_size=(30, 1)).Layout(layout)
