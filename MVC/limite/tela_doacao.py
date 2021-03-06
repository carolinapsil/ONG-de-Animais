import PySimpleGUI as sg
from PySimpleGUI import Button


class TelaDoacao():

    def __init__(self, controlador_doacao):
        self.__controlador_doacao = controlador_doacao
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
                    [sg.Text("DOAÇÃO", justification='center', size=(20, 1), font=("Helvetica", 15))],
                    [sg.Text("O que deseja fazer?", justification='center', size=(20, 1), font=("Helvetica", 10))],
                    [sg.Column(botoes, vertical_alignment='center', justification='center')]
        ]

        self.__window = sg.Window('Tela Doação', default_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def pega_dados_doacao(self):
        sg.ChangeLookAndFeel('BlueMono')

        entrada = [
                    [sg.Text("Doador")],
                    [sg.InputText(size=(20,2), key="doador")],
                    [sg.Text("Valor doado")],
                    [sg.Slider(range=(1, 1000), orientation='h', size=(34, 20), default_value=50, key="valor")],
                    [sg.Text('Data da doacao')],
                    [sg.InputText(size=(20, 2), key="data_doacao")],
                    [sg.Text('Código da doacao')],
                    [sg.InputText(size=(20, 2), key="codigo")],
                ]

        layout = [
            [sg.Text('Cadastro Doação', size=(10,1), font=("Helvetica", 15), justification='center')],
            [sg.Column(entrada, vertical_alignment='center', justification='center', k='-C-')],
            [sg.Submit()]
                ]

        self.__window2 = sg.Window("Cadastro de Doação", default_element_size=(30, 1)).Layout(layout)

    def abrir_cadastro_doacao(self):
        self.pega_dados_doacao()
        button, values = self.__window2.Read()
        return values

    def fechar_cadastro_doacao(self):
        if self.__window2 != None:
            self.__window2.Close()
        self.__window2 = None

    def mostra_doacao(self, dados_doacao):
        sg.ChangeLookAndFeel('BlueMono')

        dados = [[sg.Text("DOADOR: ", dados_doacao["doador"], font=("Helvetica", 25), justification='center')],
                 [sg.Text("VALOR: ", dados_doacao["valor"], font=("Helvetica", 25), justification='center')],
                 [sg.Text("DATA DOAÇÃO: ", dados_doacao["data_doacao"], font=("Helvetica", 25), justification='center')],
                 [sg.Text("CÓDIGO DA DOACAO: ", dados_doacao["codigo"], font=("Helvetica", 25), justification='center')],
                [sg.Text("_"*100)]]
        layout = [[sg.Text('Adoções', size=(10, 1), font=("Helvetica", 25), justification='center')],
                  [sg.Column(dados, vertical_alignment='center', justification='center', k='-C-')]]

        self.__window3 = sg.Window("Adoção", default_element_size=(30, 1)).Layout(layout)

    def abrir_mostra_doacao(self):
        self.pega_dados_doacao()
        button, values = self.__window3.Read()
        return values

    def fecha_mostra_doacao(self):
        if self.__window3 != None:
            self.__window3.Close()
        self.__window3 = None


    def seleciona_doacao(self):
        sg.ChangeLookAndFeel('BlueMono')

        layout = [[sg.Text("Digite o código da doação que deseja selecionar")],
                  [sg.InputText(size=(20, 2), key="codigo")]]

        self.__window4 = sg.Window("Doação", default_element_size=(30, 1)).Layout(layout)