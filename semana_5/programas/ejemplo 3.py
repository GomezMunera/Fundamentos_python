import random

estrella="\u2605"


filas=int(input("Ingrese filas: "))

columnas=int(input("Ingrese columnas: "))

cielo=[ [" " for i in range(columnas)] for j in range(filas)]


# for i in range(filas):
#     for j in range(columnas):
#         num=random.randint(0,5)
#         if num == 2:
#             cielo[i][j]=estrella

numero_est=int(input("cantidad de estrellas: "))

for i in range(numero_est):
    fil_al= random.randint(0, filas-1)
    col_al= random.randint(0, columnas-1)
    
    cielo[fil_al][col_al]=estrella
    
    
for fil in cielo:
    for elementos in fil:
        print(elementos, end=" ")
    print()
