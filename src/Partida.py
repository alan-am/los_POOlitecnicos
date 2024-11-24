from Tablero import Tablero
from Cartas import CartaMonstruo
import random
from Jugador import *

class Partida:

    #Constructor
    def __init__(self):
        self.__id = 1;
        self.__turno = 1;
        self.__tablero = Tablero();

   #Getters y setters
    def getId(self):
        return self.__id
    def setId(self, nuevo_id):
        self.__id = nuevo_id

    def getTablero(self):
        return self.__tablero;
    def setTablero(self, nuevo_tablero):
        self.__tablero = nuevo_tablero;

    def getTurno(self):
        return self.__turno
    def setTurno(self, nuevo_turno):
        self.__turno = nuevo_turno

   
    #Metodos
    def sorteoInicios(self,j1, j2):
        print("La partida esta por comenzar")
        JugadoresIniciales = [j1,j2]
        JugadorEmpieza = random.choice(JugadoresIniciales)
        print(f"El jugador que empieza es: {JugadorEmpieza}")
        
    def cambiarTurno(self, jugadores):
        ###Cambia el turno al siguiente jugador."""
        self.__turno = (self.__turno % len(jugadores)) + 1
        print(f"Es el turno del Jugador {self.__turno}.") ##AUN NO ESTA COMPLETO CREO


    def resetearEstadoCartasMounstro(self, jugador):
        """Después de cada turno, resetear el estado de las cartas monstruo"""
        for carta in jugador.getCartasEnMano():
            if isinstance(carta, CartaMonstruo):
                carta.setPuedeAtacar(True)
                carta.setIsInAtaque(True)
    
    
    def finalizarPartida(self, j1, j2):
        """Finaliza la partida determinando el ganador."""
        if j1.esDerrotado():
            print(f"El jugador{j1.getNombre()} ha sido derrotado.")
            print(f"El ganador es {j2.getNombre()}!")
        elif j2.esDerrotado():
            print(f"El jugador {j2.getNombre()} ha sido derrotado.")
            print(f"El ganador es {j1.getNombre()}!")
        else:
            print("La partida se acabo, terminaron en empate !!")


    


        