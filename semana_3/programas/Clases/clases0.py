# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 23:13:15 2021

@author: Digital
"""

#%% Programación orientada a objetos

# clase Persona
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
"""La clase persona posee 2 atributos, o variables de instancia 
__init__ es un método especial, es un inicializador o constructor para la clase
este indica los datos que deben ser suministrados cuando una instancia de la 
clase Persona es creada.

Los valores suministrados se almacenarán entonces dentro de una instancia de 
la clase (representada por por la variable especial self) en las variables de 
instancia/atributos self.name y self.edad. Los parámetros del método __init__ 
son variables locales y desaparecerán cuando el método termine, pero self.name
y self.age son son variables de instancia y existirán mientras el objeto esté
disponible.

self se utiliza para representar el objeto en el que se ejecuta el 
método. Esto proporciona el contexto dentro del cual el método se ejecuta y
permite que el método acceda a los datos que contiene el objeto. Por lo tanto,
self es el objeto en sí mismo.


"""

#%%
# una nueva instancia u objeto
p1 = Persona("John", 32)
p2 = Persona("Angela", 30)

#%%
# identificadores
"""Cada instancia tiene su propio identificador unico"""
print('id(p1):', id(p1))
print('id(p2):', id(p2))

#%% Accediendo a los atributos
print(p1)

#%% Accediendo a los atributos del objeto
print(p1.nombre, "tiene", p1.edad)

#%% Actualización de los atributos del objeto
p1.nombre = "Juan"
p1.edad = 25
print(p1.nombre, "tiene", p1.edad)

#%% Definiendo una representación de String por defecto
# usado para definir un método que pueda convertir un objeto en un string para
# propositos de impresión
# clase Persona
class Persona:
    """"
    Una clase Persona que tiene de atributos nombre y edad
    """
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return self.nombre + " tiene " + str(self.edad)

#%%
p3 = Persona("Maria", 22)
print(p3)

#%% haciendo un método cumpleano()
class Persona:
    """"
    Una clase Persona que tiene de atributos nombre y edad
    """
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return self.nombre + " tiene " + str(self.edad)
    
    def cumpleano(self): # sin parámetros
        print("Feliz cumpleaños {}, tenias: {}".format(self.nombre,self.edad))
        self.edad += 1 
        print("Ahora tienes: {}".formata(self.edad))
    
    def calcularPago(self, horas_trabajadas):
        VALORHORA = 20000
        if self.edad >= 18:
            VALORHORA += 5000
        return VALORHORA * horas_trabajadas

#%% returno de los métodos creados

p4 = Persona("Luis", 17)
print(p4)

pago =p4.calcularPago(10)
print(pago)