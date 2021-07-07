# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 00:24:37 2021

@author: Digital
"""

def esNumerico(valor):
    """ returna valor numérico o no"""
    return isinstance(valor, (int,float))

def cadenaVacia(mensaje):
    if(mensaje == "*"):
        return True
    return False