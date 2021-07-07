
fichas=["\u2654", "\u2655", "\u2656", "\u2657",
        "\u2658", "\u2659", "\u265A", "\u265B",
        "\u265C", "\u265D", "\u265E", "\u265F"
        ]


class ajedrez():
    
    fichas=["\u2654", "\u2655", "\u2656", "\u2657",
        "\u2658", "\u2659", "\u265A", "\u265B",
        "\u265C", "\u265D", "\u265E", "\u265F"
        ]
    
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
    
    def construir_tablero(self):
        self.tablero= [[" " for i in range(8)] for j in  range(8) ]
        
    def ponerfichas(self):
        
        for i in range(8):
            self.tablero[1][i] = self.peonB
            
        for i in range(8):
            self.tablero[6][i] = self.peonN
        
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
        
    def mostrar(self):
        
        for fil in self.tablero:
            for elementos in fil:
                print(elementos, end=" ")
            print()  
        


miajedrez=ajedrez()
miajedrez.construir_tablero()
miajedrez.ponerfichas()
miajedrez.tablero
        

class tablero():
    
    def __init_(self):
        
        self.peon1=peon()
    

class peon():
    pass
    
    
    
    
    


    
    
    