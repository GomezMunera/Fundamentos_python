from lista_ligada import *

nodo1=nodoSimple("Hola, ")
nodo2=nodoSimple("¿Cómo ")
nodo3=nodoSimple("estas ")
nodo4=nodoSimple("tú?")


## Ligo el nodo 1 con el nodo 2
nodo1.asignarLiga(nodo2)
nodo2.asignarLiga(nodo3)
nodo3.asignarLiga(nodo4)


print(nodo1.dato, end="")
nuevaLiga = nodo1.liga

while nuevaLiga != None:
    
    print(nuevaLiga.dato, end="")
    
    nuevaLiga = nuevaLiga.liga

# In[]
"""
Ejemplo frutas
"""
