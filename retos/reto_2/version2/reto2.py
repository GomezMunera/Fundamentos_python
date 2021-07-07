# -*- coding: utf-8 -*-
"""
reto 2 variante 2
"""

from math import sqrt
import numpy as np
#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""



#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 
def iniciar_matriz(n):
    mat = []
    for i in range(n):
        a = [0] * (n)
        mat.append(a)
    return mat


def llenar_matriz(mat,a,n):
    for i in range(n):
        in_menor = int((i*(i+1))/2)
        in_mayor = int((i*(i+3))/2)
        t = in_mayor - in_menor + 1
        mat[i][0:t] = a[in_menor:in_mayor + 1]
        
            

"""Fin espacio para programar funciones propias"""

def solucion(a):
    """
    En esta función deberás programar tu solución.
    Explicación del parámetro que recibe:
    - a: Es un vector unidimensionalde numpy, (No te preocupes si NO conoces numpy,
        el manejo que debes darle es IGUAL al de una lista de Python)
        El largo de la lista lo puedes calcular así: L = len(a)
        Para indexar el elemento en la posición i se hace así (Igual como una lista):
            a[i] 
            
    Explicación de lo que debe retornar:
    -matriz: Puede ser de dos tipos (COMO TE SIENTAS MÁS CÓMODO)
        Una matriz de numpy O una lista de listas (El calificador está en las condiciones
        para recibit cualquiera de los dos tipos), en esta matriz debes guardar los
        elementos que hay en el vector a como se especifica en el enunciado
    """
    
    L = len(a)
    
    # saca la raíz positiva
    n = int((- 1 + sqrt(1 - 4*(-2*L))) / 2)
    
    matriz = iniciar_matriz(n)
    
    llenar_matriz(matriz,a,n)
    
    return matriz
    
"""
Estas líneas de código que siguen, permiten probar si su ejercicio es correcto
"""
#NO MODIFICAR
l = [8, 60, 72, 35, 26, 75, 15, 12, 33, 54]
matriz_correcta = np.array([[ 8.,  0.,  0.,  0.], [60., 72.,  0.,  0.], [35., 26., 75.,  0.], [15., 12., 33., 54.]])
matriz_estudiante = np.array(solucion(l)).astype(float)
print("LISTA ENTREGADA:\n", l,"\n")
print("===SALIDA ESPERADA===\nMatriz:\n", matriz_correcta,"\n")
print("===TU SALIDA===\nMatriz:\n", matriz_estudiante,"\n")