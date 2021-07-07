# -*- coding: utf-8 -*-
#Ejercicio De Clases 
""" Clase para una Tienda """

class Tienda(object):
    def __init__(self,nombre,tamano,tipo,direccion,empleados,ide):
        self.nombre = nombre
        self.tamano = tamano
        self.tipo = tipo
        self.direccion = direccion
        self.empleados = empleados
        self.ide = ide
        
    def vender(self):
        print("se hizo una venta")
    
    def comprar(self):
        print("se hizo una compra")
        
    def inventario(self):
        print("se hizo un inventario")
        
    def domicilios(self):
        print("se hizo un domicilio")
        
    def info(self):
        print("nombre de la tienda: " +self.nombre)
        
    
        
    
        
    


