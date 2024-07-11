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

        self.funcionMovimientos = { #Diccionario con las funciones de los movimientos de las piezas 
            'P': self.movimientoPeones,
            'R': self.movimientoTorres,
            'N': self.movimientoCaballos,
            'B': self.movimientoAlfiles,
            'Q': self.movimientoReinas,
            'K': self.movimientoReyes
        } 

        self.movimientoBlancas = True
        self.historialMovimientos = [] #Lista auxiliar para almacenar el historial de los movimientos 
        
    def tableroConsola(self): #Imprimir el estado actual del tablero en la consola
        print("\nTABLERO JUEGO")
        for fila in range(8):
            print(self.tablero[fila])
        return f"Historial de movimientos: {self.historialMovimientos}" #Retornar el historial de movimientos

    def hacerJugada(self, jugada): #Funcion para realizar un movimiento en el tablero 
        self.tablero[jugada.filaInicial][jugada.columnaInicial] = "--" #La posicion inicial de la pieza ahora estara vacia 
        self.tablero[jugada.filaFinal][jugada.columnaFinal] = jugada.piezaMovida #El tablero se actualiza con la pieza movida a su nueva casilla, dejando la posicion inicial vacia 
        self.historialMovimientos.append(jugada) #Guardar la jugada en el historial de movimientos relaizadas 
        self.movimientoBlancas = not self.movimientoBlancas #Indicar que ya no es el turno de las blancas 

    def deshacerJugada(self): #Funcion para deshacer la ultima jugada realizada en el tablero 
        if len(self.historialMovimientos) != 0: #Si el historial de movimientos contiene jugadas
            movimiento = self.historialMovimientos.pop() #Obtener la jugada de la lista y eliminarlo en el historial
            self.tablero[movimiento.filaInicial][movimiento.columnaInicial] = movimiento.piezaMovida #Regresar a la posicion inicial de la pieza a mover
            self.tablero[movimiento.filaFinal][movimiento.columnaFinal] = movimiento.piezaCapturada #Regresar la pieza que habia en la pieza capturada (la posicion jugada por las blancas )
            self.movimientoBlancas = not self.movimientoBlancas #Indicar que ya no es el turno de las blancas 

            # Verificar el turno actual
            if self.movimientoBlancas: #Validar de quien es el turno despues de deshacer la jugada 
                print("Turno de las blancas después de deshacer.")
            else: #Entonces no es el turno de las blancas
                print("Turno de las negras después de deshacer.")

    def movimientosValidos(self): #Las jugadas validas que si se pueden realizar
        return self.movimientosPosibles()

    def movimientosPosibles(self): #Las jugadas posibles que se pueden realizar, sin validar jaques o otras preocupaciones
        movimientos = [] #Lista con los movimientos posibles para que las piezas puedan hacer sus jugadas en los movimiento contenidos dentro de esta lista
        for fila in range(len(self.tablero)): #Recorrer las filas del tablero  
            for columna in range(len(self.tablero[fila])): #Recorrer las columnas de acuerdo con la fila del tablero
                turno = self.tablero[fila][columna][0] #Validar de quien es el turno obteniendo la inicial de la pieza, por ejemplo: "bPawn" o "wPawn"

                if (turno == 'w' and self.movimientoBlancas) or (turno == 'b' and not self.movimientoBlancas): #Validar de quien es el turno para realizar una jugada 
                    pieza = self.tablero[fila][columna][1] #Obtener la pieza con la segunda inicial del nombre de la pieza

                    # self.funcionMovimientos
                    # Utilizar el diccionario como un Switch 

                    #Validar cada una de las piezas del tablero 
                    if pieza == 'P': #Si la pieza es un peon
                        self.movimientoPeones(fila, columna, movimientos)
                    elif pieza == 'R': #Si la pieza es una torre
                        self.movimientoTorres(fila, columna, movimientos)

        return movimientos #Retornar la lista con los movimientos validos 


    def movimientoPeones(self, fila, columna, movimientos): #Agregar a la lista todos los movimientos validos del peon
        #El peon tiene tres movimientos
            #1. Avanzar una casilla hacia adelante
            #2. Si el peon avanza por primera vez y no hay ninguna pieza bloqueandolo, puede avanzar dos casillas
            #3. Comer piezas en diagonal/cruzado
            #El peon tambien tiene una regla especial, el peon pasante 

        if self.movimientoBlancas: #Validar si es el movimiento de las blancas
            #Movimiento de las blancas
            if self.tablero[fila-1][columna] == '--': #Validar si existe una pieza delante del peon 
                movimientos.append(Movimiento((fila, columna), (fila-1, columna), self.tablero)) #Avanzar una casilla: Agregar movimientos validos del peon para avanzar una casilla
                if fila == 6 and self.tablero[fila-2][columna] == '--': #Validar si es el primer movimiento y que no existan piezas bloqueando la casilla 
                    movimientos.append(Movimiento((fila, columna), (fila-2, columna), self.tablero)) #Avanzar dos casillas: Agregar movimientos validos del primer movimiento del peon para avanzar dos casillas 

            if columna-1 >= 0: #Validar que no exceda los limites del tablero 
                if self.tablero[fila-1][columna-1][0] == "b": #Validar si la pieza es negra y no blanca
                    movimientos.append(Movimiento((fila, columna), (fila-1, columna-1), self.tablero)) #Generar un movimiento y eliminar la pieza negra por la izquierda
            if columna+1 <= 7: #Validar que no exceda los limites del tablero
                if self.tablero[fila-1][columna+1][0] == "b": #Validar si la pieza es negra y no blanca
                    movimientos.append(Movimiento((fila, columna), (fila-1, columna+1), self.tablero)) #Generar un movimiento y eliminar la pieza negra por la derecha 

        else: #Entonces ya no es turno de las blancas 
            movimientos.append(Movimiento((fila,columna), (fila+1,columna), self.tablero)) 
            #Generar los movimientos de los peones negros
            #...
            #...
            
    def movimientoTorres(self, fila, columna, movimiento): #Agregar a la lista todos los movimientos validos de la torre 
        pass

    def movimientoCaballos(self, fila, columna, movimiento): #Agregar a la lista todos los movimientos validos del caballo
        pass

    def movimientoAlfiles(self, fila, columna, movimiento): #Agregar a la lista todos los movimientos validos del alfil
        pass

    def movimientoReinas(self, fila, columna, movimiento): #Agregar a la lista todos los movimientos validos de la reina 
        pass

    def movimientoReyes(self, fila, columna, movimiento): #Agregar a la lista todos los movimientos validos del rey
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
        self.IDmovimiento = self.filaInicial * 1000 + self.columnaInicial * 100 + self.filaFinal * 10 + self.columnaFinal #Obtener un ID unico para cada movimiento (es random)
        # print("ID de la jugada: ", self.IDmovimiento) #Imprimir el ID de las jugadas

    def __eq__(self, otro):
        if isinstance(otro, Movimiento):
            return self.IDmovimiento == otro.IDmovimiento
        return False 

    def obtenerNotacion(self): #Obtener la notacion de ajedrez 
        return self.obtenerRangoFila(self.filaInicial, self.columnaInicial) + self.obtenerRangoFila(self.filaFinal, self.columnaFinal)

    def obtenerRangoFila(self, fila, columna): #Obtener la posicion de la pieza
        return self.columnasToFilas[columna] + self.filasToRangos[fila] #A4, B7, H6, B4... 


    #Notacion para describir los movimientos de la clase Movimiento 
    def __str__(self):
        return f"{self.piezaMovida} mueve de {self.obtenerRangoFila(self.filaInicial, self.columnaInicial)} a {self.obtenerRangoFila(self.filaFinal, self.columnaFinal)}"

    def __repr__(self):
        return f"Movimiento({self.obtenerNotacion()})"