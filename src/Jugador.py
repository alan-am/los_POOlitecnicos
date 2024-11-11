class Jugador:

    def __init__(self, id, puntosVida, Deck, tablero):
        self.__id = id;
        self.__puntosVida = puntosVida;
        self.__deck = Deck;
        cartasEnMano = [];
        self.__tablero = tablero;
    
    def tomar5Cartas():
        '''Metodo que toma las 5 cartas de la deck al inicio del juego'''
        pass;
    def robarCartaEnTurno():
        '''Metodo para que hace q el jugador tome una carta,
        se asocia con el metodo robarCarta() de Deck'''
        pass;
    def jugarCarta():
        '''Metodo para jugar una carta en el tablero,
        se asocia con el metodo aniadirCarta() de Tablero'''
        pass;
    def declararBatalla():
        '''Metodo para iniciar batalla entre cartas,
        se asocia con atacar() de CartaMonstruo'''
        pass;