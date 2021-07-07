# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:08:45 2021

@author: Digital
"""

def print_msg(number):
    def printer():
        "Aqui estamos usando la palabra clave nolocal"
        #nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)