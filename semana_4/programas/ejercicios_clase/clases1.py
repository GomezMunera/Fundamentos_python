#%%

class Circulo:
    pass

c1 = Circulo()
print(type(c1))

#%%
class Circulo:
    
    def __init__(self):
        print("Llamado al constructor")
        
c2 = Circulo()

#%% 
class Circulo:
    def __init__(self, radio=1):
        self.radio = radio
        
c3 = Circulo(5)
print(c3.radio)

c4 = Circulo()
print(c4.radio)

#%%
import math
class Circulo:
    def __init__(self, radio = 1):
        self.radio = radio
        self.mensaje = "Creación de la clase"
        
    def perimetro(self):
        return 2*math.pi*self.radio
    
    def area(self):
        return math.pi*self.radio**2
    
    def __str__(self):
        return self.mensaje +" con radio " + str(self.radio)

c5 = Circulo(2)
print(c5.mensaje)

print("perimetro ", c5.perimetro())
print("área ", c5.area())

c6 = Circulo(4)
print(c6.mensaje)

print("perimetro ", c6.perimetro())
print("área ", c6.area())

print(c5)

c5.radio = 10
print(c5)

#%% 
class producto:
    IVA = 0.19
    ENVIO = 5000
    def __init__(self, nombre ,costo):
        self.nombre = nombre
        self.costo = costo
        