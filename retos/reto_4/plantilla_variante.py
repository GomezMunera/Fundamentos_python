#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
from pruebas import pruebas_codigo_estudiante
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL




"""Fin espacio para programar funciones propias"""

def actualizar_estado_editor(operaciones_usuario):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    texto_escrito = []
    texto_actual = ""
    rehacer = []
    
    for i in operaciones_usuario:
        if i == "DESHACER":
            texto_actual = texto_estrito.pop()
            
        elif(i == "REHACER"):
            
        else:
            texto_escrito.append(texto_actual)
            texto_actual = i
        
    cadena_final = "".join(texto_escrito) + texto_actual
    
    return cadena_final


#operaciones_usuario = ["hola", "mundo","DESHACER"]

#actualizar_estado_editor(operaciones_usuario)

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
pruebas_codigo_estudiante(actualizar_estado_editor)