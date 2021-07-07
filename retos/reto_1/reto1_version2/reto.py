# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:00:01 2021

@author: Digital
"""

from vector import vector
import random
#import math


#INICIE COMPLETANDO LA FUNCIÓN SOLUCIÓN
def solucion():
    """Completa la siguiente línea para generar un número entero aleatorio 
    entre 15 y 30.
    Sugerencia, usa random.randint"""
    a = random.randint(15,30)
    print(a)
    
    """Creación del objeto vector con tamaño a"""
    v = vector(a)
    
    """Llenar el vector con números enteros aleatorios entre 1 y 9999.
    Recuerde que en el curso se definió que se debe llenar desde 
    la posición 1 en adelante, pues la posición cero guarda el número
    de casillas ocupadas en el vector con números diferentes de cero"""
    for i in range(1, a+1):
        
        """Completa el llenado de cada casilla, el número debe ser entero y 
        aleatorio entre 1 y 9999.
        Sugerencia, usa random.randint"""
        v.V[i] = random.randint(1,9999)
        
        """Como el número es aleatorio entre 1 y 9999, habrá UNA (1) nueva casilla
        ocupada, por lo tanto, se debe ir alterando en UNO (1) la posición 0 del vector
        cada vez que se llene una casilla"""
        v.V[0] += 1

    #Vamos a completar la función es_primo, (línea 53)
    
    #SIGAMOS COMPLETANDO LA FUNCIÓN SOLUCIÓN
    """Creamos una variable s, donde guardaremos la suma de los números 
    que son primos o que comienzan por dígito impar"""
    s = 0
    
    """Recorramos todas las casilla del vector (Desde la posición 1)
    Complete los límites de la función range:"""
    for i in range(1,v.V[0]+1):
        
        """Si el número guardado en la posición i es primo o comienza por dígito impar
        SÚMELO a la variable s
        Complete el siguiente condicional, para que sume solo los números primos
        o números que empiecen por dígito impar:"""
        if es_primo(v.V[i]) or comienza_digito_impar(v.V[i]):
            s += v.V[i]
            
    #El ejercicio ha terminado, presiona en evaluar :D
    return v, s

def es_primo(n):
    """
    Esta función retorna True si el número n es primo
    Retorna False si el número n NO es primo
    
    -Un número primo es un número que SOLO es divisible por él mismo y el 1.
    Ejemplos: 2, 3, 5, 7, 11, 13, y el 17 son números primos.
    
    -Un número k es divisible por d si k módulo d es cero: k % d == 0
    Ejemplos:8 es divisible por 4, 9 es divisible por 3, 27 es divisible por 3.
    
    Comprobemos si el número n es un número primo, para ello se hará lo siguiente:
        Probar si n es divisible por un número entre 2 y n-1.
        En caso de que NO haya ningún número tal que n sea divisible por él, retornamos True (Sí es primo), pero si hay 
        al menos UN número en ese intervalo que divida a n, retornamos False (No es primo)
    Complete los límites del ciclo (los límites en la función range)"""
    for d in range(2,n):
        
        """Complete cuál es la condición que se debe cumplir para que un número NO sea primo
        Ayuda: si n es divisible por d, entonces n NO es primo"""
        if n%d==0:
            """Si entra a este condicional, es porque hay un número que divide a n, por tanto NO es primo"""
            return False
            
    #Si logra salir de este ciclo, es porque no hayó ningún número que divida a n, por tanto SÍ es primo
    #Vamos a completar la función comienza_digito_impar, (línea 83)
    return True
    

def comienza_digito_impar(n):
    """Esta función retorna True si n comienza por un dígito impar, ejemplo de números que
    comienzan por dígito impar: 1234, 76555, 92228
    Retorna False si n NO comienza por dígito impar
    
    Complete la siguiente línea, que sirve para guardar el primer dígito de n en una variable llamada d"""
    d = str(n)[0]
    
    """d guarda un valor de tipo texto, completa la siguiente línea para cambiar el tipo de la variable d a entero"""
    d = int(d )
    
    """Un número d es impar si d % 2 == 1
    Complete cuál es la condición que se debe cumplir para que un número SÍ sea impar"""
    if d % 2 == 1:
    
        """Si entra a este condicional, es porque n empieza por un dígito impar"""
        return True
        
    """Si NO entra al condicional anterior, es porque n NO empieza por un dígito impar"""
    #Vamos a seguir completando la función solución, (línea 34)
    return False
    
solucion()
print(solucion())