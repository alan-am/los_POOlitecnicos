class Partida:

    #Constructor
    def __init__(self, id, jugador1, jugador2):
        self.__id = id;
        self.__jugador1 = jugador1;
        self.__jugador2 = jugador2;
        turno = 1;
    
    #Getters y setters
    def getId(self):
        return self.__id
    def setId(self, nuevo_id):
        self.__id = nuevo_id

    def getJugador1(self):
        return self.__jugador1
    def setJugador1(self, nuevo_jugador1):
        self.__jugador1 = nuevo_jugador1

    def getJugador2(self):
        return self.__jugador2
    def setJugador2(self, nuevo_jugador2):
        self.__jugador2 = nuevo_jugador2

    def getTurno(self):
        return self.__turno
    def setTurno(self, nuevo_turno):
            self.__turno = nuevo_turno

    #Metodos
    def sorteoInicio(j1, j2):
        '''Realiza el sorteo de quien empieza la partida'''
        pass;
    
    def resetearEstadoCartas(jugador):
        '''Despues de cada turno , resetea el estado "puedeAtacar"
        de las cartasMonstruo en el tablero de un jugador'''
        pass;

    