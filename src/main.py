from Deck import Deck
from Jugador import Jugador
from Partida import Partida
from Tablero import Tablero
from Cartas import *


def main():

    #cuerpo de la partida
    partida = Partida()

    print("---+ Jugador 2 corresponde a la máquina")
    usuario = partida.getTablero().getJugador1()
    maquina = partida.getTablero().getJugador2() #j2 es la maquina
    
    #TEST
    print("Mostrando la informacion de ambos jugadores" ) 
    #Luego cuando ya este todo testeado eliminar esto de mostrar nombre, pq se supone
    #que el jugador no deberia ver su baraja xd, solo sus cartas en mano
    print("")
    print(usuario.toString())
    print(maquina.toString())
    print("")
    # cambio_nom = input("¿Deseas cambiar el nombre de tu jugador?(si/no) ").lower()
    # while cambio_nom not in ["si","no"]:
    #     cambio_nom = input("¿Deseas cambiar el nombre de tu jugador?(si/no) ").lower()
    # if cambio_nom == "si":
    #     nombre= input("Ingrese el nuevo nombre: ")
    #     usuario.setNombre(nombre)
    #     print("---> Nombre de jugador cambiado con éxito")
    #     print(f"> {usuario.getNombre()}")
    #     print("")



 
    #iNICIO DEL JUEGO
    print("\n \n \nEmpieza el juego!")
    print("Presiona enter para continuar")
    input("Loading...")
    print("")



    #Inicio con sorteo de quien empieza
    partida.sorteoInicios(usuario,maquina)


    #Ciclo de turnos
    while not usuario.esDerrotado() and not maquina.esDerrotado():
        partida.ronda()
    
    
    #Final del juego
    #luego de que uno es derrotado:
    partida.finalizarPartida(usuario,maquina)
    

#llamado de la funcion main
main()

