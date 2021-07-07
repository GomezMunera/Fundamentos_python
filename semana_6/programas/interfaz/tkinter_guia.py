# -*- coding: utf-8 -*-
"""
tkinter librería para construir interfaces

"""
# In[]
"""
Creamos una ventana pero no la podemos ver, dado que no tenemos un 
ciclo repetitivo que la mantenga en visualización.
"""  
from tkinter import *

ventanaPrincipal = Tk()

# In[]

"""
Ya tenemos una ventana que se puede mostrar debido a que utilizamos 
el método mainloop(). Éste método mantiene visible la ventana
"""
from tkinter import *

ventanaPrincipal= Tk()



ventanaPrincipal.mainloop()

"""
Acá la aplicación ya funciona
"""

# In[]
"""
Agregamos un título a la ventana
"""
from tkinter import *

vp= Tk()

vp.title("Bienvenidos a Tkinter")

vp.mainloop()

# In[]
"""
Podemos crear otra ventana a través de:
    Tk():        Es una ventana nueva que no depende de la anterior
    Toplevel():  Es una ventana nueva que depende de una ventana principal
"""
from tkinter import *

ventanaPrincipal = Tk()
ventanaPrincipal.title("Ventana principal")
ventanaSecundaria = Tk()
ventana3 = Tk()
ventanaSecundaria.mainloop()

"""
 Al ejecutar el mainloop() en la ventana secundaria se abre la ventana
 principal también. Es necesario cerrar todas las ventanas
"""

# In[]

from tkinter import *

ventanaPrincipal= Tk()
#ventanaPrincipal.title("Ventana principal")
ventanaSecundaria=Toplevel()
ventana3=Toplevel()
ventana3.mainloop()

"""
 solo debo cerrar una vez usando TopLevel()
"""

# In[]
ventanaPrincipal= Tk()
ventanaPrincipal.title("Bienvenidos a Tkinter")
# Creando un label o etiqueta
label1 = Label(ventanaPrincipal,
               text = '\n Etiqueta 1 \n')

label1.pack(fill=X)
                                                         
label2 = Label(ventanaPrincipal, 
               text = '\n Etiqueta 2 \n').pack(side=RIGHT)
ventanaPrincipal.mainloop()

# In[]
"""
Creación de widgets label

"""
from tkinter import *

ventanaPrincipal= Tk()
ventanaPrincipal.title("Bienvenidos a Tkinter")

lbl = Label(ventanaPrincipal, text="Hola")

# es  necesario llamar la siguiente sentencia para que se muestre
lbl.grid(column=0, row=0)

lbl.configure(text="Otra cosa")

ventanaPrincipal.mainloop()

# In[]
"""
cambiando tipo de fuente
"""

ventanaPrincipal= Tk()
ventanaPrincipal.title("Bienvenidos a Tkinter")

