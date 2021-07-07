"""
reto 4 - variante 1
"""

#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL

def pilaAtras(pila_atras,cad):
    return pila_atras.append(cad)

def pilaAdelante(pila_adelante,cad):
    return pila_adelante.append(cad)

"""Fin espacio para programar funciones propias"""

def actualizar_estado_pestana(operaciones_usuario, pagina_default):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    
    pagina_actual = pagina_default
    pila_atras = []
    pila_adelante = []
    
    for i in operaciones_usuario:
        
        if i == "atras":
            pilaAdelante(pila_adelante, pagina_actual)
            pagina_actual = pila_atras.pop()
                
        elif i == "adelante":
            pilaAtras(pila_atras, pagina_actual)
            pagina_actual = pila_adelante.pop()
            
        else:
            if(i != pagina_actual):
                pilaAtras(pila_atras, pagina_actual)
                pagina_actual = i
                pila_adelante = []

    
    return pila_atras, pagina_actual, pila_adelante

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA
"""
operaciones_usuario = ["udea.edu.co","ingeniaudea.co","twitter.com", "atras",
"atras", "adelante", "facebook.com", "facebook.com"]
pagina_default = "google.com"

sal = actualizar_estado_pestana(operaciones_usuario, pagina_default)

#pruebas_codigo_estudiante(actualizar_estado_pestana)

