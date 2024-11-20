import random
class Deck:
    
    def __init__(self,rutaArchivo, jugador):
        listaCartas = self.cargarCartas(rutaArchivo);
        self.__baraja = self.asignarCartas(self.barajear(listaCartas));
        self.__jugador = jugador;
    
    def cargarCartas(self,rutaArchivo):
        '''Crea cartas y las aniade a una lista de cartas sacadas a partir de un
        archivo, luego la retorna'''
        cartasNuevas = []
        with open(rutaArchivo, "r") as archivo:
            for linea in archivo:
                linea = linea.rstrip()
                cartasNuevas.append(linea)
        return cartasNuevas
        pass;
    
    def barajear(self, listaCartas):
        '''desordena una lista de cartas'''
        random.shuffle(listaCartas)
        return listaCartas
        pass;

    def asignarCartas(self, listaCartas):
        '''De una lista de cartas, retorna una nueva lista con 
        20 cartas monstruo, 5 magicas y 5 trampas'''

        pass;

    def robarCarta(self):
        '''devuelve un carta para el jugador traida de la baraja y la borra
        de la baraja'''
        pass;

    #Getters y setters 
    def getBaraja(self):
        return self.__baraja;
    def setBaraja(self, nuevaBaraja):
        self.__baraja = nuevaBaraja;

    def getJugador(self):
        return self.__jugador;
    def setJugador(self, nuevo_jugador):
        self.__jugador = nuevo_jugador;