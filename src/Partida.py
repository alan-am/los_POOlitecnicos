from Tablero import Tablero
import random
class Partida:
    
    #Atributo estatico
    turno = 1;
    #Constructor
    def __init__(self):
        self.__id = 1;
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
    def sorteoInicio(j1, j2):
        JugadoresIniciales = [j1,j2]
        JugadorEmpieza = random.choice(JugadoresIniciales)
        return JugadorEmpieza
        
    
    def resetearEstadoCartas(jugador):
        '''Despues de cada turno , resetea el estado "puedeAtacar"
        de las cartasMonstruo en el tablero de un jugador'''
        pass;