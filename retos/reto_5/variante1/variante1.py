# -*- coding: utf-8 -*-
"""
reto 5 variante 1
"""

#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento del módulo csv respectivamente
#from pruebas import pruebas_codigo_estudiante
import csv
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)



"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    
    with open('TSLA.csv') as csvfile:
        reader = csv.DictReader(csvfile,delimiter=',')
        datos = []
        valor = []
        concepto = []
        menor = []
        mayor = []
        for row in reader:

            datos.append(row["Date"])
            valor.append(float(row["Close"]))
            concepto.append("")
            menor.append(float(row["Low"]))
            mayor.append(float(row["High"]))
              
     
    with open('analisis_archivo.csv', newline='', mode= 'w') as csvfile:
            campos = ['Fecha', 'Concepto']
            writer = csv.DictWriter(csvfile, fieldnames=campos, delimiter='\t')
            writer.writeheader() # usado con DictWriter
            
            # writer solo
            #writer = csv.writer(csvfile, delimiter='\t')
            #writer.writerow(['Fecha','Concepto']) #usado con writer solo
            
            for i in range(len(datos)):
                if valor[i] < 200:
                    concepto[i] = "MUY BAJO"
                elif valor[i] >= 200 and valor[i] < 300:
                    concepto[i] = "BAJO"
                elif valor[i] >= 300 and valor[i] < 500:
                    concepto[i] = "MEDIO"
                elif valor[i] >= 500 and valor[i] < 600:
                    concepto[i] = "ALTO"
                elif valor[i] >= 600:
                    concepto[i] = "MUY ALTO"
                    
                
                # DictWriter
                writer.writerow({'Fecha': datos[i], 'Concepto': concepto[i]})
                #usar con writer solo
                #writer.writerow([datos[i], concepto[i]])
                
    
    valor_min = min(menor)
    in_min = menor.index(valor_min)
    
    valor_max = max(mayor)
    in_max = mayor.index(valor_max)
    
    date_lowest = datos[in_min]
    lowest_value = menor[in_min]
    
    date_highest = datos[in_max]
    highest_value = mayor[in_max]
    
    return date_lowest, lowest_value, date_highest, highest_value

sal = solucion()

"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#pruebas_codigo_estudiante(solucion)