# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 08:22:16 2021

@author: Digital
"""

def cambiarFilas(A,i,j):
    for z in range(len(A[0])):
        temp = A[i][z]
        A[i][z] = A[j][z]
        A[j][z] = temp

# In[]
def sumaFilas(A):
    vec_suma = []
    for f in range(len(A)):
        s = 0
        for c in range(len(A[0])):
            s = s + A[f][c]
        vec_suma.append(s)
    return vec_suma