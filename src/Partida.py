class Partida:

    #Constructor
    def __init__(self, id,tablero):
        self.__id = id;
        self.__turno = 1;
        self.__tablero = tablero;
        self.__idTablero = tablero.getId();

    #Metodos
    def sorteoInicio(j1, j2):
        '''Realiza el sorteo de quien empieza la partida'''
        pass;
    
    def resetearEstadoCartas(jugador):
        '''Despues de cada turno , resetea el estado "puedeAtacar"
        de las cartasMonstruo en el tablero de un jugador'''
        pass;

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
    