# -*- coding: utf-8 -*-
"""
Created on Fri May 28 19:57:53 2021

@author: Digital
"""

# In[]
# Listas
lista1 = [5, 6, 7.0, "hola", True]
print(lista1)


print(lista1[0])
print(lista1[-1])

lista2 = [1,2,3,["python",False]]
print(lista2[3][1])

# In[]
lista3 = [1,2,3,["python",False,["cadena", 5]]]
print(lista3[3][2][1])

# In[]
lista4 = [1,5,7,lista2]
print(lista4)

# In[]
lista5 = []

nombre = input("Ingrese nombre: ")
lista5.append(nombre)
print(lista5)

# In[]
del lista4[3]
print(lista4)

# In[]
# tuplas
tupla1 = (1,2,3,(9,8))
print(tupla1)
print(tupla1[3][1])

# In[]

libro={
    "capitulo 1": {
        "paginas": 20,
        "ilustraciones": 12,
        "Titulos":["tema 1", "tema 2", "tema 3", {"sesion especial":"agradecimientos","autores":"Juan, David" }]
        
        },
    "capitulo 2":{
        "paginas":12,
        "ilustraciones":2
        
        }
    
}
