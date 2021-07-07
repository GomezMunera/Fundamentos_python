# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 13:10:52 2021

@author: Digital
"""

#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la clase cliente
#from pruebas import pruebas_codigo_estudiante
from cliente import cliente
import numpy as np
"""NOTAS:
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""
"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL

"""Fin espacio para programar funciones propias"""

def sede_bancaria(cola_general):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
   
    cola_caja = []
    cola_info = []
    suma_consignaciones = 0
    suma_retiros = 0
    edad_minima_retiro1 = []
    edad_minima_consignacion1 = []
    edad_minima_info1 = []
    edad_minima_retiro = 0
    edad_minima_consignacion = 0
    edad_minima_info = 0
   
    for cliente in cola_general:
        if cliente.fila_interes == "caja":
            cola_caja.append(cliente.nombre)
        else:
            cola_info.append(cliente.nombre)
           
        if cliente.transaccion == "retirar":
            if cliente.dinero_cuenta_bancaria > cliente.cantidad_retirar:
                suma_retiros += cliente.cantidad_retirar
                cliente.dinero_cuenta_bancaria -= cliente.cantidad_retirar
                edad_minima_retiro1.append(cliente.edad)
               
        elif cliente.transaccion == "consignar":
            cliente.dinero_cuenta_bancaria += cliente.cantidad_consignar
            suma_consignaciones += cliente.cantidad_consignar
            edad_minima_consignacion1.append(cliente.edad)
           
        else:
            edad_minima_info1.append(cliente.edad)
           
    edad_minima_retiro = np.amin(edad_minima_retiro1)
    edad_minima_info = np.amin(edad_minima_info1)
    edad_minima_consignacion = np.amin(edad_minima_consignacion1)
   
    if edad_minima_consignacion ==0:
       edad_minima_consignacion = -1
       
    if edad_minima_retiro ==0:
        edad_minima_retiro = -1
       
    if edad_minima_info ==0:
        edad_minima_info = -1        
       
    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion



cola_general = [
cliente("Matt",21,235000,"caja","retirar",100000,0),
cliente("Dan",32,658000,"caja","retirar",98000,0),
cliente("Steve",22,34000,"caja","consignar",0,20000),
cliente("Diana",29,87000,"info","ninguna",0,0),
cliente("Cris",21,87000,"caja","consignar",0,77000),
cliente("Jorge",41,987000,"caja","retirar",400000,0)
]

sal = sede_bancaria(cola_general)

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#pruebas_codigo_estudiante(sede_bancaria)