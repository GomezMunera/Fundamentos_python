# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 08:43:34 2021

@author: Digital
"""

# funcion para manejar el acierto
def acierto(numero_sugerido,numero_ingresado,cont_intentos):
    # condicional para verificar
    if numero_ingresado == numero_sugerido:
        print("Muy bien, adivinaste el número en {} intentos".format(cont_intentos))
    else:
        print("Lo siento, no adivinaste el número en {} intentos".format(cont_intentos))
        print("El número que necesitabas encontrar es %.i"%numero_sugerido)