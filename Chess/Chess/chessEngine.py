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

    def hacerJugada(self, jugada): #Funcion para realizar un movimiento en el tablero 
        self.tablero[jugada.filaInicial][jugada.columnaInicial] = "--"
        self.tablero[jugada.filaFinal][jugada.columnaFinal] = jugada.piezaMovida #El tablero se actualiza con la pieza movida 
        self.historialMovimientos.append(jugada) #Guardar la jugada en el historial de movimientos relaizadas 
        self.movimientoBlancas = not self.movimientoBlancas #Un movimiento de las blancas no puede realizarse en su misma posicion, deben de ser diferentes coordenadas dentro del tablero

    def deshacerJugada(self): #Funcion para deshacer la ultima jugada realizada en el tablero 
        if len(self.historialMovimientos) != 0: #Si el historial de movimientos contiene jugadas
            movimiento = self.historialMovimientos.pop() #Obtener la jugada de la lista y eliminarlo en el historial
            self.tablero[movimiento.filaInicial][movimiento.columnaInicial] = movimiento.piezaMovida
            self.tablero[movimiento.filaFinal][movimiento.columnaFinal] = movimiento.piezaCapturada
            self.movimientoBlancas = not self.movimientoBlancas

    def movimientosValidos(self): #Las jugadas validas que si se pueden realizar
        return self.movimientosPosibles()

    def movimientosPosibles(self): #Las jugadas posibles que se pueden realizar, sin validar jaques o otras preocupaciones
        movimientos = [Movimiento((6,4), (4,4), self.tablero)]
        for fila in range(len(self.tablero)): #Recorrer las filas del tablero  
            for columna in range(len(self.tablero[fila])): #Recorrer las columnas de acuerdo con la fila del tablero
                turno = self.tablero[fila][columna][0] #Obtener una casilla
                if (turno == 'w' and self.movimientoBlancas) and (turno == 'b' and not self.movimientoBlancas):
                    pieza = self.tablero[fila][columna][1]

                    #Validar cada una de las piezas del tablero 
                    if pieza == 'p': #Si la pieza es un peon
                        self.movimientoPeones(fila, columna, movimientos)
                    elif pieza == 'r': #Si la pieza es una torre
                        self.movimientoTorres(fila, columna, movimientos)

        return movimientos #Retornar la lista con los movimientos validos 
    
    def movimientoPeones(self, fila, columna, movimiento):
        pass

    def movimientoTorres(self, fila, columna, movimiento):
        pass

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
        self.IDmovimiento = self.filaFinal * 1000 + self.columnaInicial * 100 + self.filaFinal * 10 + self.columnaFinal #Obtener un ID unico para cada movimiento (es random)
        print(self.IDmovimiento)

    def __eq__(self, otro):
        if isinstance(otro, Movimiento):
            return self.IDmovimiento == otro.IDmovimiento
        return False 

    def obtenerNotacion(self): #Obtener la notacion de ajedrez 
        return self.obtenerRangoFila(self.filaInicial, self.columnaInicial) + self.obtenerRangoFila(self.filaFinal, self.columnaFinal)

    def obtenerRangoFila(self, fila, columna): #Obtener la posicion de la pieza
        return self.columnasToFilas[columna] + self.filasToRangos[fila] #A4, B7, H6, B4... 