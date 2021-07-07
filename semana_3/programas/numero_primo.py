# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 10:37:23 2021

@author: Digital
"""

# verificación de número primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def main():
    value = int(input("Ingrese un entero: "))
    if es_primo(value):
        print(value,"es primo")
    else:
        print(value,"no es primo")
        
if __name__ == "__main__":
    main()