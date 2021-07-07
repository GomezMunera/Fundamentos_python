# -*- coding: utf-8 -*-
"""
Created on Sat May 29 08:11:05 2021

@author: Digital
"""

# sumatoria desde 0 hasta n

n = int(input("Ingresar un número entero positivo: "))

# variable controladora
conteo = 0

# variable acumuladora
suma = 0

while conteo <= n:
    if n > 0:
        suma = suma + conteo
        conteo = conteo + 1
    else:
        print("El número debe ser positivo")
        
print("La sumatoria es: {}".format(suma))
    

