# -*- coding: utf-8 -*-
"""
Created on Sat May 29 08:43:27 2021

@author: Digital
"""

# constantes

BEBE = 0
NINO =  10000
ADULTO = 20000
ABUELO = 12000

# controlador
controlador = "t"

# acumulador
costo = 0

# contador
contar = 0

mensaje = input("Ingrese la edad (para terminar darle t): ")


while mensaje != controlador:
    edad = int(mensaje)
    if edad >= 0:
        if (edad <= 2):
            costo = costo + BEBE 
        elif (edad >= 3 and edad <= 12):
            costo = costo + NINO
        elif (edad >= 65):
            costo = costo + ABUELO
        elif (edad >= 13 and edad <= 64):
            costo = costo + ADULTO
        
        contar = contar + 1
    elif (edad < 0):
        print("Edad no valida")
    
    mensaje = input("Ingrese la edad (para terminar darle t): ")
        
    
promedio = costo/contar
#print("El costo total es {}, con un promedio de {}".format(costo,promedio))
print("El costo total es %.2f, con un promedio de %.2f"%(costo,promedio))
    