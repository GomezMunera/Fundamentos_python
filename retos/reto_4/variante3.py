
"""
reto 4 variante 3
"""

#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la clase cliente
#from pruebas import pruebas_codigo_estudiante
from cliente import cliente
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
    suma_retiros = 0
    suma_consignaciones = 0
    edad_minima_retiro = -1
    edad_minima_info = -1
    edad_minima_consignacion = -1
    
    for i in cola_general:
        
        if i.fila_interes == "caja":
            cola_caja.append(i.nombre)
        elif i.fila_interes == "info":
            cola_info.append(i.nombre)
            if i.edad <= edad_minima_info or edad_minima_info == -1:
                edad_minima_info = i.edad
            
        if i.transaccion == "retirar":
            if i.dinero_cuenta_bancaria >= i.cantidad_retirar:
                suma_retiros += i.cantidad_retirar
                if i.edad < edad_minima_retiro or edad_minima_retiro == -1:
                    edad_minima_retiro = i.edad
            
        elif i.transaccion == "consignar":
            suma_consignaciones += i.cantidad_consignar
            if i.edad < edad_minima_consignacion or edad_minima_consignacion == -1:
                edad_minima_consignacion = i.edad
            

    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion

"""
cola_general = [
cliente("Matt",21,235000,"caja","retirar",100000,0),
cliente("Dan",32,658000,"caja","retirar",98000,0),
cliente("Diana",29,87000,"info","ninguna",0,0)
]
"""
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