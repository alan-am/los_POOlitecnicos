class Jugador:

    def __init__(self, id, puntosVida, deck):
        self.__id = id;
        self.__puntosVida = puntosVida;
        self.__deck = deck;
        self.__cartasEnMano = [];
    
    #Metodos
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
    
    def jugarComoMaquina():
        '''Metodo para la instancia Maquina'''
        pass;
    
    #Getters y setters 
    def getId(self):
        return self.__id
    def setId(self, nuevo_id):
        self.__id = nuevo_id
 
    def getPuntosVida(self):
        return self.__puntosVida
    def setPuntosVida(self, nuevos_puntosVida):
        self.__puntosVida = nuevos_puntosVida

    def getDeck(self):
        return self.__deck
    def setDeck(self, nuevo_deck):
        self.__deck = nuevo_deck
  
    def getCartasEnMano(self):
        return self.__cartasEnMano
    def setCartasEnMano(self, nuevas_cartas):
        self.__cartasEnMano = nuevas_cartas

