# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:00:58 2021

@author: Digital
"""
import random

class vector:
    def __init__(self, n):
        self.n = n
        self.V =[0]*(n+1)
        
        
    def construyeVector(self,V, n, rango):
        self.V[0] = n
        for i in range(1, n + 1):
            self.V[i] = random.randint(1, rango)
            
    
