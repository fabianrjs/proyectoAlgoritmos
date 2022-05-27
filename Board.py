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
                    s += "|  " + str(self.m_tablero[i][k]) + "  "
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
        mov = move.split(",")
        print(mov[0])
        tablero = np.array(self.m_tablero)
        result = np.where(tablero == int(mov[0]))
         
        print(result[0])
        print(result[1])