# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:11:35 2021

@author: alejo
"""

total=0
cant_personas=0
edad=0
precio=0

while edad != "":
    edad=input("Ingrese la edad: ")
    
    if edad != "":
        edad=int(edad)
        
        if edad<=2:
            precio=0
        elif (edad>=3) and (edad<=12):
            precio=10000
        elif (edad>12) and (edad<=65):
            precio=20000
        elif edad>65:
            precio=12000
        total = precio + total 
        cant_personas=cant_personas+1

print("El total es: ", total)
promedio=total/cant_personas
print("El promedio es: %.2f"%promedio) 


    







