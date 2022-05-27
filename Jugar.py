import sys
from Board import *

if len( sys.argv ) < 2:
    print( "Usage: python3", sys.argv[ 0 ], "size" )
    sys.exit( 1 )

# end if
tam = int( sys.argv[ 1 ] )

board = Board( tam )

#movimientos: numero,direccion. ejemplo 8,a
#a = arriba
#d = derecha
#i = izquierda
#b = abajo
while not board.have_won( ):
    print( board )
    move = input( 'Movimiento: ' )
    board.moves( move )

print( board )
print('You Won!')

