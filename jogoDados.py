import PySimpleGUI as sg    
from random import randint

from PySimpleGUI.PySimpleGUI import Window, popup

dado = randint(1,6)
# Layout                                                         # Creat GUI
layout = [[sg.Txt('ESCOLHA UM N* de 1 a 6')],                      
          [sg.Text('', size=(15, 1), font=('Helvetica', 18), text_color='red', key='input',background_color="white",justification="center")],
          [sg.Txt(''  * 10)],
          [sg.ReadFormButton('1',key=1), sg.ReadFormButton('2',key=2), sg.ReadFormButton('3',key=3)],
          [sg.ReadFormButton('4',key=4), sg.ReadFormButton('5',key=5), sg.ReadFormButton('6',key=6)],
          [sg.Button('Exit')],
          ]

# Set PySimpleGUI
form = sg.FlexForm('Acerte o número', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout)

# Set Process
Equal = ''
prog = 0

# Loop
while True:
    button, value = form.Read()    
    
    # Press Button
    if button == dado:
        Equal = 'Acertou'
        form.find_element('input').Update(Equal)
        popup('Voce ganhou')
        break
    if button != dado:
        Equal = 'Errou'
        form.find_element('input').Update(Equal)
        prog += 1
        if prog == 3:
            popup(' PERDEU!\nFim de jogo')
            break
    elif button == 'Exit':
        form.close()
        break   

form.close()  
