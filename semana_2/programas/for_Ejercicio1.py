# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:41:40 2021

@author: Digital
"""

# Ejercicio del palindromo

# lectura del usuario
mensaje = input("Entre la palabra: ")

# elimina los espacios en blanco
mensaje = mensaje.replace(" ","")

# bandera
palindromo = True

for i in range(0,len(mensaje)//2):
    if mensaje[i] != mensaje[len(mensaje) - i - 1]:
        palindromo = False
        
# mostrar el resultado
if palindromo:
    print("La palabra es palindromo")
else:
    print("La palabra no es palindromo")