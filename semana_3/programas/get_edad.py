# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:59:18 2021

@author: Digital
"""

def get_integer_input(message):
    """
    Esta función muestra un mensaje al usuario
    solicitando que introduzca un entero.
    Si el usuario introduce algo que no es un número
    entonces la entrada es rechazada 
    y muestra un mensaje de error.
    El usuario es preguntado de nuevo."""
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('La entrada debe ser un entero')
        value_as_string = input(message)
    return int(value_as_string)
    

age = get_integer_input('Por favor ingrese su edad: ')
print('La edad es', age)

#print(get_integer_input.__doc__)