#lbl = Label(ventanaPrincipal, text="Hola")
lbl = Label(ventanaPrincipal, text="Hola", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

ventanaPrincipal.mainloop()

# In[]
"""
Otra forma de cambiar el tipo de fuente

import tkinter.font as tkFont

ventanaPrincipal= Tk()
ventanaPrincipal.title("Bienvenidos a Tkinter")


lbl = Label(ventanaPrincipal, text="Hola")
lbl.pack()

fontExample = tkFont.Font(family="Arial",
                          size=25,
                          weight="bold",
                          slant="italic")

lbl.configure(font=fontExample)

ventanaPrincipal.mainloop()
"""

# In[]
"""
Cambiando tamaño de ventana
"""
ventanaPrincipal= Tk()
ventanaPrincipal.geometry('350x400')

ventanaPrincipal.title("Bienvenidos a Tkinter")

lbl = Label(ventanaPrincipal, text="Hola", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

ventanaPrincipal.mainloop()

# In[]
"""
Cambiando fondo de ventana
"""

ventanaPrincipal= Tk()
imagen = PhotoImage(file='fondo.png')
Lbl = Label(width=600, image=imagen)
Lbl.grid(row=0)

ventanaPrincipal.title("Bienvenidos a Tkinter")

lbl = Label(ventanaPrincipal, text="Hola", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

ventanaPrincipal.mainloop()


# In[]
"""
Agregar un botón
"""
ventanaPrincipal= Tk()
imagen = PhotoImage(file='fondo.png')
Lbl = Label(width=600, image=imagen)
Lbl.grid(row=0)

ventanaPrincipal.title("Bienvenidos a Tkinter")

lbl = Label(ventanaPrincipal, text="Hola", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)


btn = Button(ventanaPrincipal, text="Click")

btn.grid(column=0, row=1)

ventanaPrincipal.mainloop()

# In[]
"""
Agregar botón con otros colores y evento de click
"""
from tkinter import *

win = Tk()

win.title("Bienvenido a interfaces gráficas con python")

win.geometry('350x200')

lbl = Label(win, text="Hola")

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="El botón fue clickeado !!")

btn = Button(win, text="Click", bg="blue", fg="white", command=clicked)

btn.grid(column=1, row=0)
# si se colocan columnas más allá, igual este lo ubica ahí, usar frame

win.mainloop()

# In[]
"""
Agregar un botón
"""
ventanaPrincipal= Tk()
imagen = PhotoImage(file='fondo.png')
Lbl = Label(width=600, image=imagen)
Lbl.grid(row=0)

ventanaPrincipal.title("Bienvenidos a Tkinter")

lbl = Label(ventanaPrincipal, text="Hola", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="El botón fue clickeado !!")

btn = Button(ventanaPrincipal, text="Click", command = clicked)

btn.grid(column=1, row=0)

ventanaPrincipal.mainloop()

# In[]
"""
Para cambiar tamaño de la ventana y centrarla
"""
ventanaPrincipal= Tk()

width_window = 500
height_window = 200

width_screen = ventanaPrincipal.winfo_screenwidth()
height_sreen = ventanaPrincipal.winfo_screenheight()

x = (width_screen/2) - (width_window/2)
y = (height_sreen/2) - (height_window/2)

ventanaPrincipal.geometry('%dx%d+%d+%d' % (width_window, height_window, x, y))

ventanaPrincipal.title("Bienvenidos a Tkinter")

lbl = Label(ventanaPrincipal, text="Hola")

lbl.grid(column=0, row=0)
ventanaPrincipal.mainloop()

# In[]
"""
Entrada de datos usando Entry
"""
from tkinter import *

window = Tk()

window.title("Bienvenido a interfaces gráficas con python")

window.geometry('350x200')

lbl = Label(window, text="Hola mundo")

lbl.grid(column=0, row=0)

txt = Entry(window,width=20)

txt.grid(column=1, row=1)

def clicked():

    lbl.configure(text="El botón fue clickeado !! !! "+ txt.get())

btn = Button(window, text="Click", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()

# In[]
"""
Empaquetar en Frames
"""
from tkinter import *

window = Tk()
width_window = 400
height_window = 200

width_screen = window.winfo_screenwidth()
height_sreen = window.winfo_screenheight()

x = (width_screen/2) - (width_window/2)
y = (height_sreen/2) - (height_window/2)

window.geometry('%dx%d+%d+%d' % (width_window, height_window, x, y))

#window.geometry('700x200')
#Ventana Principal
vp = Frame(window, width=width_window, height=height_window)
# para organizar y dar formato al contenido de una ventana

# Empaqueta el frame en la raíz
vp.pack()

#vp.config(bg="blue")          # color de fondo, background
vp.config(cursor="")         # Tipo de cursor
#vp.config(relief="sunken")   # relieve del frame hundido
vp.config(bd=25)             # tamaño del borde en píxeles

#método grid para dar formato a la ventana
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
# column=0 y row=0 es para que quede centrado
#pads son para los margenes

#los métodos columnconfigure() y rowconfigure() que nos servirán para dar un peso 
#relativo al ancho y alto de todos los elementos que se añadan a la ventana.
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

def on_closing():
    if messagebox.askyesno("Salir", "Seguro que quiere salir?"):
        window.destroy()
        flag = True
        
def clicked():
    lbl_nt.configure(text=txt_n.get())

window.title("Registro")

lbl_n = Label(vp, text="Nombre", padx=5, pady=5, font='Arial 18 bold')
lbl_n.grid(column=0, row=1)

lbl_a = Label(vp, text="Apellido", padx=5, pady=5,font='Arial 18 bold')
lbl_a.grid(column=1, row=1)

lbl_h = Label(vp, text="Hora", padx=5, pady=5,font='Arial 18 bold')
lbl_h.grid(column=2, row=1)

txt_n = Entry(vp,width=10)
txt_n.grid(column=0, row=2)

lbl_nt = Label(vp, text=" ", padx=5, pady=5, font='Arial 18')
lbl_nt.grid(column=0, row=3)

lbl_at = Label(vp, text=" ", padx=5, pady=5, font='Arial 18')
lbl_at.grid(column=2, row=3)

lbl_ht = Label(vp, text=" ", padx=5, pady=5, font='Arial 18')
lbl_ht.grid(column=3, row=3)

btn = Button(vp, text="Registrar", command=clicked, font='Arial 16')
btn.grid(column=1, row=4)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()