# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

estrella="\u2605"


class ajedrez():
    
    fichas=["\u2654", "\u2655", "\u2656", "\u2657",
            "\u2658", "\u2659", "\u265A", "\u265B",
            "\u265C", "\u265D", "\u265E", "\u265F"
            ]
    
    #tablero= [ [" " for i in range(8)  ] for j in range(8)]
    tablero = []
    for i in range(8):
        tablero.append([" "]*8)
    #tablero=[[0]*8]*8 # GENERA UN ERROR
    
    def __init__(self):
        self.reyN=self.fichas[0]
        self.reinaN=self.fichas[1]
        self.torreN=self.fichas[2]
        self.alfilN=self.fichas[3]
        self.caballoN=self.fichas[4]
        self.peonN=self.fichas[5]
        
        self.reyB=self.fichas[6]
        self.reinaB=self.fichas[7]
        self.torreB=self.fichas[8]
        self.alfilB=self.fichas[9]
        self.caballoB=self.fichas[10]
        self.peonB=self.fichas[11]

        #Peones
        for i in range(8):
            self.tablero[1][i]=self.fichas[11]
            self.tablero[6][i]=self.fichas[5]
        
        #Torres
        self.tablero[0][0]=self.torreB
        self.tablero[0][7]=self.torreB
        self.tablero[7][0]=self.torreN
        self.tablero[7][7]=self.torreN
        
        #Alfiles
        self.tablero[0][2]=self.alfilB
        self.tablero[0][5]=self.alfilB
        self.tablero[7][2]=self.alfilN
        self.tablero[7][5]=self.alfilN
        
        #Caballos
        self.tablero[0][1]=self.caballoB
        self.tablero[0][6]=self.caballoB        
        self.tablero[7][1]=self.caballoN
        self.tablero[7][6]=self.caballoN
        
        #Rey
        self.tablero[0][3]=self.reyB
        self.tablero[7][3]=self.reyN
        
        #Reina
        self.tablero[0][4]=self.reinaB
        self.tablero[7][4]=self.reinaN
        
    def __str__(self):
        self.texto="\n"
        for j in range(8): 
            self.texto+="       "
            for i in range(8):
                self.texto +=self.tablero[i][j] + " "
            self.texto+="\n"
            
        return self.texto



miAjedrez=ajedrez()
print(miAjedrez)




    