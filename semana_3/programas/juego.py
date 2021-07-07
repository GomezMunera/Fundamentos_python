# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 08:18:22 2021

@author: Digital
"""

# In[]
# uso de random
# cree un juego que busque adivinar un número cargado al azar

import random
from errado import errado
from acierto import acierto

# cantidad de intentos
intentos = 4

# mensaje de bienvenida al juego
print(f"Bienvenido al juego de adivina el número del 0 al 10, cuenta con {intentos} intentos")

# inicia el número sugerido
numero_sugerido = random.randint(0, 10)

# contador de intentos
cont_intentos = 1

# mensaje para que e usuario ingrese el primer número
numero_ingresado = int(input("Ingrese un número entero del 0 al 10: "))

# Bandera para terminar
terminar = False

#print(numero_sugerido)

# ciclo para mirar el número de intentos
while numero_ingresado != numero_sugerido and not terminar:
    print("Lo siento, el número ingresado no corresponde")
    
    # hacer el llamado a la funcion errado
    retorno = errado(cont_intentos,intentos,numero_sugerido, numero_ingresado)
    cont_intentos = retorno[0]
    numero_ingresado = retorno[1]
    terminar = retorno[2]
 #   print(retorno)

acierto(numero_sugerido,numero_ingresado,cont_intentos)
print("Fin de juego")