from Tablero import Tablero
from Cartas import CartaMonstruo
import random
from Jugador import *

class Partida:

    #Constructor
    def __init__(self,jugador1,jugador2):
        self.__id = 1;
        self.__turno = 1;
        self.__tablero = Tablero();
        self.__jugadores = [jugador1,jugador2]

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

    def getJugadorActual(self):
        return self.__jugadores[self.__turno]
   
    #Metodos
    def faseTomarCarta(self):
        """Es la fase en la cual un jugador roba una carta de su deck"""
        jugadorActual = self.getJugadorActual()
        if jugadorActual == self.__jugadores[0]: 
            print(f"{jugadorActual.getNombre()} está robando una carta")
            jugadorActual.tomarCartaEnTurno()
        else:
            print(f"{jugadorActual.getNombre()} está robando 5 cartas...")
            jugadorActual.tomar5Cartas()


    def fasePrincipal(self):
        pass;
    
    def faseBatalla(self):
        pass;
    



    def sorteoInicios(self,j1, j2):
        print("¡Bienvenido al juego de YuGiOH!")
        JugadoresIniciales = [j1,j2]
        JugadorEmpieza = random.choice(JugadoresIniciales)
        self.__turno = JugadorEmpieza.getId() #con esto ya modifiqué el turno por primera vez
        print(f"El jugador que empieza es: {JugadorEmpieza.getNombre()} -Id: {JugadorEmpieza.getId()}")
        
    def cambiarTurno(self):
        ###Cambia el turno al siguiente jugador."""
        if self.__turno == 1:
            self.__turno+=1
        else: #como solo hay dos jugadores solo hay dos posibilidades
            self.__turno-=1

        #intenté acomodar este método


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


    


        