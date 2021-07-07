import PySimpleGUI as sg

sg.popup('Hola', 'inicio de pysimplegui!')

# In[]
import PySimpleGUI as sg

event, values = sg.Window('Get filename example', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).read(close=True)

# In[]
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your creations colorful

layout = [  [sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Get filename example', layout)

event, values = window.read()
window.close()

# In[]
sg.popup('popup')  # Shows OK button
sg.popup_ok('popup_ok')  # Shows OK button
sg.popup_yes_no('popup_yes_no')  # Shows Yes and No buttons
sg.popup_cancel('popup_cancel')  # Shows Cancelled button
sg.popup_ok_cancel('popup_ok_cancel')  # Shows OK and Cancel buttons
sg.popup_error('popup_error')  # Shows red error button
sg.popup_timed('popup_timed')  # Automatically closes
sg.popup_auto_close('popup_auto_close')  # Same as PopupTimed

# In[]
import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

# In[]
import PySimpleGUI as sg

layout = [  [sg.Text("Pulsa", justification='c', size=(30,1), font='Mambo 30', key='-c-')],
            [sg.Button('Pulsa para Iniciar', size=(60, 12), font='Arial 15', key='-b-')] ]
window = sg.Window('Test', layout, size=(550, 350))

clicks = 0
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-b-':
        text = " " if clicks < 1 else str(clicks)
        window['-b-'].Update(text)
        clicks += 1
        window['-c-'].update(str(clicks))

window.close()