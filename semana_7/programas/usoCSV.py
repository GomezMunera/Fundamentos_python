# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:01:33 2021

@author: alejo
"""

#%%
#pip install tabulate
from tabulate import tabulate

tabla = [["Sol",696000,1989100000],
         ["Tierra",6371,5973.6],
         ["Luna",1737,73.5],
         ["Marte",3390,641.85]]

print(tabla)
print(tabulate(tabla))

#%%

diccionario = {"Nombre": ["Alice", "Bob"], 
               "Edad": [24, 19]}

print(tabulate(diccionario, headers="keys"))

#%%
import csv
from tabulate import tabulate

with open('VentasCSV.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')    
    # print(reader)
    print(tabulate(reader))

#%%
#Imprimir el archivo

import csv
with open('VentasCSV.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')#, quotechar='\n')
    for row in spamreader:
        for j in range(len(row)):
            print(row[j],end=" ")
        print()
        

#%%
#Imprimir por filas

with open("VentasCSV.csv") as f:
    reader = csv.reader(f)
    print(next(reader)[0])
    

#%%
# imprimir por columnas

import csv
with open('VentasCSV.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')#, quotechar='\n')
    for row in spamreader:
        #print(row[8])
        for j in range(len(row)):
            print(row[j],end=" ")
        print()

#%%

import csv

with open('VentasCSV.csv') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=';')
    a=0
    for row in reader:
        
        print(row["Febrero"])
        a+=float(row["Febrero"])  
        # print(row)
        # print()
        
    print(f"Ventas de Febrero: {a}")
    
#%%

import csv

with open('VentasCSV.csv') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=';')

    suma=0
    for row in reader:
        for llave in row:
            # print(row[llave])
            
            if llave != "Producto" and llave !="Costo Unidad":
                suma+=float(row[llave])
                print(row[llave], end=" ")
                
        print(f"""nTotal productos {row["Producto"]}: """,suma)
        suma=0
        #print(row)
        print()



#%%

with open('VentasCSV.csv') as file:
    data = {}
    for row in csv.DictReader(file,delimiter=';'):
        for key, value in row.items():
            if key not in data:
                data[key] = []
            data[key].append(value)

#%%

import csv
 
with open('Estudiantes.csv', 'w') as csvfile:
    campos = ['NOMBRE', 'APELLIDO', 'GRADO']
    writer = csv.DictWriter(csvfile, fieldnames=campos, delimiter=';')
 
    writer.writeheader()
    writer.writerow({'GRADO': 'B', 'NOMBRE': 'Alex', 'APELLIDO': 'Brian'})
    
    writer.writerow({'GRADO': 'A',
                     'NOMBRE': 'Rachael',
                     'APELLIDO': 'Rodriguez'})
    
    writer.writerow({'GRADO': 'B', 'NOMBRE': 'Jane', 'APELLIDO': 'Oscar'})
    writer.writerow({'GRADO': 'B', 'NOMBRE': 'Jane', 'APELLIDO': 'Loive'})
 
print("Archivo Guardado")

#%%
with open("Estudiantes.csv") as f:
    reader = csv.reader(f,  delimiter=';')
    print(tabulate(reader))

#%%

import csv
 
with open('Estudiantes.csv', 'w') as csvfile:
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

    

