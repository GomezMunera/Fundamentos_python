# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:12:15 2021

@author: Digital
"""

def closure(parametro1):
    def funcion(parametro2):
        print(parametro1 + parametro2)
    return funcion

foo = closure(10) # foo ahora es la funcion interna del closure
print(foo(200)) # Imprime: 210
print(foo(500)) # Imprime: 510