# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:12:28 2021

@author: Digital
"""
import random

# In[]
# Crear vector
def crearVector(tamano):
    vector=[0]*(tamano+1)
    return vector

# In[]
def construyeVector(V, n, rango):
  V[0] = n
  for i in range(1, n + 1):
    V[i] = random.randint(1, rango)

# In[]
# Verificar si el arreglo esta lleno o no
def esLleno(V, nt):
    if V[0] == nt:
        return True
    return False


# In[]
# agrega un dato si tiene espacio
def agregarDato(d, V, nt):
    if esLleno(V, nt):
        return
    V[0] = V[0] + 1
    V[V[0]] = d


# In[]
# insertar dato en posicion

def insertarDato(d, i, V, nt):
    if esLleno(V, nt):
        return    
    for j in range(V[0], i - 1, -1):
        V[j + 1] = V[j]
    V[i] = d
    V[0] = V[0] + 1

# In[]
# imprimir vector
def imprimeVector(V, mensaje = "vector sin nombre: \t"):
  print("\n", mensaje, end=" ")
  m = V[0] + 1
  for i in range(1, m):
    print(V[i], end = ", ")
  print()

# In[]
def mayorDato(V):
    mayor = 1
    for i in range(2, V[0] + 1):
       if V[i] > V[mayor]:
          mayor = i
    return mayor

# In[]
# entrega un vector si tienen varios mayores
""" 
def mayorDatoV(V):
    mayor = 1
    pos = []
    for i in range(2, V[0] + 1):
       if V[i] >= V[mayor]:
          mayor = i
          pos.append(i)
    return pos
"""
# In[]
def menorDato(V):
     menor = 1
     for i in range(2, V[0] + 1):
         if V[i] < V[menor]:
              menor = i
     return menor

# In[]
def intercambiar(V, i, j):
    aux = V[i]
    V[i] = V[j]
    V[j] = aux
    
# In[]
# Exclusivo de python swap
"""
def intercambiar2(V, i, j):
    V[i], V[j] = V[j], V[i]
"""

# In[]
def buscarDato(d, V):
    i = 1
    while i <= V[0] and V[i] != d:
        i = i + 1
    if i <= V[0]:
        return i
    return -1


# In[]
#  tiene que estar el valor de datos en la posición [0]
def ordenaAscen(V):
    for i in range(1, V[0]):
        k = i
        for j in range(i+1, V[0] + 1):
            if V[j] < V[k]:
                k = j
        intercambiar(V, i, k)
        #print(V)

             
# In[]
def burbuja(V):
    for i in range(1, V[0]):
        for j in range(1, V[0] - i + 1):
            if V[j] > V[j+1]:
                intercambiar(V, j, j+1)
        print(V)
             
# In[]
# modificando el primero
"""
def bubbleSort2(v):
 for i in range(0, len(v)-1):
     for j in range(0, (len(v)-1)-i):
         if v[j] > v[j + 1]:
             intercambiar(v, j, j + 1)
"""

# In[]
# Método de inserción
def insercion(V):
    for i in range(2, V[0]+1):
        d = V[i]
        j = i - 1
        while j > 0 and V[j] > d:
            V[j+1] = V[j]
            j = j - 1
        V[j+1] = d
# In[]
"""
def busBinaria(arreglo, d):
 inicio = 0
 fin = len(arreglo)-1
 while inicio <= fin:
     mitad = (inicio + fin) // 2
     if arreglo[mitad] == d:
         return mitad
     if d < arreglo[mitad]:
         fin = mitad - 1
     else:
         inicio = mitad + 1
 return -1

arreglo = [10,20,30,40,50]
print(busBinaria(arreglo,20))
"""

# In[]
# El vector de entrada debe estar organizado acendentemente
def busbin(V, d):
    inicio = 1
    fin = V[0]
    while inicio <= fin:
        mitad = (inicio + fin) // 2
        if V[mitad] == d:
            return mitad
        if d < V[mitad]:
            fin = mitad - 1
        else:
             inicio = mitad + 1
    return -1

# In[]
# operaciones con vector
def sumaVector(V):
  n = V[0] + 1
  s = 0
  for i in range(1, n):
    s = s + V[i]
  return s


# In[]
# Borrar un dato indicando la posición
def borrarDatoEnPosicion(i, V):
    if i == V[0]:
        V[i] = 0
    else:
        for j in range(i, V[0]):
            V[j] = V[j + 1]
        V[j+1] = 0
    V[0] = V[0] - 1


# In[]
def borrarDato(d, V):
  i = buscarDato(d,V)
  if i != -1:
    borrarDatoEnPosicion(i, V)
 
# In[]    
def invertir(vec, n):
    lista = [0]*n
    for i in range(1,n+1):
        lista[i-1] = vec[i]
    print(lista)
    vec[1:n+1] = lista[::-1]

# In[]
# Ejemplo

#Crear un vector de tamaño 6 y Luego:
"""
   1. Inicialice 3 elementos con numeros aleatorios entre 1 y 99.
   2. Muestre el vector
   3. Agregue un dato con valor de 69
   4. Imprima nuevamente el vector
   5. Obtenga la ubicación del mayor dato del vector.
   6. Obtenga la ubicación del menor dato del vector.
   7. Imprima un mensaje con las ubicacion del dato mayor y su valor.
   8. Imprima un mensaje con las ubicacion del dato menor y su valor.
   9. Intercambie los elementos mayor y menor.
  10. Imprima nuevamente el vector
  11. Ordenar el vector en orden ascendente
  12. Imprima nuevamente el vector
  13. copie el vector en otro e inviertalo
  14. imprima el nuevo vector
"""
