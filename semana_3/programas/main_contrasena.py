# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:00:45 2021

@author: Digital
"""
#from contrasena import verificar_contrasena
import contrasena

def main():
    s = input("Ingrese una contraseña: ")
    if contrasena.verificar_contrasena(s):
        print("Es una buena contraseña")
    else:
        print("No es una buena contraseña")
        
if __name__ == "__main__":
    main()