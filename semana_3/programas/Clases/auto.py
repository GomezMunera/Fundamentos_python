# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 00:20:36 2021

@author: Digital
"""

class Auto(object):
    # Atributo de clase
    modelo = 2021
    
    cont = 0

    # El método __init__ es llamado al crear el objeto
    def __init__(self, marca, color):
        print(f"Creando registro de un auto {marca}, {color}")
        Auto.cont = Auto.cont + 1

        # Atributos de instancia
        self.marca = marca
        self.color = color
        
        
    
    # métodos de la instancia
    def girar(self):
        print("haciendo un giro")
        self.palabra = "estas dentro de giro"
        self.marca = "otra"

    def avanzar(self, kilometros):
        print(f"Avanzando {kilometros} kilometros")