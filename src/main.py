from Deck import Deck
from Jugador import Jugador
from Partida import Partida
from Tablero import Tablero
import Cartas


def main():
    partida = Partida();
    # Referenciamos el espacio de memoria de jugador 1 y jugador 2 para guardalos
    #Partida tiene un tablero y ese tablero tiene 2 jugadores, de ahi los referenciamos
    j1 = partida.__tablero.getJugador1()

    #comprobamos que guarde los nombres correctamente
    print(j1.stringOf())


    #Hacer una prueba de ver q los datos se modifiquen




#llamado de la funcion main
main()

