
class Jugador:

    #Atributo estatico
    jugadores = 0

    #Constructor
    def __init__(self,nombre, deck):

        Jugador.jugadores += 1;
        self.__id = Jugador.jugadores;
        self.__puntosVida = 4000;
        self.__nombre = nombre;
        self.__deck = deck; #es una lista de cartas
        self.__cartasEnMano = [];
    
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
    
    def getNombre(self):
        return self.__nombre;
    def setNombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre;
    

    #Metodos
    
    def tomar5Cartas(self):
        ###Metodo donde  el jugador tome una carta del Deck suyo,se asocia con el metodo robarCarta() de Deck'''
        i = 0;
        for i in range(5):
            self.tomarCartaEnTurno();
            i += 1;

    def tomarCartaEnTurno(self):
        ###Metodo donde  el jugador tome una carta del Deck suyo, se asocia con el metodo robarCarta() de Deck'''
        cartaTomada = self.__deck.robarCarta();
        self.__cartasEnMano.append(cartaTomada);
        
    def jugarCarta():
        '''Metodo para jugar una carta en el tablero,
        se asocia con el metodo aniadirCarta() de Tablero y luego de validar
        quita la carta de la mano del jugador'''
        pass;
    
    def declararBatalla():
        '''Metodo para iniciar batalla entre cartas,
        se asocia con atacar() de CartaMonstruo'''
        pass;
    
    def imprimirMano(self):
        ###Imprime por consola las cartas en mano que tiene el jugador'''
        for Carta in self.__cartasEnMano:
            print(Carta.toString())

    def listarCartasEnMano(self):
        ###Metodo hecho por Alan, escribe su funcionalidad xd
        cartas = []
        for Carta in self.__cartasEnMano:
                     cartas.append(Carta.getNombre())
        return cartas


    def jugarComoMaquina():
        '''Metodo para la instancia Maquina'''
        pass;
    
    
         
    #String of
    def stringOf(self):
        return f''' Datos Jugador {self.__nombre} \n
        Id: {self.__id} \n
        Puntos de vida: {self.__puntosVida} \n
        --------------------------------- \n
        Baraja: {self.__deck} \n
        ---------------------------------- \n
        Cartas en mano: {self.__cartasEnMano} \n
        -----------------------------------
        '''

