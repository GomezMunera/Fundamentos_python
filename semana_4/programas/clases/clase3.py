# In[]
"""
Atributos intrínsecos

"""

# In[]
# clase persona para agregar un método que le permita calcular la edad
# ingresando la fecha de nacimiento
import datetime
class Persona:
    """"
    Clase creada para asignar el nombre de una persona y calcular la edad, a
    partir de su fecha de nacimiento, para esto se hace uso de la libreria 
    datetime, por tanto es necesario acceder al método calcularEdad por medio
    del formato de datetime: ejemplo datetime.date(año,mes,día)
    """
    def __init__(self, nombre):
        self.nombre = nombre
        
    def calcularEdad(self,nacimiento):
        today = datetime.date.today()
        self.hoy = today.year
        self.hoy_m = today.month
        self.hoy_d = today.day
        self.fecha = nacimiento.year
        self.fecha_m = nacimiento.month
        self.fecha_d = nacimiento.day
        
        if (self.fecha > self.hoy):
            print("Error en fecha de nacimiento")
        else:
            if(self.fecha_m - self.hoy_m > 0) and (self.fecha_d - self.hoy_d > 0):
                self.edad = self.hoy - self.fecha - 1
                print("su edad es: {}".format(self.edad))
            else:
                self.edad = self.hoy - self.fecha
                print("su edad es: {}".format(self.edad))
            return self.edad

p1 = Persona("John")
p1.calcularEdad(datetime.date(1988, 10, 14))

print('Atributos de la clase')
print(Persona.__name__)
print(Persona.__module__)
print(Persona.__doc__)
print(Persona.__dict__)
print('Atributos del objeto')
print(p1.__class__)
print(p1.__dict__)

# In[]
"""Atributos de clase"""
class Persona:
    """ Un ejemplo de clase que contiene la cédula, el nombre y el apellido
    de una persona, el ejemplo sirve para mostrar un atributo de clase"""
    
    contador_instancias = 0
    # contador_instancias no es parte de un objeto individual
    
    def __init__(self, dni,nombre,apellido):
        Persona.contador_instancias += 1
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        

p1 = Persona(123,'Juan', 'Aristizabal')
p2 = Persona(222,'Carolina', 'Garcia')
p3 = Persona(333,'Jairo', 'Duque')
p4 = Persona(444,'Tomas', 'Giraldo')
print(Persona.contador_instancias)

# In[]
"""Ejemplo de poliformismo
"""
from validaciones import esNumerico

class Punto3D(object):
    """Representación de un punto en el plano cartesiano, con valores x,y
    """
    
    def __init__(self,x=0,y=0,z=0):
        """Constructor del punto, debe ser numérico"""
        if(esNumerico(x) and esNumerico(y)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise TypeError("x e y deben ser valores numéricos")
        
    
    def distancia(self, p2):
        dx = self.x - p2.x
        dy = self.y - p2.y
        dz = self.z - p2.z
        return (dx**2 + dy**2 + dz**2)**0.5

    
    def norma(self):
        """ devuelve la norma del vector, desde el origen al punto """
        return(self.x**2 + self.y**2 + self.z**2)**0.5
# In[]
"""
ejemplo de herencia 
"""
class Persona:
    """Ejemplo de clase padre"""
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def cumpleano(self):
        print('Tenias la edad de', self.edad)
        self.edad += 1
        print('Feliz cumpleaños, ahora tienes', self.edad)

class Empleado(Persona):
    def __init__(self, nombre, edad, id):
        super().__init__(nombre, edad)
        self.id = id
    def calcularPago(self, horas_trabajadas):
        valor_hora = 10000
        if self.edad >= 18:
            valor_hora += 2500
        return horas_trabajadas * valor_hora

ob1 = Empleado(22,22,22)
print(ob1.nombre)

# In[]
"""Herencia multiple"""
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
        print("muestra información del color")
        
class Cuadrado(Forma,Color):
    def __init__(self, alto, ancho, color):
        Forma.__init__(self,alto, ancho)
        Color.__init__(self,color)
        
    def area(self):
        return self.alto * self.ancho 
    
class Triangulo(Color,Forma):
    def __init__(self, alto, ancho, color):
        Forma.__init__(self,alto, ancho)
        Color.__init__(self,color)
        
    def area(self):
        return self.alto * self.ancho / 2
    
f1 = Cuadrado(4,6,"Rojo")
print(f1.ancho)
print(f1.color)
print(f1.area())
f1.info()

f2 = Triangulo(4,4,"Verde")
print(f2.ancho)
print(f2.color)
print(f2.area())
f2.info()

# In[]
""" Herencia multiple secuencia """
class Vehiculo:
    def info(self):
        print("Mensaje desde Vehiculo")

class Terrestre(Vehiculo):
    def otro(self):
        print("M")
    
class Aereo(Vehiculo):
    def info(self):
        Vehiculo.info(self)
        print("Mensaje desde aereo")

class Moto(Terrestre):
    def info(self):
        Terrestre.info(self)
        print("Mensaje desde moto")
    
aereo1 = Aereo()
aereo1.info()
moto1 = Moto()
moto1.info()

# In[]
""" Polimorfismo"""
class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def sonido(self):
        return "Error - Las subclases son las que tienen sonido"
        
    def imprimirSonido(self):
        self.sonido()
        
class Gato(Animal):
    def __init__(self,nombre):
        super().__init__(nombre)
        
    def sonido(self):
        return "Miau, Miau"
        
class Perro(Animal):
    def __init__(self,nombre):
        super().__init__(nombre)
        
    def sonido(self):
        return "Guau, Guau"
        
g1 = Gato("Judas")
g2 = Gato("lio")
p1 = Perro("Negro")
p2 = Perro("Beethoven")

animales = [g1,g2,p1,p2]


def sonidos(arreglo):
    for i in arreglo:
        print(f"{i.nombre} tiene sonido {i.sonido()}")
        
sonidos(animales)
print(p2.imprimirSonido())