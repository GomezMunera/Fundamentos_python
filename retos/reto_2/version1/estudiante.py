
"""
reto 2 variante 1
"""

import numpy as np
#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""



#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 
posiciones_valor_minimo = list()
def anadir_elemento(s,d):
    s.append(d)
    return s
            

"""Fin espacio para programar funciones propias"""

def solucion(A):
    
    valor_minimo = A[0][0]
    fila = len(A)
    
    del posiciones_valor_minimo[:]
    
    for i in range(fila):
            for j in range(fila):
                if A[i][j] < valor_minimo:
                    valor_minimo = A[i][j]
                    del posiciones_valor_minimo[:]
                    anadir_elemento(posiciones_valor_minimo, (i,j))
                elif(A[i][j]== valor_minimo):
                    anadir_elemento(posiciones_valor_minimo, (i,j))
                    
        
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
        
    
    return valor_minimo, posiciones_valor_minimo
    
"""
Estas líneas de código que siguen, permiten probar si su ejercicio es correcto
"""
#NO MODIFICAR
matriz_entrada = np.array([[89, 5, 23, 72],
       [51, 5, 81, 62],
       [27, 26, 88, 33],
       [ 5, 78, 11, 5]])
menor_estudiante = solucion(matriz_entrada)[0]
posiciones_menor_estudiante = solucion(matriz_entrada)[1]
print("MATRIZ ENTREGADA:\n", matriz_entrada,"\n")
print("===SALIDA ESPERADA===\nMenor = ", 5,"\nPosiciones donde está el menor = ", [(3, 0)],"\n")
print("===TU SALIDA===:\nMenor = ", menor_estudiante,"\nPosiciones donde está el menor = ", posiciones_menor_estudiante,"\n")
if menor_estudiante == 5 and  set(posiciones_menor_estudiante) == set([(3, 0)]):
    print("Todo se ve correcto, ¡Procede a calificar tu código!")
else:
    print("Las salidas no coinciden, ¡Estás olvidando algo en tu código!")