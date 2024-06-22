# cheesEngine es una clase para almacenar toda la informacion acerca del estado actual del juego, con el fin
# de poder determinar las siguientes jugadas, y las cuales deben de ser validas para continuar con el juego

class gameState():
    def __init__(self):

        # El tablero es una lista bidimensional de 8x8
        # Los elementos estan compuestos por dos elementos principales:
            # El primer elemento es: "b" | "w"
            # Representa el color de las piezas para el juego, en donde "b": negras y "w": blancas

            # El segundo elemento representa el nombre de las piezas en ingles:
                # Pawn: Peon 
                # Rook: Torre
                # Knight: Caballo
                # Bishop: Alfil
                # Queen: Reina
                # King: Rey

        self.tablero = [ #Lista de listas con el contenido del tablero de Ajedrez 
            ['bRook','bKnight', 'bBishop', 'bQueen', 'bKing', 'bBishop', 'bKnight', 'bRook'], #Fila de piezas principales negros 
            ['bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn'], #Fila de peones negros
            ['--', '--', '--', '--', '--', '--', '--', '--'], #Fila vacia 
            ['--', '--', '--', '--', '--', '--', '--', '--'], #Fila vacia 
            ['--', '--', '--', '--', '--', '--', '--', '--'], #Fila vacia 
            ['--', '--', '--', '--', '--', '--', '--', '--'],#Fila vacia
            ['wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn'], #Fila de peones blancos
            ['wRook','wKnight', 'wBishop', 'wQueen', 'wKing', 'wBishop', 'wKnight', 'wRook'], #Fila de piezas principales blancos 
        ] #Fin de la lista de listas