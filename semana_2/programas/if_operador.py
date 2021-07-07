# -*- coding: utf-8 -*-
"""
Created on Fri May 28 21:30:20 2021

@author: Digital
"""

nota = float(input("Ingrese nota: "))
estudiante_matriculado = int(input("Ingrese 1 o 0: "))

if nota > 2.95 and nota <= 5:
    if estudiante_matriculado == 1:
        print("El estudiante aprobó")
    else:
        print("No esta en la clase")
else:
    print("El estudiante reprobó")
    
print("Programa finalizado")