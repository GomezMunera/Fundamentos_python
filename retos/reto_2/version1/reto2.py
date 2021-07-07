# -*- coding: utf-8 -*-
"""
reto 2 variante 1
"""

import numpy as np
#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""



#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 

def menorV(V,n):
    menor = V[0][0]
    pos = []
    for i in range(n):
        for j in range(n):
           if V[i,j] <= menor:
              menor = V[i,j]
    
    for i in range(n):
        for j in range(n):
            if (i+j < n ) and ((i+j)%2 != 0) and V[i,j] == menor:
                pos.append((i,j))
    
    return menor, pos

def matrizbuscada(A,n):
    for i in range(n):
        for j in range(n):
            if(i+j > n - 1) or ((i+j)%2 != 1):
                A[i,j] = 0
            """if ((i+j)%2 != 1):
                A[i,j] = 0"""
            

"""Fin espacio para programar funciones propias"""

def solucion(A):
    """
    En esta función deberás programar tu solución.
    Explicación del parámetro que recibe:
    - A: Es una matriz cuadrada de números enteros aleatoria (NO TE DEBES PREOCUPAR POR LLENARLA, YA LO ESTÁ), 
        para indexar un elemento en la fila i, columna j se hace así:
        A[i,j] o A[i][j], como te sientas más cómod@.
        El orden de la matriz lo puedes calcular así: n = A.shape[0]
        
    Explicación de lo que debe retornar:
    -valor_minimo: Es el valor mínimo (Número más pequeño) ubicado en las casillas
        descritas en el enunciado, es de tipo float o entero (Elige el tipo que quieras)
    -posiciones_valor_minimo: Es una lista de Python que contiene la posición o las 
        posiciones donde se encuentra el valor mínimo determinado, 
        ¡Cada posición debe ser una tupla!
    """
    
    n = A.shape[0]
    
    """
    volver Vector
    """
    vector = menorV(A,n)
    
    valor_minimo = vector[0]
    
    posiciones_valor_minimo = vector[1]
    
    
    return valor_minimo, posiciones_valor_minimo
    
"""
Estas líneas de código que siguen, permiten probar si su ejercicio es correcto
"""
#NO MODIFICAR
matriz_entrada = np.array([[89, 13, 23, 72],
       [29, 11, 81, 62],
       [27, 26, 88, 33],
       [ 5, 78, 11, 11]])
menor_estudiante = solucion(matriz_entrada)[0]
posiciones_menor_estudiante = solucion(matriz_entrada)[1]
print("MATRIZ ENTREGADA:\n", matriz_entrada,"\n")
print("===SALIDA ESPERADA===\nMenor = ", 5,"\nPosiciones donde está el menor = ", [(3, 0)],"\n")
print("===TU SALIDA===:\nMenor = ", menor_estudiante,"\nPosiciones donde está el menor = ", posiciones_menor_estudiante,"\n")
if menor_estudiante == 5 and  set(posiciones_menor_estudiante) == set([(3, 0)]):
    print("Todo se ve correcto, ¡Procede a calificar tu código!")
else:
    print("Las salidas no coinciden, ¡Estás olvidando algo en tu código!")