# -*- coding: utf-8 -*-

from Tienda import Tienda

class Producto(Tienda):
    def __init__(self,nombre,tamano,tipo,direccion,empleados,marca,cantidad,
                 ide,ida,precio,descripcion,nombre_producto):
        super().__init__(nombre, tamano, tipo, direccion, empleados, ide)
        
        self.marca = marca
        self.cantidad = cantidad
        self.ida = ida
        self.precio = precio
        self.descripcion = descripcion
        self.nombre_producto = nombre_producto
                
    def crear(self):
        print("ingresaron nuevos productos")
    
    def eliminar(self):
        print("se elimino un producto")
        
    def modificar(self):
        print("se actualizo el inventario")
        
    def domicilios(self):
        print("se hizo un domicilio")
        
    def info(self):
        print("nombre del producto: " +self.nombre_producto)
    
    def infotienda(self):
        super().info()
        
p1 = Producto("tienda la 55","grande","supermercado","cra 55 N 21d-10",10,
              "roa",30,1001,10011,2300,"arroz blanco de 500g","arroz premium")

#%%
p1.info()
print(p1.direccion)
p1.infotienda()