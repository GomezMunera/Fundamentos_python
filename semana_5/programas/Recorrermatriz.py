# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 12:18:19 2021

@author: 
"""
M = [     [0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 3, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 2, 0 ],
        [0, 0, 1, 0, 0, 0, 0, 0 ], 
        [0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0 ]
   ]

filas=len(M)

columnas=len(M[1])

print("\nImprimir una matriz: \n")
for i in range(filas):
    for j in range(columnas):
        print(M[i][j], end="  ")
    print()

print("\nImprimir por columnas (Trasponer): \n")
for i in range(columnas):
    for j in range(filas):
        print(M[j][i], end="  ")
    print()
     
# import itertools
# for i,j in itertools.product(range(filas),range(columnas)):
#     print(M[i][j])    

print("\nOtra forma: \n")
for filas in M:
    for elementos in filas:
        print(elementos, end="  ")
    print()
        

    
        
        
        
        
        
        
        