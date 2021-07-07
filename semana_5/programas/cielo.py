# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:08:21 2021

@author: alejo
"""

import random
estrella="\u2605"


m = int(input("ingrese filas: "))
n = int(input("ingrese columnas: "))

M = []
for i in range(n):
    M.append([" "]*m)

## Matriz construida por comprensión
#M= [ [" " for i in range(n)  ] for j in range(m)]

for i in range(m):  ## se recorren las filas
    
    for j in range(n):  ## recorro la parte interna de cada fila
        
        num=random.randint(0, 5)
        if num == 0:
            M[i][j] = estrella 
        else:
            M[i][j] = " "
            
print()
for filas in M: ## se recorren las filas

    print("      ", end="")
    for elementos in filas:  ## recorro la parte interna de cada fila
       
        print(elementos, end="  ")
    print()
    
    
    
    
    