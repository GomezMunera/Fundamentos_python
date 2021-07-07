# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:15:23 2021

@author: Digital
"""

cad = "NOS HAN PICADO LOS MOSQUITOS"

b = cad.split()

c = list(cad)

# In[]
word = "Easy"
x = list(word)
print(x)

# In[]

# variante 1

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'
            ,'P','Q','R','S','T','U','V','W','X','Y','Z']
morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..'
         ,'.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
         '...','-','..-','...-','.--','-..-','-.--','--..']

print(len(alfabeto))
print(len(morse))

cad_prueba = "NOS HAN PICADO LOS MOSQUITOS"

cad_palabras = cad_prueba.split()

print(len(cad_palabras))

cad_morse = []

for i in range(len(cad_palabras)):
    dividida = list(cad_palabras[i])
    for j in range(len(dividida)):
        k = alfabeto.index(dividida[j])
        cad_morse.append(morse[k])
    if i == len(cad_palabras) - 1:
        pass
    else:
        cad_morse.append("/")
    
salida = " ".join(cad_morse)

print(salida)
print(type(salida))

# In[]
# variante 2

cad_entrada_morse = "-. --- ... / .... .- -. / .--. .. -.-. .- -.. --- / .-.. --- ... / -- --- ... --.- ..- .. - --- ..."

cad_morse_div = cad_entrada_morse.split()

print(len(cad_morse_div))

cad_pal_salida = []

for i in range(len(cad_morse_div)):
    if (cad_morse_div[i] == "/"):
        cad_pal_salida.append(" ")
    else:
        p = morse.index(cad_morse_div[i])
        cad_pal_salida.append(alfabeto[p])
    
salida_palabras = "".join(cad_pal_salida)