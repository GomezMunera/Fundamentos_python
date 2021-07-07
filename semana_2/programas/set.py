# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:05:25 2021

@author: Digital
"""

# set

numeros={1,2,3,5,4}
frutas={"manzana", "peras","higos"}

# In[20]:


tienda=numeros.union(frutas)
print(tienda)

print('higos' in tienda)

nuevo=tienda.intersection(frutas)
print(nuevo)

dif=tienda.difference(frutas)
print(dif)

# In[]:

tienda.add("uvas")
print(tienda)

# In[]:

tienda.remove('higos')
print(tienda)