# cheesMain se utiliza para manejar las entradas del usuario, ademas de mostrar la situacion actual del juego

#Librerias
import pygame as p
from Chess import chessEngine

# Tablero 
anchura = 512 #Tamaño px de anchura para el tablero 
altura = 512 #Tamaño px de altura para el tablero 
#Tambien es posible utilizar ''400' para la anchura y altura del juego 
dimension = 8 #Cantidad de casillas por fila 
maxFPS = 15 #Fotogramas para animaciones 
tamañoCuadros = anchura // dimension #Tamaño de los 64 cuadros para el tablero 
imagenes = {} #Diccionario con las imagenes de las piezas

#Cargar las imagenes de las piezas del tablero 
def cargarImagenes():
    piezas = ['bPawn', 'bKnight', 'bBishop', 'bRook', 'bQueen', 'bKing', 'wPawn', 'wKnight', 'wBishop', 'wRook', 'wQueen', 'wKing'] #Lista con el nombre de las piezas dentro de la carpeta "imagenesPiezas"

    for pieza in piezas: #Iterar las imagenes dentro de la carpeta "imagenesPiezas"
        imagenes[pieza] = p.transform.scale(p.image.load("Chess/imagenesPiezas/" + pieza + ".png"), (tamañoCuadros, tamañoCuadros)) #Cargar cada una de las imagenes de las piezas del juego 
        #De igual manera se realiza un escalado de imagenes 

#Dibujar los cuadros del tablero
#Nota: El cuadro superior izquierdo siempre es de color blanco 
def dibujarTablero(pantalla):
    #Variables para los colores
    colorBlanco = p.Color(238,239,233)
    colorNegro = p.Color(37, 111, 135)
    colores = [p.Color(colorBlanco), p.Color(colorNegro)] #Definir los colores para el tablero
    for fila in range(dimension): #Filas del tablero 
        for columna in range(dimension): #Columnas del tablero 
            color = colores[((columna + fila) % 2)] #El color se obtiene calculando la posicion del cuadro dentro del tablero
            #Ejemplo de posiciones de los cuadros:
                # cuadro(1,1) = 1 + 1 = 2 | ¿Residuo de 2?: 0 -> El color "0" es "coloBlanco"
                # cuadro(1,2) = 1 + 2 = 3 | ¿Residuo de 3?: 1 -> El color "1" es "colorNegro"
                #... 
            p.draw.rect(pantalla, color, p.Rect(columna*tamañoCuadros, fila*tamañoCuadros, tamañoCuadros, tamañoCuadros)) #Dibujar el rectangulo con el color correspondiente 

#Dibujar las piezas dentro del tablero, utilizando el estado actual del tablero 
def dibujarPiezas(pantalla, tablero):
    for fila in range(dimension): #Filas del tablero 
        for columna in range(dimension): #Columnas del tablero 
            pieza = tablero[fila][columna] #Obtener la pieza del tablero 
            if pieza != "--": #Validar que no sea una casilla vacia 
                pantalla.blit(imagenes[pieza], p.Rect(columna*tamañoCuadros, fila*tamañoCuadros, tamañoCuadros, tamañoCuadros)) #Dibujar una pantalla con las imagenes y rectangulos definidos 

# Dibujar el estado actual del tablero 
def dibujarEstadoJuego(pantalla, estadoJuego):
    dibujarTablero(pantalla) #Dibujar el tablero
    dibujarPiezas(pantalla, estadoJuego.tablero) #Dibujar las piezas del tablero con la posicion actual

#Funcion principal
def main():
    p.init() #Inicializar la libreria 
    pantalla = p.display.set_mode((anchura, altura)) #Definir el tamaño de la pantalla 
    reloj = p.time.Clock()
    pantalla.fill(p.Color("White"))
    estadoJuego = chessEngine.gameState() #Acceder a la clase "gameState" que esta dentro del archivo "chessEngine" 
    cargarImagenes() #Cargar imagenes 
    print(estadoJuego.tablero)

    #Variables auxiliares
    bandera = True #Variable auxiliar para el while

    while bandera: #Ejecutar mientras que sea verdadero
        for x in p.event.get(): #Esperar a obtener un evento 
            if x.type == p.QUIT: #Si el evento es QUIT
                bandera = False #Salir del ciclo 
        
        dibujarEstadoJuego(pantalla, estadoJuego) #Dibujar el estado actual del juego 
        reloj.tick(maxFPS) #El juego no se ejecuta a mas de "maxFPS" fotogramas por segundo 
        p.display.flip() #Doble buffering, se intercambian los buffers, mostrando el buffer fuera de la pantalla en la pantalla y ocultando el buffer previamente visible.

if __name__ == "__main__":
    main() #Ejecutar programa principal 
