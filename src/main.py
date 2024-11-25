from Deck import Deck
from Jugador import Jugador
from Partida import Partida
from Tablero import Tablero
from Cartas import *


def main():
    '''
    TEST 1 -- probando la base 

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

    print("___________pruebas con el tablero______________________________________________________")
    tablero = partida.getTablero()
    tablero.aniadirCartaTablero(j1.getCartasEnMano()[0],1) #aquí directamente se llama al método toString de la clase Tablero

    print(tablero.toString())
    print(j1.toString())
'''

    #cuerpo de la partida


    partida = Partida()
    #Nuevo Cambio, modifique partida para que se crear con un jugador "maquina' automaticamente
    #asi ya no hay q estarle dando nombre, la maquina sera el jugador 2
    print("---+ Jugador 2 corresponde a la máquina")
    usuario = partida.getTablero().getJugador1()
    maquina = partida.getTablero().getJugador2() #j2 es la maquina
    # maquina.setNombre("Maquina") #para que se entienda mejor quien juega

    input("Mostrando la informacion de ambos jugadores" ) 
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
    print("Presiona enter para continuar")
    input("Loading...")
    print("")



    #Inicio con sorteo de quien empieza
    partida.sorteoInicios(usuario,maquina)


    #Ciclo de turnos
    while not usuario.esDerrotado() and not maquina.esDerrotado():
        partida.ronda()
         #verifiquen en cada función qué desean que imprima para que el usuario lo pueda ver
    
    
    #Final del juego
    #luego de que uno es derrotado:
    partida.finalizarPartida(usuario,maquina)
    




    #ayuda como lo ejecuto

#llamado de la funcion maine
main()

