# -*- coding: utf-8 -*-
"""
Created on Sat May 29 09:19:26 2021

@author: Digital
"""

# tablas

# controlador
control = 1


n = int(input("Ingesar el entero hasta el cual obtener la tabla: "))

while control <= n:
    i = 1
    while i <= 10:
        if (i == 8):
            continue
        res = control * i
        print(control,"*", i ,"=",res)
        
        i = i + 1
        
    print("")
    control = control + 1
