# Importamos el módulo Tkinter 
from tkinter import * 
from tkinter.ttk import *
  
# importamos el método strftime que devuelve la hora local 
from time import strftime 
  
# Creamos una ventana con Tkinter 
root = Tk() 
 
# Título de la Ventana 
root.title('Reloj') 
 
# Icono del Programa (Colocamos la ruta completa) 
#root.iconbitmap(r"D:/xampp/htdocs/xampp/nc/tutoriales/python_ejecutable/nc.ico")
  
# Creamos la función hora() para mostrar la hora en un label 
def hora(): 
    
    # Obtenemos la hora local 
    datos = strftime('%I:%M:%S %p') 
    
    # Pasamos la hora al label 
    label.config(text = datos) 
 
    # Hacemos un retardo de tiempo de 1 segundo, antes de ejecutar el reloj 
    label.after(1000, hora) 
  
# Estilizo mi reloj   
label = Label(root, 
	font = (
		'Arial', 60
	), 
	padding = '50',
    background = 'orange', 
    foreground = 'black' 
) 
  
# Expando el reloj en el centro de la ventana 
label.pack(expand = True) 
 
# Llamamos a la función hora() 
hora() 
 
# Con el método mainloop() le decimos a Python se detenga hasta aquí y no ejecute nada más  
mainloop()