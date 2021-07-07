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
with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])