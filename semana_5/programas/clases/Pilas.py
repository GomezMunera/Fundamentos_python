# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:20:42 2021

@author: Digital
"""

""" Pilas """
from vector import vector
from LSL import LSL
# In[]
"""
Pilas con funciones
"""
def funcion1():
    print("Ingreso por el método 1")
    x = 5 + funcion2()
    return x
    
def funcion2():
    print("Ingreso por el método 2")
    x = 3 + funcion3()
    return x

def funcion3():
    print("Ingreso por el método 3")
    x = 7
    return x
    
x = funcion1()
print(x)

# In[]
"""
Recursión
"""
def factorial(n):
    if (n == 0):
        return 1
    else:
        return n*factorial(n-1)
    
factorial(5)

# In[]
"""
Pilas con listas
"""
stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)

print("\nElementos apilados en la pila")
print(stack.pop())
print("\nDespués de eliminar los elementos")
print(stack)

# In[]
"""
Clase Pila
"""
class Pila:
    def __init__(self):
        self.arreglo=[]
    def apilar(self, x):
        self.arreglo.append(x)
    def desapilar(self):
        try:
            return self.arreglo.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
    def es_vacia(self):
        return self.arreglo == []
    def muestraPila(self):
        for i in self.arreglo:   
            print(i, end="| ")   
        print()
        
# In[]
# prueba
p = Pila()
print("Es vacia?",p.es_vacia())
p.apilar("hola")
print("Es vacia?",p.es_vacia())
p.muestraPila()
p.apilar(6)
p.apilar("+")
p.apilar(7)
p.muestraPila()
p.desapilar()
p.muestraPila()

# In[]
"""
clase pila con vector
"""
class pilaVector(vector):
     def __init__(self, n):
         vector.__init__(self, n)
     
     def apilar(self, d):
        self.agregarDato(d)
        
     def muestraPila(self):
         self.imprimeVector()
         
     def desapilar(self):
         if self.V[0] == 0:
             print("Pila vacía")
             return None
         d = self.V[self.V[0]]
         self.V[0] = self.V[0] - 1
         return d

st = pilaVector(10)
st.apilar("a")
st.apilar("b")
st.apilar(316)
st.muestraPila()
d = st.desapilar()
print(d)
st.muestraPila()

# In[]
"""
clase Pila con Lsl

"""
class pila(LSL):
     def __init__(self):
         LSL.__init__(self)
     def apilar(self, d):
         y = self.buscarDondeInsertar(d)
         self.insertar(d,y)
     def muestraPila(self):
         self.recorrerLista()
     def desapilar(self):
         p = self.primerNodo()
         d = p.retornarDato()
         self.borrar(p)
         return d
    
a = pila()
a.apilar("a")
a.apilar("e")
a.apilar("i")
a.apilar("o")
a.recorrerLista()
b = a.esVacia()
print("\n Está vacía?", b)
d = a.desapilar()
print("\ndato desapilado", d)
a.recorrerLista()