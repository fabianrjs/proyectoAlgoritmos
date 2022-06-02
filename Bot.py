import math
import numpy as np

from Nodo import Nodo

class Bot:
    def __init__( self, m_tableroG):
        self.m_tableroGanador = m_tableroG

    def have_won( self, tablero ):
        return np.array_equal(tablero, self.m_tableroGanador)

    def jugar( self, tablero ):
        pila_de_movimientos = []
        tablero_padre = tablero

        arbol = Nodo(tablero, None, None)

        while not self.have_won(tablero):
            
            movimientos = [ 'a', 'b', 'i', 'd' ]
            posicionCasillaVacia = np.where( np.array(tablero) == 0 )
            ( fila, columna ) = ( posicionCasillaVacia[ 0 ], posicionCasillaVacia[ 1 ] )
            
            if fila == 0:
                movimientos.remove('a')
            if fila == len( tablero ) - 1:
                movimientos.remove('b')
            if columna == 0:
                movimientos.remove('i')
            if columna == len( tablero ) - 1:
                movimientos.remove('d')


            hijos = []
            hijos_move = []

            '''print('Tablero ------------')
            for i in range( len(tablero) ):
                print( tablero[i] )'''

            for movimiento in movimientos:
                hijo = self.mover( movimiento, posicionCasillaVacia, np.copy(tablero) )
                if not np.array_equal(tablero_padre, hijo ):
                    hijos.append( hijo )
                    hijos_move.append( movimiento )

            min_heurstica = math.inf
            min_movimiento = ''

            for i in range( len( hijos ) ):
                if self.heuristica( hijos[i] ) < min_heurstica:
                    tablero_padre = np.copy( tablero )
                    tablero = hijos[ i ]
                    min_heurstica = self.heuristica( hijos[i] )
                    min_movimiento = hijos_move[ i ]
            
            print('---------------\n')
            for i in range( len(tablero) ):
                print( tablero[i] )

            #input()

            pila_de_movimientos.append( min_movimiento )

            movimientos.clear()
            hijos.clear()

        return pila_de_movimientos

    def moveDerecha(self, fila, columna, tablero):
        tablero[fila][columna], tablero[fila][columna + 1] = tablero[fila][columna + 1], tablero[fila][columna]
    
    def moveAbajo(self,fila,columna, tablero):
        tablero[fila][columna], tablero[fila + 1][columna] = tablero[fila + 1][columna], tablero[fila][columna]
        
    def moveIzquierda(self,fila,columna, tablero):
        tablero[fila][columna], tablero[fila][columna - 1] = tablero[fila][columna - 1], tablero[fila][columna]

    def moveArriba(self, fila, columna, tablero):
        tablero[fila][columna], tablero[fila - 1][columna] = tablero[fila - 1][columna], tablero[fila][columna]

    def mover(self, movimiento, casillaVacia, tablero ):
        if movimiento == 'a':
            self.moveArriba( int( casillaVacia[0] ), int( casillaVacia[1] ), tablero )
        elif movimiento == 'b':
            self.moveAbajo( int( casillaVacia[0] ), int( casillaVacia[1] ), tablero )
        elif movimiento == 'i':
            self.moveIzquierda( int( casillaVacia[0] ), int( casillaVacia[1] ), tablero )
        elif movimiento == 'd':
            self.moveDerecha( int( casillaVacia[0] ), int( casillaVacia[1] ), tablero )
        return tablero

    def heuristica(self, hijo):
        H = 0
        tablero = np.array(hijo)
        tableroG = np.array( self.m_tableroGanador )

        for i in range(1, len( self.m_tableroGanador ) * len( self.m_tableroGanador )):
            posTablero = np.where(tablero == i)
            posTableroG = np.where(tableroG == i)

            #calcular la distancia
            distFila = abs( int(posTableroG[0]) - int(posTablero[0]))
            #print("distFila: ", distFila)
            disColumna = abs( int(posTableroG[1]) - int(posTablero[1]))
            #print("disColumna: ", disColumna)
            #print("i: ", i, " distancia a su posicion objetivo: " ,distFila + disColumna)
            H += distFila + disColumna

        return H