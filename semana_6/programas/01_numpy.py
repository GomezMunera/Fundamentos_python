# -*- coding: utf-8 -*-
""""

NumPy basics
"""
# In[]
# importación de numpy
import numpy as np

# In[]
# configurar una semilla para reproducibilidad
np.random.seed(seed=1234)

# In[]
# Escalares
x = np.array(6) # escalar
print ("x: ", x)
# Numero de dimensiones
print ("x ndim: ", x.ndim)
# Dimensiones
print ("x shape:", x.shape)
# Tamaño de elementos
print ("x size: ", x.size)
# Tip de Dato 
print ("x dtype: ", x.dtype)

# In[]
# 1-D Array
x = np.array([1.3 , 2.2 , 1.7])
print ("x: ", x)
print ("x ndim: ", x.ndim)
print ("x shape:", x.shape)
print ("x size: ", x.size)
print ("x dtype: ", x.dtype) # notar datatype tipo flotante

# In[]
# 3-D array (matrix)
x = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
print ("x:\n", x)
print ("x ndim: ", x.ndim)
print ("x shape:", x.shape)
print ("x size: ", x.size)
print ("x dtype: ", x.dtype)

# In[]
# Funciones
print ("np.zeros((2,2)):\n", np.zeros((2,2)))
print ("np.ones((2,2)):\n", np.ones((2,2)))
print ("np.eye((2)):\n", np.eye((2)))
print ("np.random.random((2,2)):\n", np.random.random((2,2)))

# In[]
"""# Indexado"""

# Indexing
x = np.array([1, 2, 3])
print ("x[0]: ", x[0])
x[0] = 0
print ("x: ", x)

# In[]
# Slicing
x = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print (x)
print ("x column 1: ", x[:, 1]) 
print ("x row 0: ", x[0, :]) 
print ("x rows 0,1,2 & cols 1,2: \n", x[:3, 1:3])

# In[]
# Integer array indexing
print (x)
print(len(x))
rows_to_get = np.arange(len(x))
print ("rows_to_get: ", rows_to_get)
cols_to_get = np.array([0, 2, 1])
print ("cols_to_get: ", cols_to_get)
print ("indexed values: ", x[rows_to_get, cols_to_get])

# In[]
# Boolean array indexing
x = np.array([[1,2], [3, 4], [5, 6]])
print ("x:\n", x)
print ("x > 2:\n", x > 2)
print ("x[x > 2]:\n", x[x > 2])

# In[]
"""# Array math"""

# Matemática básica
x = np.array([[1,2], [3,4]], dtype='i')
y = np.array([[1,2], [3,4]], dtype=np.float64)
print ("x + y:\n", np.add(x, y)) # or x + y
print ("x - y:\n", np.subtract(x, y)) # or x - y
print ("x * y:\n", np.multiply(x, y)) # or x * y

# In[]
# Dot product
a = np.array([[1,2,3], [4,5,6]], dtype=np.float64) # we can specify dtype
b = np.array([[7,8], [9,10], [11, 12]], dtype=np.float64)
print(a)
print(b)
print (a.dot(b))

# In[]
# Sum across a dimension
x = np.array([[1,2],[3,4]])
print (x)
print ("sum all: ", np.sum(x)) # adds all elements
print ("sum by col: ", np.sum(x, axis=0)) # add numbers in each column
print ("sum by row: ", np.sum(x, axis=1)) # add numbers in each row

# In[]
# Transposing
print ("x:\n", x)
print ("x.T:\n", x.T)

# In[]
"""# Advanced"""

# Arreglo por repetición
# Tile
x = np.array([[1,2], [3,4]])
y = np.array([5, 6])
addent = np.tile(y, (len(x), 1))
print(x)
print ("addent: \n", addent)
z = x + addent
print ("z:\n", z)


# In[]
# Broadcasting
x = np.array([[1,2], [3,4]])
y = np.array([5, 6])
z = x + y
print ("z:\n", z)

# In[]
# Reshaping (redimensionamiento)
x = np.array([[1,2], [3,4], [5,6]])
print (x)
print ("x.shape: ", x.shape)
y = np.reshape(x, (2, 3))
print ("y.shape: ", y.shape)
print ("y: \n", y)

# In[]
# Removing dimensions (quitando dimensiones)
x = np.array([[[1,2,1]],[[2,2,3]]])
print ("x.shape: ", x.shape)
y = np.squeeze(x, 1) # squeeze dim 1 (reduce una dimensión)
print ("y.shape: ", y.shape) 
print("x: \n", x)
print ("y: \n", y)

# In[]
# Adding dimensions
x = np.array([[1,2,1],[2,2,3]])
print ("x.shape: ", x.shape)
y = np.expand_dims(x, 2) # expand dim 1 (Expande una dimensión)
print ("y.shape: ", y.shape) 
print ("y: \n", y)

# In[]
"""# Recursos

[manual de referencia de NumPy] https://numpy.org/doc/stable/user/whatisnumpy.html
"""