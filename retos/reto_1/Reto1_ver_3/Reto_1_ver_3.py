from vector import vector
import random
import math

"""Función que contiene la solución al problema que será calificado"""


def solucion():
    # Completa la siguiente línea para generar un número entero aleatorio entre 15 y 25.
    a = random.randint(15,25) # Sugerencia, usa random.randint

    """Creación del objeto vector con tamaño a"""
    v = vector(a)

    """Llenar el vector con números enteros aleatorios entre 1 y 99.
    Recuerde que en el curso se definió que se debe llenar desde 
    la posición 1 en adelante, pues la posición cero guarda el número
    de casillas ocupadas en el vector con números diferentes de cero"""
    for i in range(1, a + 1):
        # Completa el llenado de cada casilla, el número debe ser entero y
        # aleatorio entre 1 y 99.
        v.V[i] = random.randint(1,99)# Sugerencia, usa random.randint

        """Como el número es aleatorio entre 1 y 9999, habrá UNA (1) nueva casilla
        ocupada, por lo tanto, se debe ir alterando en UNO (1) la posición 0 del vector
        cada vez que se llene una casilla"""
        v.V[0] += 1

    """Salimos del ciclo de llenado y procedemos a crear un nuevo objeto vector con el mismo tamaño a"""
    """Creación del nuevo objeto vector con tamaño a"""
    vres = vector(a)

    """Recorramos todas las casilla del vector desde la posición inicial (1) hasta la penúltima posición (a). 
    En este caso añadimos un tercer parámetro, que indicará la diferencia entre los números del rango,
    en este caso, será de dos en dos.
    Ejemplos: recorremos range(1, 6, 1), que es la secuencia de números (1,2,3,4,5) con un valor de incremento 1, que resultará en la secuencia de números (1, 2, 3, 4 y 5)
              recorremos range(1, 6, 2), que es la secuencia de números (1,2,3,4,5) con un valor de incremento 2, que resultará en la secuencia de números (1, 3 y 5)
              recorremos range(1, 6, 4), que es la secuencia de números (1,2,3,4,5) con un valor de incremento 4, que resultará en la secuencia de números (1 y 5)
              recorremos range(1, 6, 6), que es la secuencia de números (1,2,3,4,5) con un valor de incremento 6, que resultará en la secuencia de número (1) solamente"""
   
    for i in range(1, a, 2):
        # Completa la siguiente línea para obtener el máximo común divisor de la posición actual y la posición siguiente.
        valormcd =  math.gcd(v.V[i], v.V[i + 1]) # Sugerencia, usa math.gcd

        """Almacenamos y hallamos el mínimo común múltiplo de la posición actual y la posición siguiente del vector"""
        # Vamos a completar la función mcm, (vaya a la línea 80)
        valormcm = mcm(v.V[i], v.V[i + 1])

        """Agregamos el máximo común divisor obtenido al nuevo vector con el método agregarDato"""
        agregarDato(vres, valormcd)

        """Agregamos el mínimo común múltiplo obtenido al nuevo vector con el método agregarDato"""
        agregarDato(vres, valormcm)

    """El ejercicio ha terminado, presiona en evaluar :D"""
    return v, vres


def agregarDato(vector, d):
    """ Esta función agrega un valor al vector que tiene como primer parámetro"""

    """Pregunta si el vector está lleno; si lo está, NO agregará ningún dato y 'retornará' nada"""
    if esLleno(vector):
        return

    """Como se agregará un valor 'd', habrá UNA (1) nueva casilla
    ocupada, por lo tanto, se debe ir alterando en UNO (1) la posición 0 del vector
    cada vez que se agregue un valor 'd'"""
    vector.V[0] = vector.V[0] + 1

    """Finalmente, agregamos el valor 'd' a la última posición del vector"""
    vector.V[vector.V[0]] = d


def esLleno(vector):
    """ Esta función retorna True si el vector tiene todas las casillas ocupadas
        De lo contrario, retorna False"""
    return vector.V[0] == vector.n


def mcm(x, y):
    """ Esta función retorna el valor del mínimo común múltiplo de dos números"""
    # Completa la siguiente línea para obtener el mínimo común múltiplo de dos números
    # Sugerencia, la fórmula para obtener el mínimo común múltiplo consiste en
    # multiplicar los dos números y dividirlos por su máximo común divisor
    # Ejemplo: el mcm entre 8 y 12 es 24, teniendo en cuenta que 8x12=96 y su máximo común divisor es 4.
    valor =  x*y/math.gcd(x,y) # Sugerencia, usa math.gcd
    
    return valor


"""Este procedimiento permite imprimir vectores en la consola"""


def imprimeVector(vector, mensaje="vector sin nombre: \t"):
    print("\n", mensaje, end="        ")
    for i in range(1, vector.V[0] + 1):
        print(vector.V[i], end=", ")
        if i % 30 == 0:
            print("\n                      ", end="")
    print()


"""Las siguientes líneas le permitirán probar su solución al presionar el botón de ejecutar"""


a, b = solucion()
imprimeVector(a, 'Original')
imprimeVector(b, 'Modificado')
