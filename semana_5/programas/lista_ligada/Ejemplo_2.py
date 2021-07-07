from lista_ligada import *


nodin=nodoSimple("A")
nodofin=nodoSimple("Z")

lista=LSL()

lista.primero=nodin
lista.ultimo=nodofin

print("Lista")
print("Dato del primer nodo: ", lista.primero.dato)
print("Dato del segundo nodo: ", lista.ultimo.dato)
print("LIGA del primer nodo: ", lista.primero.liga)
print("LIGA del segundo nodo: ", lista.ultimo.liga)


# In[]
lista_2=LSL()

lista_2.agregarDato("A")
lista_2.agregarDato("Z")

print("Lista_2")
print("Dato del primer nodo: ", lista_2.primero.dato)
print("Dato del segundo nodo: ", lista_2.ultimo.dato)

print("LIGA del primer nodo: ", lista_2.primero.liga)
print("LIGA del segundo nodo: ", lista_2.ultimo.liga)

# In[]