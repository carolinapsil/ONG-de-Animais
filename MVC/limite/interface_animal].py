import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button

class TelaAnimalGUI():
  def __init__(self):
    self.__window = None
    self.__window2 = None

  def init_components(self):
    sg.ChangeLookAndFeel('DarkBlue')

    botoes = [
              [sg.Button('Cadastrar', size=(20,2), key=1)],
              [sg.Button('Alterar', size=(20,2), key=2)],
              [sg.Button('Excluir', size=(20,2), key=3)],
              [sg.Button('Listar', size=(20, 2), key=4)],
              [sg.Button('Retornar', size=(20, 2), key=5)]
            ]
    layout = [[sg.Text('Animais', size=(10, 1), font=("Helvetica", 25), justification='center')],
              [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]
    ]

    self.__window = sg.Window("Login", default_element_size=(40, 1)).Layout(layout)

  def open(self):
      self.__window = None
      self.init_components()
      button, values = self.__window.Read()
      return button

  def close(self):
      if self.__window != None:
          self.__window.Close()
      self.__window = None

  def show_message(self, titulo: str, mensagem: str):
      sg.Popup(titulo, mensagem)

  def pega_animal(self):
      sg.ChangeLookAndFeel('DarkBlue')

      entrada = [[sg.Text('Inserir os dados do Animal abaixo: ', size=(30, 1),
                   justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
                    [sg.Text('Nome', size=(15, 1)), sg.InputText('nome', key='nome')],
                    [sg.Text('Chegada', size=(15, 1)), sg.InputText('chegada', key='chegada')],
                    [sg.Text('Ano Nascimento', size=(15, 1)), sg.InputText('ano_nascimento', key='ano_nascimento')],
                    [sg.Text("Qual o sexo do Animal:")],
                    [sg.Radio('Fêmea', "RADIO1", default=True, size=(10, 1)), sg.Radio('Macho', "RADIO1")],
                    [sg.Text("O Animal possui doenças?:")],
                    [sg.Radio('Sim', "RADIO1", default=True, size=(10, 1)), sg.Radio('Não', "RADIO1")],
                    [sg.Text("O Animal está vacinado?:")],
                    [sg.Radio('Sim', "RADIO1", default=True, size=(10, 1)), sg.Radio('Não', "RADIO1")],
                    [sg.Text("O Animal está castrado?:")],
                    [sg.Radio('Sim', "RADIO1", default=True, size=(10, 1)), sg.Radio('Não', "RADIO1")],
                    [sg.Submit(tooltip='Clique para enviar os dados'), sg.Cancel()]]

      layout = [
          [sg.Text('Animal', size=(10, 1), font=("Helvetica", 25), justification='center')],
          [sg.Column(entrada, vertical_alignment='center', justification='center', k='-C-')]
      ]

      self.__window2 = sg.Window("Animal", default_element_size=(30, 1)).Layout(layout)

  def open_animal(self):
      self.pega_animal()
      button, values = self.__window2.Read()
      return values

  def close_animal(self):
      if self.__window2 != None:
          self.__window2.Close()
      self.__window2 = None

    window = sg.Window('Everything bagel', default_element_size=(40, 1), grab_anywhere = False).Layout(layout)
    button, values = window.Read()
    sg.Popup('Animais',
             'A opção selecionada foi "{}"'.format(button),
             'As informações são', values)


