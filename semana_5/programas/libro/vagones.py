# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 00:28:56 2021

@author: Digital
"""

class Nodo:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox
        
    def __str__(self):
        return str(self.dato)
    
    """def verLista(self):
        #Recorre todos los nodos a través de sus enlaces,
        #mostrando sus contenidos. 
        # cicla mientras nodo no es None
        while self.dato:
        # muestra el dato
            print(self.dato)
            self.dato = self.prox
        # ahora nodo apunt"""
        
# In[]
def verLista(nodo):
        """ Recorre todos los nodos a través de sus enlaces,
        mostrando sus contenidos. """
        # cicla mientras nodo no es None
        while nodo:
        # muestra el dato
            print(nodo)
            nodo = nodo.prox # ahora nodo apunta al próximo
        
    
# In[]
""" Probando los nodos"""
v3 = Nodo("Bananos")
v2 = Nodo("Manzanas",v3)
v1 = Nodo("Fresas", v2)

print(v1)

verLista(v1)

# In[]


# In[]
""" Desenganchar un nodo o vagón de la lista """
v1.prox=v3
verLista(v1)

# In[]
"""Lista infinita o lista circular"""
v1.prox = v2
verLista(v1)

# In[]
"""Referenciado al principo de la lista """
lista = v1
verLista(lista)

# In[]
""" Borrado del primer elemento de la lista sin perder identidad"""
lista = lista.prox
lista = lista.prox
verLista(lista)

#print(v3)