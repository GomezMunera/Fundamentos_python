# -*- coding: utf-8 -*-
"""
Created on Mon May 31 20:45:00 2021

@author: Digital
"""

def transmitir_mensaje(msg):
    "Esta es la funcion de closure"
    print("mensaje afuera: ")
    def transmisor_datos():
        "La funcion anidada"
        print(msg)

    transmisor_datos()

print(transmitir_mensaje("Hola, Juan."))