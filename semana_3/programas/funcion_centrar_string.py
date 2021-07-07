# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 09:21:19 2021

@author: Digital
"""

# centrar un string en la terminal
WIDTH = 100

def center(s, width):
    if width < len(s):
        return s
    
    #calcula el número de espacios neccesarios para generar el resultado
    espacios = (width - len(s)) // 2
    resultado = " " * espacios + s
    
    return resultado

def main():
    print(center("Una historia famosa", WIDTH))
    print(center("Por una persona famosa", WIDTH))
    print(center("Comenzaba con:", WIDTH))
    print(center("Erase una vez ...", WIDTH))
    
main()
    