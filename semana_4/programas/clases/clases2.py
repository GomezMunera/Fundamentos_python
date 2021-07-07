
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
    
    def norma(self):
        """ devuelve la norma del vector, desde el origen al punto """
        return(self.x**2 + self.y**2)**0.5
    
    def distancia2(self,b):
        """Devuelve la distancia entre dos puntos"""
        r = self.restar(b)
        return r.norma()
    
#instanciando
p = Punto(5,7)
q = Punto(2,3)
print(p.distancia(q))

# restar
pr1 = p.restar(q)
print(p.restar(q))

# In[]
"""Métodos para operar aritmeticamente"""
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
    
    def norma(self):
        """ devuelve la norma del vector, desde el origen al punto """
        return(self.x**2 + self.y**2)**0.5
    
    def distancia2(self,b):
        """Devuelve la distancia entre dos puntos"""
        r = self.restar(b)
        return r.norma()
    
    def __add__(self,b):
        """Entrega la suma de 2 puntos"""
        return Punto(self.x + b.x, self.y + b.y)
    
    def __sub__(self,b):
        """Entrega la resta de 2 puntos"""
        return Punto(self.x - b.x, self.y - b.y)
    
    def __mul__(self,b):
        """Entrega la multiplicación de 2 puntos"""
        return Punto(self.x * b.x, self.y * b.y)
    
    def __divmod__(self,b):
        """Entrega la división de 2 puntos"""
        return Punto(divmod(self.x,b.x), divmod(self.y,b.y))
    
    def __str__(self):
        return "x: " + str(self.x) + ", " + "y: "+ str(self.y)
    
    def __eq__(self, b):
        """ Devuelve si dos puntos son iguales. """
        return self.x == b.x and self.y == b.y
    
    def __ne__(self, b):
        """ Devuelve si dos punto son diferentes"""
        return not self == b
    
    """def __cmp__(self, b):
        if (self.x == b.x) and (self.y == b.y):
            return 1
        else:
            return 0"""

#instanciando
p = Punto(4,9)
q = Punto(4,9)
print(p+q)
print(p-q)
#print(p//q)
print(p.y//q.y)



