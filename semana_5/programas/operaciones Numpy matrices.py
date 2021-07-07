
import numpy

#creación de las matrices

x = numpy.array([[10, 8], [9, 10]])
y = numpy.array([[2, 4], [3, 2]])

print ("Suma elemento a elemento de las matrices: ")
print (numpy.add(x,y))

print()
print ("Resta elemento a elemento las matrices: ")
print (numpy.subtract(x,y))

print()
print ("División elemento a elemento de la matriz : ")
print (numpy.divide(x,y))

print()
print ("Multiplicar elemento a elemento: ")
print (numpy.multiply(x,y))

print()
print ("Multiplicación de matrices : ")
print (numpy.dot(x,y))

print()
print ("Se obtiene la raíz de cada elemento de la matriz : ")
print (numpy.sqrt(x))

print()
print ("Obtiene la suma de todos los elementos: ")
print (numpy.sum(y))

print()
print ("Suma de los elementos de  cada columna : ")
print (numpy.sum(y,axis=0))

print()
print ("Suma de los elementos de cada fila: ")
print (numpy.sum(y,axis=1))

print()
print ("Calculo de la matriz traspuesta: ")
print (x.T)

print()
matriz_aleatoria=numpy.random.rand(2,2)*100
print("Matriz aleatoria",  matriz_aleatoria, sep="\n")

matriz=numpy.array([[0,1,2,3,4],
                    [5,6,7,8,9],
                    [10,11,12,13,14],
                    [15,16,17,18,19]                
                    ])
print(matriz)

print()
print("Elemento 2,2 : \n",matriz[2,2])

print()
print("Dos primeras columnas: \n",matriz[:,0:2])

print()
print("Dos primeras filas: \n",matriz[0:2,:])

print()
print("las dos ultimas filas y columnas: \n",matriz[-2:,-2:])

print()
print("las dos primeras filas y columnas: \n",matriz[:2,:2])

print()
print("Imprimir en orden inverso: \n",matriz[::-1,::-1])

print()
print("Imprimir las ultimas dos filas: \n",matriz[2::])

print()
print("Imprimir las primeras tres filas en orden inverso: \n",matriz[2::-1])


