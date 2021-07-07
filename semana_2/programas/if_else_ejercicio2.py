# -*- coding: utf-8 -*-
"""
Created on Fri May 28 20:56:25 2021

@author: Digital
"""

# verificar si es par

numero = input("Ingrese el número: ")

if numero.isdigit():
    numero = int(numero)
    if numero%2 == 0:
        print("Número par")
    else:
            print("Número impar")
else:
    print("Es un caracter")
    
print("Programa finalizado correctamente")