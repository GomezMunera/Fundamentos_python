# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 08:28:06 2021

@author: Digital
"""

# Vamos a crear una función que reduzca el número de intentos y muestre
# el mensaje al usuario para volver a ingresar el dato
def errado(cont_intentos, intentos,numero_sugerido,numero_ingresado):
    # vemos si tiene chances todavia
    # inicia con el false la bandera
    terminar = False
    if cont_intentos == intentos:
        terminar = True
    elif(numero_sugerido < numero_ingresado): 
        print("El número ingresado es mayor que el número a buscar")
    else:
        print("El número ingresado es menor que el número a buscar")
        
    
    # aumentamos el contador
    cont_intentos += 1
    
    # mensaje para volver a preguntar
    numero_ingresado = int(input("Intente de nuevo: "))
    
    return cont_intentos, numero_ingresado, terminar
    