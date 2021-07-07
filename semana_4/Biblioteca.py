# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:12:29 2021

@author: Digital
"""

class Biblioteca():
    def __init__(self, cantidad,nombre):
        self.cantidad  = cantidad
        self.nombre = nombre

micoleccion=Biblioteca(300,"mi colección")
print(micoleccion)