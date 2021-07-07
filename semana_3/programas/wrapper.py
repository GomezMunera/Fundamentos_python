# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:14:32 2021

@author: Digital
"""

def decorador(funcion):
    print('Soy el decorador()')
    def wrapper():
        print('Soy el wrapper()')
        return funcion()
    return wrapper

@decorador
def funcion_decorada():
    print('Soy la funcion_decorada()')

funcion_decorada()