import PySimpleGUI as sg


class AnimalView:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel("Reddit")

    layout = [[sg.Text("Cadastre as informações do Animal!", size = (30, 1), font = ("Helvetica", 25))]
              [sg.Text("Inserir o nome do Animal:")],
              [sg.InputText("", key = "nome_animal")],
              [sg.Text("Inserir a data de chegada:")],
              [sg.InputText("", key = "data_chegada")],
              [sg.Text("Inserir o ano de nascimento:")],
              [sg.InputText("", key = "ano_nascimento")],
              [sg.Text("Qual o sexo do Animal:")],
              [sg.Radio("Fêmea", "RD1", default = True, key = "rd_femea"),
               sg.Radio("Macho", "RD1", key = "rd_macho")],
              [sg.Text("O animal possui doenças?:")],
              [sg.Radio("Possui", "RD1", default = True, key = "rd_sim"),
               sg.Radio("Não possui", "RD1", key = "rd_nao")],
              [sg.Text("O Animal está vacinado?:")],
              [sg.Radio("Sim", "RD1", default = True, key = "rd_vacinado"),
               sg.Radio("Não", "RD1", key = "rd_naovacinado")],
              [sg.Text("O Animal está castrado?:")],
              [sg.Radio("Sim", "RD1", default = True, key = "rd_castrado"),
               sg.Radio("Não", "RD1", key = "rd_naocastrado")],
              [sg.Submit(), sg.Cancel()]
             ]

    self.__window = sg.Window("Cadastro de Animais", default_element_size == (40, 1).Layout(layout))



