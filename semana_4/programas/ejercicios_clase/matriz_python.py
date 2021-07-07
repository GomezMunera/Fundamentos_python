
A = [[1, 5],[4,6]]
print(A)


# In[]
f = 6
c = 3
a = [0] * f
for i in range(f):
    a[i] = [0] * c
print(a)

# In[]
f = 7
c = 4
b = []
for i in range(f):
    b.append([0] * c)
print(b)

# In[]
f = int(input("Filas"))
c = int(input("Columnas"))
matriz = [[0] * c for i in range(f)]
print(matriz)

for i in range(f):
    for j in range(c):
        valor = int(input(f"Ingrese el valor para la empresa {i}, empleado{j}"))
        matriz[i][j] = valor
        
print(matriz)