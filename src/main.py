from Deck import Deck
from Jugador import Jugador
from Partida import Partida
from Tablero import Tablero
from Cartas import *


def main():
    partida = Partida();
    # Referenciamos el espacio de memoria de jugador 1 y jugador 2 para guardalos
    #Partida tiene un tablero y ese tablero tiene 2 jugadores, de ahi los referenciamos
    j1 = partida.getTablero().getJugador1()
    j2 = partida.getTablero().getJugador2()

    print("-----comprobamos que guarde los nombres correctamente-----")
    print(j1.toString())
    print(j2.toString())


    print("----Hacer una prueba de ver q los datos se modifiquen----")
    partida.getTablero().getJugador1().setNombre("Ya no es Alan , Ahora es Pedro")
    #tambien podria ser directamente
    #j1.setNombre("e")
    print(j1.toString())

    print("------Prueba aniadendo cartas a la mano del jugador-------- \n \n")

    j1.tomar5Cartas()
    j1.imprimirMano()

    print("------Verificando q las cartas q se aniaderon a la mano se eliminar del deck------- \n")
    print(j1.toString())

    print("___________pruebas con el tablero__________")
    tablero = partida.getTablero().toString() #aquí directamente se llama al método toString de la clase Tablero
    print(tablero)

#llamado de la funcion maine
main()

