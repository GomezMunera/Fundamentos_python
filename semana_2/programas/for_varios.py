# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:44:50 2021

@author: Digital
"""

# In[]:
# for con variable anonima

for _ in range(10):
    print("*", end = "\t")
    
# In[]
# declaración break
num = int(input('Entre un número para verificar con el for: '))
for i in range(0, 6):
	if i == num:
		break
	print(i, ' ', end='')
print('Hecho')

# In[]
# declaración continue
for i in range(0, 10):
	print(i, ' ', end='')
	if i % 2 == 1:
		continue
	print('Es un número par')
print('Programa finalizado')
