# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:59:04 2021

@author: Digital
"""

libro={}

while True:
    
    print("Datos que se pueden ingresar",
          "Titulo [T]",
          "Capítulo [C]",
          "Glosario[G]",
          "Bibliografía [B]",
          "Apéndice[A]", 
          sep="\n"          
          )
         
    dato=input("¿Que datos quiere ingresar? ")
    
    if dato.upper()=="T":
        
        libro["Titulo"] = input("Ingrese el título: ")
    
    elif dato.upper()=="C":
        
        while True:
            
            capitulo=input("Ingrese el nombre del capitulo: ")
            
            libro[capitulo]={"Resumen":"",
                              "Numero de paginas":0,
                              "Numero de ilustraciones":0               
                            }
                        
            libro[capitulo]["Resumen"] = input(f"Ingrese el resumen del capitulo {capitulo}: ")
            libro[capitulo]["Numero de paginas"] = input("Ingrese el número de paginas: ")
            libro[capitulo]["Numero de ilustraciones"] = input("Ingrese el número de número de ilustraciones: ")
                        
            temp=input("Desea ingresar otro capitulo")
            
            if temp =="s":
                continue
            else:
                break
        
    elif dato.upper()=="G":
        print("Selecciono Glosario")
    
    elif dato.upper()=="B":
        print("Selecciono Bibliografía")
    
    elif dato.upper()=="A":
        print("Selecciono Apéndice")
        
    
    
    ## Estructura de control de repetición
    var=input("¿Quiere agregar mas datos?: ")
    
    if var.lower() =="s":
        continue
    elif var.lower() =="n":
        print("Terminó el ingreso de datos")
        break
    else:
        print("No es un caracter válido")