# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 09:42:26 2021

@author: Digital
"""

# hacer un string representar un entero
def isInteger(s):
    # quita los espacios en blanco del inicio al fin del string
    s = s.strip()
    
    # determina si los caracteres restantes forman un número entero válido
    if(s[0] == "+" or s[0] == "-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False

def main():
    s = input("Entre un String: ")
    if isInteger(s):
        print("El entero representa un String")
    else:
        print("El entero no representa un String")
        
# sólo llamar a la función principal cuando este archivo no ha sido importado
if __name__ == '__main__':
    main()

