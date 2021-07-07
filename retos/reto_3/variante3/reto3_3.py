# -*- coding: utf-8 -*-
"""
reto 3 version 3
"""
#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante

#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""



#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 
def funcionOR(bits1,bits2,OP):
    resultado = []
    for i in range(len(bits1)):
        if (bits1[i] == '1' or bits2[i] == '1'):
            resultado.append("1")
        else:
            resultado.append("0")
    return resultado

def funcionAND(bits1,bits2,OP):
    resultado = []
    for i in range(len(bits1)):
        if (bits1[i] == '1' and bits2[i] == '1'):
            resultado.append("1")
        else:
            resultado.append("0")
    return resultado

def funcionXOR(bits1,bits2,OP):
    resultado = []
    for i in range(len(bits1)):
        if (bits1[i] == '1' and bits2[i] == '0') or (bits1[i] == '0' and bits2[i] == '1'):
            resultado.append("1")
        else:
            resultado.append("0")
    return resultado

"""Fin espacio para programar funciones propias"""

def calculadora(bits1, bits2, OP):
    
    
    #PROGRAMA ACÁ LA SOLUCIÓN
    if (OP == "OR"):
        resultado = funcionOR(bits1, bits2, OP)
    elif(OP == "AND"):
         resultado = funcionAND(bits1, bits2, OP)
    elif(OP == "XOR"):
        resultado = funcionXOR(bits1, bits2, OP)
    
    return resultado

bits1 = "0110110110"
bits2 = "1100011101"
OP = "XOR"
resultado = calculadora(bits1, bits2, OP)
resultado = "".join(resultado)
print(resultado)

"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
#pruebas_codigo_estudiante(calculadora)
