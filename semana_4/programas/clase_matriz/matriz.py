import random
from vector import vector

class Matriz:
    def __init__(self,m,n):
        self.m = m
        self.n = n
        self.mat = []*(m+1)
        for i in range(m + 1):
            a = [0] * (n+1)
            self.mat.append(a)
            
    def numeroFilas(self):
        return (self.m)
    
    def numerocolumnas(self):
        return (self.n)
    

    def construyeMatriz(self,r=100):
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.mat[i][j] = random.randint(1,r)
                
                
    def imprimeMatrizPorFilas(self, mensaje = "Matriz sin nombre"):
        print("\n", mensaje)
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                print(self.mat[i][j], "\t", end="")
            print()
            
    def imprimeMatrizPorColumnas(self, mensaje = "Matriz sin nombre"):
        print("\n", mensaje)
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                print(self.mat[j][i], "\t", end="")
            print()
            
    def intercambiarFilas(self, i,j):
        for k in range(1,self.n+1):
            aux = self.mat[i][k]
            self.mat[i][k] = self.mat[j][k]
            self.mat[j][k] = aux
            
    def intercambiarColumnas(self, i,j):
        for k in range(1,self.m+1):
            aux = self.mat[k][i]
            self.mat[k][i] = self.mat[k][j]
            self.mat[k][j] = aux
            
    def sumarFilas(self):
        v = vector(self.m)
        for i in range(1, self.m+1):
            s=0
            for j in range(1, self.n+1):
                s = s + self.mat[i][j]
            v.agregarDato(s)
        return v
    
    def sumarColumnas(self):
        v = vector(self.n)
        for i in range(1, self.n+1):
            s=0
            for j in range(1, self.m+1):
                s = s + self.mat[j][i]
            v.agregarDato(s)
        return v

    def traspuesta(self):
        c = Matriz(self.n,self.m)
        for i in range(1, self.m+1):
            for j in range(1, self.n+1):
                c.mat[j][i] = self.mat[i][j]
        return c
    
    # suma de dos matrices
    def __add__(self,b):
        c = Matriz(self.m, self.n)
        if self.m != b.m or self.n != b.n:
               print("Matrices no se pueden sumar. Son de dimensiones diferentes")
               return c
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                c.mat[i][j] = self.mat[i][j] + b.mat[i][j]
        return c
    
    #producto de la diagonal principal
    def productoDiagonalPrincipal(self):
       f = 1
       for i in range(1, self.m + 1):
               f = f * self.mat[i][i]
       return f
   
    # producto de matrices
    def __mul__(self, b):
          c = Matriz(self.m, b.n)
          if self.n != b.m:
                   print("Matrices no se pueden multiplicar. ", end = "")
                   print("el número de columnas de self es diferente del número de columnas de b")
                   return c
          for i in range(1, self.m + 1):
              for j in range(1, b.n + 1):
                  c.mat[i][j] = 0
                  for k in range(1, self.n + 1):
                      c.mat[i][j] = c.mat[i][j] + self.mat[i][k] * b.mat[k][j]
          return  c
      
    def sumaTriangularInferior(self):
        s = 0
        for i in range(1, self.m + 1):
            for j in range(1, i + 1):
                s = s + self.mat[i][j]
        return s

    def sumaTriangularEstrictamenteInferior(self):
        s = 0
        for i in range(2, self.m + 1):
            for j in range(1, i):
                s = s + self.mat[i][j]
        return s
    
    def sumaTriangularSuperior(self):
        s = 0
        for i in range(1, self.m + 1):
            for j in range(i, self.n + 1):
                s = s + self.mat[i][j]
        return s

    def sumaTriangularEstrictamenteSuperior(self):
        s = 0
        for i in range(1, self.m):
            for j in range(i + 1, self.n + 1):
                s = s + self.mat[i][j]
        return s