class Nodo:
    def __init__(self, tablero, movimiento, heuristica) :
        self.tablero = tablero
        self.movimiento = movimiento
        self.heuristica = heuristica

        self.hijo1 = None
        self.hijo2 = None
        self.hijo3 = None
        self.hijo4 = None