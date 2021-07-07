# -*- coding: utf-8 -*-
"""
Ejemplo de matplot
"""

# In[]
# importación de librerias
import matplotlib.pyplot as plt
import numpy as np

# In[]
# generando visualización co pyplot
plt.plot([1, 2, 3, 4, 3, 2])
plt.ylabel('eje y')
plt.xlabel('eje x')
#plt.show()

# In[]
"""
Creación de una figura que contiene un axes usando pyplot.subplots
"""
# crea una figura que contiene un axes
fig, ax = plt.subplots()

#In[]
ax.plot([1,2,3,4],[1,4,2,3])

# In[]
# se puede crear directamente la gráfica sin necesidad de crear el axes
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Matplotlib plot.

# In[]
"""
ejes con estilos
"""

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b*') # define estilos
plt.axis([0, 6, 0, 20]) # define limite eje x y eje y
plt.show()

# In[]
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# In[]
# trabajando con scatter
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

# In[]
# crea una figura vacia
fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes

# In[]
# cumsum() retorna el acumulado de la suma de los elementos a lo largo del eje
y = np.random.randn(100).cumsum()
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
axs[0,0].plot([1,2,3,4,5],[5,2,4,1,3])
axs[0,1].plot(y)

# In[]
"""
otra forma de utilizar los subplots
"""
fig, (ax1,ax2) = plt.subplots(1,2)
ax1.plot(y)

# In[]
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)
plt.title("segunda")               # a second figure
plt.plot([4, 5, 6])          # creates a subplot() by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('con 1, 2, 3') # subplot 211 title

# In[]
"""
graficando con variables categoricas
"""
names = ['grupo_A', 'grupo_B', 'grupo_C']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Figuras categoricas')
plt.show()

# In[]
# Separa dos figuras verticales
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, np.exp(t1), 'bo', t2, np.exp(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

# In[]
"""
Interfaz orientada a objetos:
    Crea explicitamente una figura y axes y llama los métodos en ellos
"""
x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.

# In[]
"""
Interfaz pyplot:
    pyplot configura automáticamente las figuras y los ejes, utiliza las 
    funciones de pyplot para el trazado
"""
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

# In[]
"""
Graficas tridimensionales
"""
from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
# cmap: autumn, coolwarm, magma, summer, inferno, plasma, viridis, cividis
"""
https://matplotlib.org/stable/tutorials/colors/colormaps.html
"""
surf = ax.plot_surface(X, Y, Z, cmap=cm.cividis,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

