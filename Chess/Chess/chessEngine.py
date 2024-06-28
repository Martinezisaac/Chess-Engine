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
            ['--', '--', '--', '--', '--', '--', '--', '--'], #Fila vacia
            ['wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn'], #Fila de peones blancos
            ['wRook','wKnight', 'wBishop', 'wQueen', 'wKing', 'wBishop', 'wKnight', 'wRook'], #Fila de piezas principales blancos 
        ] #Fin de la lista de listas

        self.movimientoBlancas = True
        self.historialMovimientos = [] #Lista auxiliar para almacenar el historial de los movimientos 

    def hacerJugada(self, jugada):
        self.tablero[jugada.filaInicial][jugada.columnaInicial] = "--"
        self.tablero[jugada.filaFinal][jugada.columnaFinal] = jugada.piezaMovida #El tablero se actualiza con la pieza movida 
        self.historialMovimientos.append(jugada) #Guardar la jugada en el historial de movimientos relaizadas 
        self.movimientoBlancas = not self.movimientoBlancas #El movimiento de las blancas no puede ser su mismo movimiento, deben de ser diferentes 
class Movimiento():
    # La clase Movimiento almacenara los movimiento y las piezas del tablero

    #Notacion del juego | Diccionarios para crear la notacion 
    rangosToFilas = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0} #Obtener las filas 
    filasToRangos = {v: k for k, v in rangosToFilas.items()} #Crear diccionario con los pares clave-valor
    # Donde v = posiciones del tablero de ajedrez y k = posiciones de la matriz del tablero 

    filasToColumnas = {"a": 0, "b": 1, "c":2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7} #Obtener las columans 
    columnasToFilas = {v: k for k, v in filasToColumnas.items()} #Crear diccionario con los pares clave-valor
    # Donde v = posiciones del tablero de ajedrez y k = posiciones de la matriz del tablero

    def __init__(self, cuadroInicial, cuadroFinal, tablero):
        self.filaInicial = cuadroInicial[0] #Tomar el primer elemento (fila) del cuadro del primer clic 
        self.columnaInicial = cuadroInicial[1] #Tomar el segundo elemento (columna) del cuadro del primer clic
        self.filaFinal = cuadroFinal[0] #Tomar el primer elemento (fila) del cuadro del segundo clic 
        self.columnaFinal = cuadroFinal[1] #Tomar el segundo elemento (columna) del segundo clic 
        self.piezaMovida = tablero[self.filaInicial][self.columnaInicial] #Posicion inicial de la pieza a mover 
        self.piezaCapturada = tablero[self.filaFinal][self.columnaFinal] #Posicion final de la pieza movida

    def obtenerNotacion(self): #Obtener la notacion de ajedrez 
        return self.obtenerRangoFila(self.filaInicial, self.columnaInicial) + self.obtenerRangoFila(self.filaFinal, self.columnaFinal)

    def obtenerRangoFila(self, fila, columna): #Obtener la posicion de la pieza
        return self.columnasToFilas[columna] + self.filasToRangos[fila] #A4, B7, H6, B4... 

