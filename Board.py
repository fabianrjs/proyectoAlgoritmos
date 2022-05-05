class Board:
    def __init__( self, tam):
        self.tam = tam
    
    def have_won( self ):
        return True
    
    def moves( self, move):
        print('moves\n' )