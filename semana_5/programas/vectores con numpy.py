import numpy as np


lista=[25,12,15,66,12.5]
vector=np.array(lista)
print(vector)

print("- vector original")
print(vector)

print()
print("- sumarle 1 a cada elemento del vector:")
print(vector+1)

print()
print("- multiplicar por 5 cada elemento del vector:")
print(vector*5)

print()
print("- suma de los elementos:")
print(np.sum(vector))

print()
print("- promedio (media) de los elementos:")
print(np.mean(vector)) # 

print()
print("- el vector sumado a si mismo:")
print(vector+vector)

print()
print("- suma de vectores vector1 y vector2 (mismo tamaño):")
vector2=np.array([11,55,1.2,7.4,-8])
print(vector+vector2)

print()
print("Elemento 3 del vector")

print()
print(vector[3])

print()
print("Elementos del 1 al 3 del vector")
print(vector[1:4])

print()
print("Elementos del 1 al final")
print(vector[1:])

print()
print("Elementos desde el principio hasta 3")
print(vector[:4])

print()
print("Todos los elementos del vector")
print(vector[:])


