import random
import numpy as np
class Board:

    #Atributos
    tam = None
    m_tablero = None
    m_tableroG = None


    def __init__( self, tam):
        self.tam = tam
        self.m_tablero = [[j+i*tam + 1 for j in range(tam)] for i in range(tam)]
        self.m_tableroG = [[j+i*tam + 1 for j in range(tam)] for i in range(tam)]

        self.m_tablero[tam -1][tam-1] = 0
        self.m_tableroG[tam -1][tam-1] = 0
        for i in range(tam):
            random.shuffle(self.m_tablero[i])
        random.shuffle(self.m_tablero)

    def __str__(self):
        s = ""  
        for k in range( len( self.m_tablero ) ):
            s += "+-----"
        s += "+\n"
        for i in range(len( self.m_tablero )):
            for k in range( len( self.m_tablero ) ):
                s += "|     "
            s += "|\n"
            for k in range( len( self.m_tablero ) ):
                if self.m_tablero[i][k] == 0:
                    s += "|  " + " " + "  "
                else:
                    if self.m_tablero[i][k] < 10:
                        s += "|  " + str(self.m_tablero[i][k]) + "  "
                    else:
                        s += "| " + str(self.m_tablero[i][k]) + "  "
            s += "|\n"
            for k in range( len( self.m_tablero ) ):
                s += "|     "
            s += "|\n"
            for k in range( len( self.m_tablero ) ):
                s += "+-----"
            s += "+\n"
        
        return s
    
    def have_won( self ):
        return np.array_equal(self.m_tablero,self.m_tableroG)
    
    def moves( self,move):
        bloqueado = False
        mov = move.split(",")
        if int(mov[0]) != 0:
            tablero = np.array(self.m_tablero)
            result = np.where(tablero == int(mov[0]))
            fila = int(result[0])
            columna = int(result[1])

            #esquina superior izquierda
            if fila == 0 and columna == 0:
                if mov[1] == "d":
                    self.moveDerecha(fila,columna)
                elif mov[1] == "b":
                    self.moveAbajo(fila,columna)
                else:
                    print("movimiento indebido")

            #esquina superior derecha
            elif fila == 0 and columna == self.tam - 1:
                if mov[1] == "i":
                    self.moveIzquierda(fila,columna)
                elif mov[1] == "b":
                    self.moveAbajo(fila,columna)
                else:
                    print("movimiento indebido")
            #cualquiera de la esquina de arriba
            elif fila == 0:
                if mov[1] == "d":
                    self.moveDerecha(fila,columna)
                elif mov[1] == "b":
                    self.moveAbajo(fila,columna)
                elif mov[1] == "i":
                    self.moveIzquierda(fila,columna)
                else:
                    print("movimiento indebido")
            
            
            
            #esquina inferior izquierda
            elif fila == self.tam - 1 and columna == 0:
                if mov[1] == "a":
                    self.moveArriba(fila,columna)
                elif mov[1] == "d":
                    self.moveDerecha(fila,columna)
                else:
                    print("movimiento indebido")

            #esquina inferior derecha
            elif fila == self.tam - 1 and columna == self.tam - 1:
                if mov[1] == "a":
                    self.moveArriba(fila,columna)
                elif mov[1] == "i":
                    self.moveIzquierda(fila,columna)
                else:
                    print("movimiento indebido")

            #Cualquiera de la esquina inferior
            elif fila == self.tam - 1:
                if mov[1] == "d":
                    self.moveDerecha(fila,columna)
                elif mov[1] == "a":
                    self.moveArriba(fila,columna)
                elif mov[1] == "i":
                    self.moveIzquierda(fila,columna)
                else:
                    print("movimiento indebido")

            #Cualquiera de la esquina izquierda
            elif columna == 0:
                if mov[1] == "d":
                    self.moveDerecha(fila,columna)
                elif mov[1] == "a":
                    self.moveArriba(fila,columna)
                elif mov[1] == "b":
                    self.moveAbajo(fila,columna)
                else:
                    print("movimiento indebido")

            #Cualquiera de la esquina derecha
            elif columna == self.tam - 1:
                if mov[1] == "i":
                    self.moveIzquierda(fila,columna)
                elif mov[1] == "a":
                    self.moveArriba(fila,columna)
                elif mov[1] == "b":
                    self.moveAbajo(fila,columna)
                else:
                    print("movimiento indebido")

            else:
                if mov[1] == "i":
                    self.moveIzquierda(fila,columna)
                elif mov[1] == "a":
                    self.moveArriba(fila,columna)
                elif mov[1] == "b":
                    self.moveAbajo(fila,columna)
                elif mov[1] == "d":
                    self.moveDerecha(fila,columna)
                else:
                    print("movimiento indebido")
        
        else:
            print("movimiento indebido")


    def moveDerecha(self,fila,columna):
        if self.m_tablero[fila][columna + 1] == 0:
            print("mover derecha")
            self.m_tablero[fila][columna], self.m_tablero[fila][columna + 1] = self.m_tablero[fila][columna + 1], self.m_tablero[fila][columna]
        else:
            print("espacio no disponible. Ocupado por ",self.m_tablero[fila][columna + 1])
    
    def moveAbajo(self,fila,columna):
        if self.m_tablero[fila + 1][columna] == 0:
            print("mover abajo")
            self.m_tablero[fila][columna], self.m_tablero[fila + 1][columna] = self.m_tablero[fila + 1][columna], self.m_tablero[fila][columna]
        else:
            print("espacio no disponible. Ocupado por ",self.m_tablero[fila + 1][columna])
    
    def moveIzquierda(self,fila,columna):
        if self.m_tablero[fila][columna - 1] == 0:
            print("mover izquierda")
            self.m_tablero[fila][columna], self.m_tablero[fila][columna - 1] = self.m_tablero[fila][columna - 1], self.m_tablero[fila][columna]
        else:
            print("espacio no disponible. Ocupado por ",self.m_tablero[fila][columna - 1])

    def moveArriba(self,fila,columna):
        if self.m_tablero[fila - 1][columna] == 0:
            print("mover izquierda")
            self.m_tablero[fila][columna], self.m_tablero[fila - 1][columna] = self.m_tablero[fila - 1][columna], self.m_tablero[fila][columna]
        else:
            print("espacio no disponible. Ocupado por ",self.m_tablero[fila - 1][columna])       
         
        
                        