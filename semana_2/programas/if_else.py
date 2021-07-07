# -*- coding: utf-8 -*-
"""
Created on Fri May 28 20:42:35 2021

@author: Digital
"""

# datos de entrada
nota = float(input("Ingrese nota: "))
estudiante_matriculado = int(input("Ingrese 1 o 0: "))

if nota > 2.95:
    if nota <= 5:
        if estudiante_matriculado == 1:
            print("El estudiante aprobó")
        else:
            print("No esta en la clase")
    else:
        print("Nota no valida")
else:
    print("El estudiante reprobó")
    
print("Programa finalizado")