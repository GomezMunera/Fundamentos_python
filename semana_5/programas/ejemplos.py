


matriz=[[1,2],
        [3,4]
        ]

matriz2=[["a","b"],
        ["c","d"]
        ]
## Es un error
matriz3=[[0]*2]*2

matriz4=[ [0 for i in range(2)] for j in range(2)]

matrizn=[0]*2
for i in range(2):
    fila=[0]*2
    for j in range(2):
        fila[j]=0
    matrizn[i]=fila
    
for i in range(0,2):
    for j in range(0,2):
        print(matrizn[i][j], end=" ")
    print()



