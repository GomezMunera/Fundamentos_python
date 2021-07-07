# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:58:05 2021

@author: Digital
"""
def tablas(i,j):
    for i in range(1, i+1):
        for j in range(1, j+1):
            print(f"{i} * {j} = {i*j}")
        print("")