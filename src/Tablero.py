from Jugador import Jugador
from Deck import Deck


class Tablero:

    #Constructor
    def __init__(self):
        self.__id = 1;
        self.__jugador1 = self.aniadirJugador(); #se deberia poner en una lista los 2 jugadores?
        self.__jugador2 = self.aniadirJugador(); #para poder controlar mejor los turnos?
        self.__cartasMonstruo = [];
        self.__cartasEspeciales = [];

    #Metodos
    def aniadirJugador(self):
        '''Aniade un jugador al tablero'''
        print(f'Ingrese el nombre del jugador {Jugador.jugadores + 1}');
        nombre = input('> ');
        #Creacion del deck
        deck = Deck();

        #Creacion y retorno del jugador
        return Jugador(nombre, deck);

    def aniadirCarta(c):
        '''metodo para aniadir cartas al tablero, a las listas'''
        pass;

    def quitarCarta():
        '''metodo para quitar cartas del tablero, 
        eliminar de las listas'''
        pass;

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
    
    def getPartida(self):
        return self.__partida;
    def setPartida(self, nueva_partida):
        self.__partida = nueva_partida;

    def getCartasMonstruo(self):
        return self.__cartasMonstruo
    def setCartasMonstruo(self, nuevas_cartas):
        self.__cartasMonstruo = nuevas_cartas

    def getCartasEspeciales(self):
        return self.__cartasEspeciales
    def setCartasEspeciales(self, nuevas_cartas):
        self.__cartasEspeciales = nuevas_cartas




