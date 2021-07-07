"""
Documento de clase
"""
class Persona:
    """Clase que hace referencia a una persona"""
    contador_instancias = 0
    
    def __init__(self, nombre, apellido,dni):
        Persona.contador_instancias += 1
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        
    def mover(self,p):
        print("{} se mueve {} pasos".format(self.nombre,p))
        
p1 = Persona("Juan", "Garcia", 2222)
# atributos intrínsecos de la clase
print(Persona.__name__)
print(Persona.__module__)
print(Persona.__dict__)
print(Persona.__doc__)

# atributos intrinsecos del objeto
print(p1.__class__)
print(p1.__dict__)

p2 = Persona("Maria", "lopez", 3333)
p3 = Persona("Ricardo", "Marin", 4444)

print("atributo de la clase",Persona.contador_instancias)

# In[]
class Estudiante(Persona):
    """ Clase hija """
    def __init__(self,nombre,apellido,dni,materias,deporte,id):
        super().__init__(nombre, apellido, id)
        self.materias = materias
        self.deporte = deporte
        self.id = id

estudiante1 = Estudiante("Roberto","Gómez", 111, 4, "natación", 4)

print(estudiante1.__class__)
print(estudiante1.nombre)
print(estudiante1.mover(4))

# In[]
""" Punto """
class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "x: "+str(self.x)+", "+"y: "+ str(self.y)
    
    def suma(self,b,c=0):
        return Punto(self.x + b.x, self.y + b.y)
        
    def __add__(self,b):
       return Punto(self.x + b.x, self.y + b.y)
   
    def __sub__(self,b):
        return Punto(self.x - b.x, self.y - b.y)
        
p = Punto(4,5)
q = Punto(3,3)

print(p)

m = p.suma(q)

print(m)
print(p+q)
print(p-q)

# In[]
""" Herencia Multiple"""
class Forma:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
        
    def info(self):
        print("Muestra información acerca de la figura")
        
class Color:
    def __init__(self, color):
        self.color = color
    
    def info(self):
        print("Muestra información acerca del color")
        
        
class Cuadrado(Color,Forma):
    def __init__(self,alto,ancho,color):
        Forma.__init__(self,alto,ancho)
        Color.__init__(self,color)
        
    def area(self):
        self.area1 = self.alto * self.ancho
        return self.area1
    
   
    def __str__(self):
        return str(self.alto*self.ancho)
    
    """def info(self):
        print("El área es: ", self.area1)"""

    
class Triangulo(Forma,Color):
    def __init__(self,alto,ancho,color):
        Forma.__init__(self,alto,ancho)
        Color.__init__(self,color)

        
    def area(self):
        self.area = self.alto * self.ancho / 2
        return self.area
    
    def __str__(self):
        return str(self.alto * self.ancho / 2)


t1 = Triangulo(3,2, "Verde")
area = t1.area()
print(area)
print(t1.color)

c1 = Cuadrado(4,4, "Amarillo")
c1.area()
c1.info()