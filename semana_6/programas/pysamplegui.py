import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Algun texto en la fila 1')],
            [sg.Text('Entre un texto en la fila 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Text("El valor ingresado es: "),sg.Text("",size=(30,1), key='a')],
            ]

# Create the Window
window = sg.Window('Titulo de la ventana', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('Entraste ', values[0])
    num_cad = str(values[0])
    print((num_cad))
    window['a'].update(num_cad)

window.close()