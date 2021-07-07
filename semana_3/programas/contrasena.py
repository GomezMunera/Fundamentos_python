# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 10:52:39 2021

@author: Digital
"""

def verificar_contrasena(s):
    tiene_mayusculas = False
    tiene_minusculas = False
    tiene_numeros = False
    
    for ver in s:
        if ver >= "A" and ver <= "Z":
            tiene_mayusculas = True
        elif ver >= "a" and ver <= "z":
            tiene_minusculas = True
        elif ver >= "0" and ver <= "9":
            tiene_numeros = True
            
        # mirar si cumple las 4 propiedades
    if (len(s) >= 8 and tiene_mayusculas and tiene_minusculas 
        and tiene_numeros):
        return True
    return False