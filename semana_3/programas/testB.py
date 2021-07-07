# -*- coding: utf-8 -*-
"""
Created on Mon May 31 19:54:42 2021

@author: Digital
"""

#from test import *  # tienes varias formas de hacerlo, from testA import * (esto importa todas las funciones de testA, no es recomendable ya que si tienes funciones con el mismo nombre no sabrás de dónde es cada una), o from testA import suma
#from test import suma, multi 
import test

resultado = test.suma(5, 3)  # si usaste alguna otra forma de import, puedes llamar la función directamente con resultado = suma(5, 3)
print(resultado)

resultado = test.suma(5, 5)  # si usaste alguna otra forma de import, puedes llamar la función directamente con resultado = suma(5, 3)
print(resultado)

resultado = test.multi(5, 5)  # si usaste alguna otra forma de import, puedes llamar la función directamente con resultado = suma(5, 3)
print(resultado)