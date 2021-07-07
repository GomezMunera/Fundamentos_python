# -*- coding: utf-8 -*-
"""
libreria csv
"""

# In[]
# persistencia en los datos

import csv

# In[]
# para leer
# open abre y prepara el archivo
archivo = open("arreglo.txt")

# lee lo que hay en el archivo
a = archivo.read()

print(a)

# In[]
# lo divide tomando como referente la ,
b = a.split(",")
print(b)

# In[]
# Para escribir
k = [["e1","e10","e3"],[25,15,65]]

with open('prueba.csv', newline='', mode='w') as file: #w: abre en modo escritura
    writer = csv.writer(file)
    for i in k:
        writer.writerow([i])
                        
# In[]
with open('employee_file.csv',newline='', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
    
#%%
"""
más ejemplos de csv
"""
#%%
#Imprimir el archivo

import csv
with open('VentasCSV.csv', newline='', mode = 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')#, quotechar='\n')
    for row in spamreader:
        for j in range(len(row)):
            print(row[j],end=" ")
        print()
        

#%%
#Imprime cada 2 filas

with open("VentasCSV.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        print(next(reader))

#%%
#Imprimir por filas

with open("VentasCSV.csv") as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(len(row))

#%%
"""
pendiente
"""
import csv

with open("VentasCSV.csv") as f:
    reader = csv.reader(f)
    lista = []
    for row in reader:
        lista.append(row)

#%%
for i in range(len(lista)):
    if( i%2 != 0):
        print(lista[i])
        
#%%
with open("VentasCSV.csv") as f:
    reader = csv.reader(f)
    F=0
    for row in reader:
          if(F%2 != 0):
              print(row)
          F = F + 1

#%%
# Imprime la cantidad de filas indicadas con libreria itertools
from itertools import islice
import csv
with open("VentasCSV.csv") as f:
    reader = csv.reader(f)
    #rows = list(islice(reader,4))
    rows = list(islice(reader,0,9,2))
    print(rows)

#%%
# imprimir por columnas

import csv
with open('VentasCSV.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')#, quotechar='\n')
    for row in spamreader:
        for j in range(len(row)):
            print(row[j],end="\t")
        print()

#%%
"""
muestra todas las ventas de una columna
"""
import csv

with open('VentasCSV.csv') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=';')
    a=0
    vector = []
    for row in reader:
        
        print(row["Febrero"])
        a+=float(row["Febrero"])
        vector.append(float(row["Febrero"]))
        
    print(f"Ventas de Febrero: {a}")
    
#%%
"""
muestra número de ventas por filas
"""
import csv

with open('VentasCSV.csv') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=';')

    suma=0
    for row in reader:
        for llave in row:           
            if llave != "Producto" and llave !="Costo Unidad":
                suma+=float(row[llave])
                print(row[llave], end=" ")
                
        print(f"""\nTotal productos {row["Producto"]}: """,suma)
        suma=0
        print()

#%%
"""
Crea un diccionario data con los datos leidos del archivo
"""

with open('VentasCSV.csv') as file:
    data = {}
    for row in csv.DictReader(file,delimiter=';'):
        for key, value in row.items():
            print(key)
            print(value)
            if key not in data:
                data[key] = []
            data[key].append(value)

#%%
"""
crea un archivo csv en forma de diccionario
"""

import csv
 
with open('Estudiantes.csv', newline='', mode= 'w') as csvfile:
    campos = ['NOMBRE', 'APELLIDO', 'GRADO']
    writer = csv.DictWriter(csvfile, fieldnames=campos, delimiter=';')
 
    writer.writeheader()
    writer.writerow({'GRADO': 'B', 'NOMBRE': 'Alex', 'APELLIDO': 'Brian'})
    
    writer.writerow({'NOMBRE': 'Rachael',
                     'GRADO': 'A',
                     'APELLIDO': 'Rodriguez'})
    
    writer.writerow({'GRADO': 'B', 'NOMBRE': 'Jane', 'APELLIDO': 'Oscar'})
    writer.writerow({'GRADO': 'B', 'NOMBRE': 'Jane', 'APELLIDO': 'Loive'})
 
print("Archivo Guardado")

#%%
"""
crea un archivo csv en forma de diccionario con un solo writer
"""

import csv
 
with open('Estudiantes.csv', 'w', newline='') as csvfile:
    campos = ['NOMBRE', 'APELLIDO', 'GRADO']
    writer = csv.DictWriter(csvfile, fieldnames=campos, delimiter=';')
 
    writer.writeheader()
    writer.writerows([{'GRADO': 10, 'NOMBRE': 'Alex', 'APELLIDO': 'Brian'},
                      {'GRADO': 11, 'NOMBRE': 'Rachael', 'APELLIDO': 'Rodriguez'},
                      {'GRADO': 2, 'NOMBRE': 'Tom', 'APELLIDO': 'smith'},
                      {'GRADO': 5, 'NOMBRE': 'Jane', 'APELLIDO': 'Oscar'},
                      {'GRADO': 5, 'NOMBRE': 'Kennzy', 'APELLIDO': 'Tim'}])
 
print("Archivo Guardado")

#%%
"""
agrega datos a un archivo csv en forma de diccionario si este existe,
sino crea un archivo
"""

import csv
 
DATOS = [#["NOMBRE", "APELLIDO", "GRADO"],
          ['Alex', 'Brian', 8],
          ['Tom', 'Smith', 9]]

while True:
    nombre=input("Escriba el nombre del archivo: ")
    try:
        myFile = open((nombre+'.csv'), 'a')#w: escribo, r: leo, a: adiciono
        
        with myFile:
            writer = csv.writer(myFile,delimiter=';')
            writer.writerows(DATOS)
             
        print("Escritura completada")
        break
        
    except:
        a=input("""No se pudo realizar la escritura del archivo\n
              Desea volver a intentar?
              """)
              
        if a=="s":
            pass
        else:
            break
