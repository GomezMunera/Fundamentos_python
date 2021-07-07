
# In[]
# clase circulo
class Circulo:
    pass

print(type(Circulo()))
# creanndo un objeto
circulo1 = Circulo()
# In[]
class persona:
    pass

persona1=persona()
persona2=persona()

# In[]
# constructor
# __init__ función especial
class Circulo2:
    def __init__(self):
        print("Se inicializa la clase, se crea un objeto")

#creamos un objeto
circulo2=Circulo2()

# In[]
# Agregar atributos
class Circulo3:
    def __init__(self):
        self.radio = 4
        self.mensaje = "mensaje del constructor de la clase"

# creamos el objeto
circulo3=Circulo3()

# observando un atributo del obtejo instanciado en 1
print(circulo3.radio)
print(circulo3.mensaje)

# si declaramos otro objeto
circulo4 = Circulo3()
# observando un atributo del obtejo instanciado en 2
print(circulo4.radio)

# In[]
# inicializador con parámetros
class Circulo4:
    def __init__(self, radio):
        self.radio = radio
        self.mensaje = "Una nueva clase de circulo"
        
# si declaramos otro objeto
circulo5 = Circulo4(10)
# observando un atributo del obtejo instanciado en 2
print(circulo5.radio)

# In[]
# crear una clase persona con los atributos nombre, apellido, edad, sexo


# In[]
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.IVA = 0.19
        self.ENVIO = 1000
    
compra1 = Producto("Camiseta",30000)
print(compra1)

# In[]
class Producto2:
    IVA = 0.19
    ENVIO = 1000
    def __init__(self):
        self.nombre = input("Ingrese el artículo: ")
        self.precio = int(input("Ingrese el precio: "))
        
    # métodos
    def precioTotal(self):
        self.total = self.precio + self.IVA*self.precio + self.ENVIO
        return self.total
    
compra3 = Producto2()
print(compra3.precio)
print("El precio total es ",compra3.precioTotal())


# In[]

""" Sugerencia:

    Siempre que vaya a invocar un atributo o método dentro de la misma clase, invóquela siguiendo el patrón:
        self.nombreVariable
        self.nombreMetodo()

    Siempre que vaya a invocar una variable de clase, invóquela siguiendo el patrón:
        NombreClase.variableDeClase

"""
# In[]
# Explicar métodos get a set
# crear métodos para obtener y modificar el nombre

# In[]
# crear un método al circulo que calcule el área y el perímetro

# In[]
# funcion para la edad import datetime
import datetime

def calcularEdad(nacimiento):
    hoy = datetime.date.today().year
    fecha = nacimiento.year
    
    if (fecha > hoy):
        print("Error en fecha de nacimiento")
    else:
        edad = hoy - fecha
        print("su edad es: {}".format(edad))
        return edad
        
calcularEdad(datetime.date(1988, 10, 14))

# In[]
# modificar la clase persona para agregar un método que le permita calcular la edad
# ingresando la fecha de nacimiento
import datetime
class persona:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def calcularEdad(self,nacimiento):
        self.hoy = datetime.date.today().year
        self.hoy_m = datetime.date.today().month
        self.hoy_d = datetime.date.today().day
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

p1 = persona("John")
p1.calcularEdad(datetime.date(1988, 10, 14))
# In[]
circulonuevo1 = Circulo4(5)
circulonuevo2 = Circulo4(12.0)
# arrelgo de objetos
arreglocirculos = []
arreglocirculos.append(circulonuevo1)
arreglocirculos.append(circulonuevo2)
print(arreglocirculos)

# para verlos
for cir in arreglocirculos:
    print(cir.radio)
# In[]
# enviar un arreglo a un método

class Circulo5: 
    descripcion = "Hola Circulo"   
    def __init__(self, radio): 
        self.radio = radio
        
    def imprimirRadiosConIndice(self,arregloCirculos):
            for x in range(len(arregloCirculos)): 
                print(f"Radio del cículo {x+1} es {arregloCirculos[x].radio}")        
                
    def imprimirRadiosSinIndice(self,arregloCirculos):
        for circ in arregloCirculos: 
            print("Radio",circ.radio)  
           

circulonuevo3 = Circulo5(15.0)
circulonuevo4 = Circulo5(21.0)
arreglocirculos2 = []
arreglocirculos2.append(circulonuevo3)
arreglocirculos2.append(circulonuevo4)

circulonuevo3.imprimirRadiosConIndice(arreglocirculos2)
circulonuevo4.imprimirRadiosSinIndice(arreglocirculos2)

# In[]
# Métodos que reciben otros objetos

class Circulo: 
    descripcion = "Hola Circulo"   
    def __init__(self, radio): 
        self.radio = radio
    
    def dobleCirculo(self,circ):
        print("Radio del circulo que invoca",self.radio)
        print("Radio del circulo que recibo",circ.radio)

circulo1 = Circulo(8.0)
circulo2 = Circulo(5.0)

circulo1.dobleCirculo(circulo2)



# In[]
# Métodos que devuelven objetos

class Circulo: 
    descripcion = "Hola Circulo"   
    def __init__(self, radio): 
        self.radio = radio
    
    def nuevoCirculo(self):
        nuevo = Circulo(self.radio*5)
        return nuevo
        

circulo1 = Circulo(8.0)
otroCirc = circulo1.nuevoCirculo()
print(otroCirc.radio)

# In[]
# visibilidad atributos y métodos
class Circulo: 
    
    def __init__(self, radio): 
        self.radio = radio
        self.descripcion = "Hola Circulo"
        
    def getRadio(self):
        return self.radio;
    
    def setRadio(self,radio):
        if(radio >= 0):
            self.radio = radio;
        else:
            print("No se puede asignar un radio negativo")
    
circulo1 = Circulo(6)
print("Antes del cambio: ",circulo1.radio)
circulo1.radio = 8 #No debería permitir modificar la variable directamente
print("Después del cambio: ",circulo1.radio)

# In[]
# encapsulamiento
class Circulo: 
    
    def __init__(self, radio): 
        self.__radio = radio
        self.descripcion = "Hola Circulo"
        
    def getRadio(self):
        return self.__radio;
    
    def setRadio(self,radio):
        if(radio >= 0):
            self.__radio = radio;
        else:
            print("No se puede asignar un radio negativo")
    
circulo1 = Circulo(4)
print("Radio: ",circulo1.getRadio())

circulo1.__radio = -10
print("Radio: ",circulo1.getRadio())

circulo1.setRadio(5)
print("Radio: ",circulo1.getRadio())

circulo1.setRadio(-10)