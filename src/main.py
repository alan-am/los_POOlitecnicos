from Deck import Deck
from Jugador import Jugador
from Partida import Partida
from Tablero import Tablero
import Cartas


def main():
    partida = Partida();
    # Referenciamos el espacio de memoria de jugador 1 y jugador 2 para guardalos
    #Partida tiene un tablero y ese tablero tiene 2 jugadores, de ahi los referenciamos
    j1 = partida.getTablero().getJugador1()
    j2 = partida.getTablero().getJugador2()

    #comprobamos que guarde los nombres correctamente
    print(j1.stringOf())
    print(j2.stringOf())


    #Hacer una prueba de ver q los datos se modifiquen
    partida.getTablero().getJugador1().setNombre("ROSA")
    print(j1.stringOf())



#llamado de la funcion main
main()

