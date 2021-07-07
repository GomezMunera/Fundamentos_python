# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:09:11 2021

@author: Digital
"""

num = int(input('Ingrese un número: '))
for i in range(0, 6):
    if i == num:
        break
    print(i, ' ', end='')
else:
        print(sep="\n")
print('Programa finalizado correctamente')
