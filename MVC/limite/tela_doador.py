import PySimpleGUI as sg
from PySimpleGUI import Button


class TelaDoador():

    def __init__(self, controlador_doador):
        self.__controlador_doador = controlador_doador
        self.__window = None
        self.__window2 = None
        self.__window3 = None
        self.__window4 = None
        self.init_components()

    @property
    def window(self):
        return self.__window



    def init_components(self):
        sg.ChangeLookAndFeel('BlueMono')

        botoes = [
                    [sg.Button('Cadastrar', size=(20, 2), key=1, button_color='#7B68EE')],
                    [sg.Button('Alterar', size=(20, 2), key=2, button_color='#7B68EE')],
                    [sg.Button('Listar', size=(20, 2), key=3, button_color='#7B68EE')],
                    [sg.Button('Retornar', size=(20, 2), key=0, button_color='#7B68EE')]
        ]

        layout = [
                    [sg.Text("DOADOR", justification='center', size=(20, 1), font=("Montserrat", 25))],
                    [sg.Text("O que deseja fazer?", justification='center', size=(15, 1), font=("Montserrat", 25))],
                    [sg.Column(botoes, vertical_alignment='center', justification='center')]
        ]

        self.__window = sg.Window('Tela Doador', default_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def pega_dados_doador(self):
        sg.ChangeLookAndFeel('BlueMono')

        entrada = [
                    [sg.Text("Nome")],
                    [sg.InputText(size=(20,2), key="nome")],
                    [sg.Text("Data de nascimento")],
                    [sg.InputText(size=(20,2), key="data_nascimento")],
                    [sg.Text('Telefone')],
                    [sg.InputText(size=(20, 2), key="telefone")],
                    [sg.Text('Gênero')],
                    [sg.InputCombo(('Feminino', 'Masculino'), size=(20, 3), key='genero')],
                    [sg.Text('Email')],
                    [sg.InputText(size=(20, 2), key="email")],
                    [sg.Text('Endereço')],
                    [sg.InputText(size=(20, 2), key="endereco")],
                    [sg.Button("Cadastrar", key=1)]
                ]

        layout = [
          [sg.Text('Login', size=(10,1), font=("Helvetica", 25), justification='center')],
          [sg.Column(entrada, vertical_alignment='center', justification='center', k='-C-')]
        ]

        self.__window2 = sg.Window("Cadastro de Doador", default_element_size=(30, 1)).Layout(layout)

    def abrir_cadastro_doador(self):
        self.pega_dados_doador()
        button, values = self.__window2.Read()
        return values

    def fechar_cadastro_doador(self):
        if self.__window2 != None:
            self.__window2.Close()
        self.__window2 = None

    def mostra_doador(self, dados_doador):
        sg.ChangeLookAndFeel('BlueMono')

        dados = [
        [sg.Text("NOME: ", dados_doador["nome"], font=("Helvetica", 25), justification='center')],
        [sg.Text("DATA DE NASCIMENTO: ", dados_doador["data_nascimento"], font=("Helvetica", 25), justification='center')],
        [sg.Text("TELEFONE: ", dados_doador["telefone"], font=("Helvetica", 25), justification='center')],
        [sg.Text("GÊNERO: ", dados_doador["genero"], font=("Helvetica", 25), justification='center')],
        [sg.Text("E-MAIL: ", dados_doador["email"], font=("Helvetica", 25), justification='center')],
        [sg.Text("ENDEREÇO: ", dados_doador["endereco"], font=("Helvetica", 25), justification='center')],

        ]

        layout = [
            [sg.Text('Doadores', size=(10, 1), font=("Helvetica", 13), justification='center')],
            [sg.Column(dados, vertical_alignment='center', justification='center', k='-C-')]
        ]

        self.__window3 = sg.Window("Cadastro de Doador", default_element_size=(30, 1)).Layout(layout)

    def abrir_mostra_doador(self):
        self.mostra_doador()
        button, values = self.__window3.Read()
        return values

    def fechar_mostra_doador(self):
        if self.__window3 != None:
            self.__window3.Close()
        self.__window3 = None

    def seleciona_doador(self):
        sg.ChangeLookAndFeel('BlueMono')

        layout = [
                    [sg.Text("Digite o telefone do doador que deseja selecionar")],
                    [sg.InputText(size=(20, 2), key="telefone")],
        ]

        self.__window4 = sg.Window("Doador", default_element_size=(30, 1)).Layout(layout)

    def abrir_seleciona_doador(self):
        self.pega_dados_doador()
        button, values = self.__window4.Read()
        return values

    def fechar_seleciona_doador(self):
        if self.__window4 != None:
            self.__window4.Close()
        self.__window4 = None
