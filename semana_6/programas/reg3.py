import xlsxwriter
import time
import serial
from datetime import datetime
from smbus2 import SMBus
from mlx90614 import MLX90614
from tkinter import *
from tkinter import messagebox

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib, ssl

flag = False

window = Tk()
width_window = 700
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

ser = serial.Serial('/dev/ttyUSB0')  # open serial port

#
now = datetime.now()
  
workbook = xlsxwriter.Workbook('registro'+'-'+str(now.month)+'-'+str(now.day)+'.xlsx') 
  
# By default worksheet names in the spreadsheet will be  
# Sheet1, Sheet2 etc., but we can also specify a name. 
worksheet = workbook.add_worksheet("Registro")
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})


worksheet.write('A1', 'CÉDULA', bold)
worksheet.write('B1', 'PRIMER APELLIDO', bold)
worksheet.write('C1', 'SEGUNDO APELLIDO', bold)
worksheet.write('D1', 'PRIMER NOMBRE', bold)
worksheet.write('E1', 'SEGUNDO NOMBRE', bold)
worksheet.write('F1', 'GENERO', bold)
worksheet.write('G1', 'FECHA DE NACIMIENTO', bold)
worksheet.write('H1', 'GRUPO SANGUINEO', bold)
worksheet.write('I1', 'TEMPERATURA', bold)
worksheet.write('J1', 'HORA', bold)

#
worksheet.set_column('A:Z', 20)

# Start from the first cell. Rows and 
# columns are zero indexed. 
row = 1
col = 0

def on_closing():
    if messagebox.askyesno("Salir", "Seguro que quiere salir?"):
        window.destroy()
        flag = True


def clicked():
    time.sleep(1)
    global row, col
    bus = SMBus(1)
    sensor = MLX90614(bus, address=0x5A)
    x=0
    for i in range(6):
        if i>2:
            x+=sensor.get_object_1()
    
    x=x/3
    
    datoTemp=0.0009852*x**3 - 0.128*x**2 + 6.116*x - 62.01
    
    #datoTemp = read_object_temp()
    line = ser.readline()
    cadena = line.split()
    # captura de hora
    reg = datetime.now()
    
    lbl_nt.configure(text=str(cadena[3], 'utf-8'))
    lbl_at.configure(text=str(cadena[1], 'utf-8'))
    lbl_tt.configure(text=str(round(datoTemp, 2)))
    lbl_ht.configure(text=str(reg.hour)+":"+str(reg.minute))
    
    #print( {(sensor.get_ambient()),sensor.get_object_1(), sensor.get_object_2()})
    print("ambiente: '{}', objeto 1: '{}', objeto 2: '{}'".format((sensor.get_ambient()),sensor.get_object_1(), sensor.get_object_2()))


    worksheet.write(row,8, str(round(datoTemp,2)))
    worksheet.write(row,9, str(reg.hour)+":"+str(reg.minute))
    
    # Iterate over the data and write it out row by row.
    if (len(cadena) == 7):
        worksheet.write(row,0, str(cadena[0], 'utf-8'))
        worksheet.write(row,1, str(cadena[1], 'utf-8'))
        worksheet.write(row,2, str(cadena[2], 'utf-8'))
        worksheet.write(row,3, str(cadena[3], 'utf-8'))
        worksheet.write(row,4, ' ')
        worksheet.write(row,5, str(cadena[4], 'utf-8'))
        worksheet.write(row,6, str(cadena[5], 'utf-8'))
        worksheet.write(row,7, str(cadena[6], 'utf-8'))       
    else:
        for cad in (cadena): 
            worksheet.write(row, col, str(cad, 'utf-8'))          
            col += 1

    row += 1
    col = 0


def clickedReport():
    # create message object instance
    msg = MIMEMultipart()

    from_address = 'gomezmunera@corum.org.co'
    to_address = 'gomezmunera@gmail.com'
    subject = 'prueba de envio'

    msg["From"] = from_address
    msg["To"] = to_address
    msg["subject"] = subject

    #instancia de MIMEBase y lo nombra part
    part = MIMEBase('application', "octet-stream")
    # abre el archivo a enviar
    part.set_payload(open('registro'+'-'+str(now.month)+'-'+str(now.day)+'.xlsx', "rb").read())
    #encode en base64
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="registro'+'-'+str(now.month)+'-'+str(now.day)+'.xlsx"')
    msg.attach(part)

    message = 'Esto es una prueba de envio de mail, dentro del programa registro de personas'
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    email = smtplib.SMTP('smtp.gmail.com', 587)
    email.ehlo()
    email.starttls()
    password = 'CORUM2010'

    #login y envio del mail
    email.login(from_address, password)
    email.sendmail(msg['From'], msg['To'], msg.as_string())
    email.quit()
    

window.title("Registro de Temperatura")

lbl_n = Label(vp, text="Nombre", padx=5, pady=5, font='Arial 18 bold')
lbl_n.grid(column=0, row=1)

lbl_a = Label(vp, text="Apellido", padx=5, pady=5,font='Arial 18 bold')
lbl_a.grid(column=2, row=1)

lbl_t = Label(vp, text="Temperatura", padx=5, pady=5,font='Arial 18 bold')
lbl_t.grid(column=3, row=1)

lbl_h = Label(vp, text="Hora", padx=5, pady=5,font='Arial 18 bold')
lbl_h.grid(column=4, row=1)

lbl_nt = Label(vp, text=" ", padx=5, pady=5, font='Arial 18')
lbl_nt.grid(column=0, row=2)

lbl_at = Label(vp, text=" ", padx=5, pady=5, font='Arial 18')
lbl_at.grid(column=2, row=2)

lbl_tt = Label(vp, text=" ", padx=5, pady=5, font='Arial 18')
lbl_tt.grid(column=3, row=2)

lbl_ht = Label(vp, text=" ", padx=5, pady=5, font='Arial 18')
lbl_ht.grid(column=4, row=2)

btn = Button(vp, text="Registrar", command=clicked, font='Arial 16')
btn.grid(column=0, row=3)

btn_e = Button(vp, text="Enviar Reporte", command=clickedReport, font='Arial 16')
btn_e.grid(column=4, row=3)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()

ser.close()             # close port
workbook.close()
