# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:16:01 2021

@author: Digital
"""

def factorial(n):
    if n == 0: # The termination condition
        return 1 # The base case
    else:
        res = n * factorial(n-1) # The recursive call
        return res
    print(factorial(5))