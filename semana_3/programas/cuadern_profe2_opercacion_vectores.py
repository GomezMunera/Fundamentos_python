# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 19:07:25 2021

@author: Digital
"""

# In[]
import random

def construyeVector(V, n, rango):
    V[0] = n
    for i in range(1, n + 1):
        V[i] = random.randint(1, rango)


def imprimeVector(V, mensaje = "vector sin nombre: \t"):
    print("\n", mensaje, end=" ")
    m = V[0] + 1
    for i in range(1, m):
        print(V[i], end = ", ")
    print()

def agregarDato(d, V, n):
    if esLleno(V, n):
       return
    V[0] = V[0] + 1
    V[V[0]] = d

def intercambie(V, a, b):
    aux = V[a]
    V[a] = V[b]
    V[b] = aux

def sumaVector(V):
     n = V[0] + 1
     s = 0
     for i in range(1, n):
        s = s + V[i]
     return s

def mayorDato(V):
     mayor = 1
     for i in range(2, V[0] + 1):
         if V[i] > V[mayor]:
             mayor = i
     return mayor

def menorDato(V):
     menor = 1
     for i in range(2, V[0] + 1):
         if V[i] < V[menor]:
              menor = i
     return menor

def insertarDato(d, i, V, n):
    if esLleno(V, n):
          return
    for j in range(V[0], i - 1, -1):
         V[j + 1] = V[j]
    V[i] = d
    V[0] = V[0] + 1

def borrarDatoEnPosicion(i, V):
    for j in range(i, V[0]):
        V[j] = V[j + 1]
    V[0] = V[0] - 1

def borrarDato(d, V):
     i = buscarDato(d, V)
     if i != -1:
         borrarDatoEnPosicion(i, V)

def buscarDato(d, V):
     i = 1
     while i <= V[0] and V[i] != d:
          i = i + 1
     if i <= V[0]:
         return i
     return -1

def esLleno(V, n):
    if V[0] == n:
          return True
    return False

def esVacio(V):
     if V[0] == 0:
          return True
     return False

def ordenaAscen(V):
    nn = V[0] + 1
    for i in range(1, V[0]):
         k = i
         for j in range(i + 1, nn):
               if V[j] < V[k]:
                  k = j
    intercambie(V, i, k)
    
# In[]
tamagno = 30
vec1 = [0] * (tamagno + 1)
construyeVector(vec1, 16, 99)
imprimeVector(vec1, "vector vec1:\t")
agregarDato(69, vec1, tamagno)
imprimeVector(vec1, "vector vec1 después de agregar dato:\t")
mayor = mayorDato(vec1)
menor = menorDato(vec1)
print("\n el mayor está en la posición", mayor, " y es", vec1[mayor], end = " ")
print("y el menor está en la posición", menor, "y es", vec1[menor])
intercambie(vec1, mayor, menor)
imprimeVector(vec1, "vector vec1 después de intercambiar mayor con menor")

tamagno = 100
vec2 = [0] * (tamagno + 1)
construyeVector(vec2, 26, 999)
imprimeVector(vec2, "vector vec2")
insertarDato(69, 2, vec2, tamagno)
imprimeVector(vec2, "vector vec2 después de insertar dato\t")
ordenaAscen(vec2)
imprimeVector(vec2, "vector vec2 después de ordenarlo")