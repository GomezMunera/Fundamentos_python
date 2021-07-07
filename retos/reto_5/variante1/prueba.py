# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 08:00:49 2021

@author: Digital
"""

import csv
 
with open('TSLA.csv') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=',')
    datos = []
    valor = []
    concepto = []
    menor = []
    mayor = []
    for row in reader:
        
        datos.append(row["Date"])
        valor.append(float(row["Adj Close"]))
        concepto.append("")
        menor.append(float(row["Low"]))
        mayor.append(float(row["High"]))
          
 
with open('analisis_archivo.csv', newline='', mode= 'w') as csvfile:
        campos = ['Fecha', 'Concepto']
        writer = csv.DictWriter(csvfile, fieldnames=campos, delimiter='\t')
        writer.writeheader()
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
                
            
            writer.writerow({'Fecha': datos[i], 'Concepto': concepto[i]})
            
            