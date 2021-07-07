
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