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


