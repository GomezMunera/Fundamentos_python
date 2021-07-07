# -*- coding: utf-8 -*-
"""
reto 5 variante 1 con pandas
"""

#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento del módulo csv respectivamente
#from pruebas import pruebas_codigo_estudiante
import csv
import pandas as pd
import numpy as np

"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)



"""Fin espacio para programar funciones propias"""
df = pd.read_csv("TSLA.csv", header=0)

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    # crear archivo 𝑎𝑛𝑎𝑙𝑖𝑠𝑖𝑠_𝑎𝑟𝑐ℎ𝑖𝑣𝑜. 𝑐𝑠𝑣
    # Saving dataframe to CSV
    # crea el dataframe con las dos columnas
    dfp = pd.DataFrame()
    dfp['Fecha'] = None
    dfp = dfp.assign(Concepto=None)

    # asigna la columna date al nuevo dataframe
    dfp["Fecha"] = df["Date"]
   
    conditions = [
        (df["Close"] < 200),
        (df["Close"] >= 200) & (df["Close"] < 300),
        (df["Close"] >= 300) & (df["Close"] < 500),
        (df["Close"] >= 500) & (df["Close"] < 600),
        (df["Close"] >= 600)]
    
    choice =['MUY BAJO','BAJO','MEDIO','ALTO','MUY ALTO']
    
    dfp["Concepto"] = np.select(conditions, choice)
   
    # guarda el dataframe
    dfp.to_csv("analisis_archivo.csv", sep="\t",index=False) 
    
    # retorna las salidas
    lowest_value = df["Low"].min()
    ind_menor = df.index[df['Low'] == lowest_value].tolist()
    date_lowest = df["Date"][ind_menor[0]]
    highest_value = df["High"].max()
    ind_mayor = df.index[df['High'] == highest_value].tolist()
    date_highest = df["Date"][ind_mayor[0]]
    
    return date_lowest, lowest_value, date_highest, highest_value


sal = solucion()

"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#pruebas_codigo_estudiante(solucion)