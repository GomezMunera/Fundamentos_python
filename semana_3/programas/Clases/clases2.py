# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 00:08:02 2021

@author: Digital
"""

#%% Creando clases
# palabra object es de un objeto básico, no esta basado en un objeto más complejo
class Punto(object):
    """Representación de un punto en el plano cartesiano, con valores x,y
    """
    def __init__(self,x=0,y=0):
        """Constructor del punto, debe ser numérico"""
        self.x = x
        self.y = y

#%% Definición de atributos
p = Punto(3,4)
print(p.x)
print(p.y)

#%% Agregando validaciones al constructor
q = Punto("A",True)
print(q.x)
print(q.y)

#%%
from validaciones import esNumerico

class Punto(object):
    """Representación de un punto en el plano cartesiano, con valores x,y
    """
    
    def __init__(self,x=0,y=0):
        """Constructor del punto, debe ser numérico"""
        if(esNumerico(x) and esNumerico(y)):
            self.x = x
            self.y = y
        else:
            raise TypeError("x e y deben ser valores numéricos")
            
#%%
p = Punto("A", True)

#%% 
"""
Agregando operaciones
"""
class Punto(object):
    """Representación de un punto en el plano cartesiano, con valores x,y
    """
    
    def __init__(self,x=0,y=0):
        """Constructor del punto, debe ser numérico"""
        if(esNumerico(x) and esNumerico(y)):
            self.x = x
            self.y = y
        else:
            raise TypeError("x e y deben ser valores numéricos")
        
    
    def distancia(self, p2):
        dx = self.x - p2.x
        dy = self.y - p2.y
        return (dx**2 + dy**2)**0.5
    
    def restar(self, b):
        """ Devuelve un nuevo punto con la resta de 2 puntos """
        return Punto(self.x - b.x, self.y - b.y)
    
#instanciando
p = Punto(5,7)
q = Punto(2,3)
print(p.distancia(q))

# restar


