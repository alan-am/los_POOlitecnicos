from Jugador import Jugador
from Deck import Deck
from Cartas import *

class Tablero:

    #Constructor
    def __init__(self):
        self.__id = 1;
        self.__jugador1 = self.aniadirJugador(); #se deberia poner en una lista los 2 jugadores?
        self.__jugador2 = self.aniadirJugador(); #para poder controlar mejor los turnos?
        self.tablerocompartido = {self.__jugador1.getId():{"CartasMonstruo":[],"CartasEspeciales":[]},
                                    self.__jugador2.getId():{"CartasMonstruo":[],"CartasEspeciales":[]}} 
        
        #self.__cartasMonstruo = [];
        #self.__cartasEspeciales = [];
        

    #Metodos
    def aniadirJugador(self):
        '''Aniade un jugador al tablero'''
        print(f'Ingrese el nombre del jugador {Jugador.jugadores + 1}');
        nombre = input('> ');
        #Creacion del deck
        deck = Deck();

        #Creacion y retorno del jugador
        return Jugador(nombre, deck);

    def aniadirCartaTablero(self,Carta,id_jugador): #debería recibir como parámetro la carta a añadir? y el self corresponde al tablero
        '''metodo para aniadir cartas al tablero, se especifica de qué jugador es la carta'''
        #al añadir o quitar cartas en el main es necesario poner el id del jugador como parámetro

        if isinstance(Carta,CartaMonstruo) and len(self.tablerocompartido[id_jugador]["CartasMonstruo"])<3: #compara el tipo de carta y la cantidad
            self.tablerocompartido[id_jugador]["CartasMonstruo"].append(Carta)
            self.quitarCarta_Mano(id_jugador,Carta)
            
        elif (isinstance(Carta,CartaMagica) or isinstance(Carta,CartaTrampa)) and len(self.tablerocompartido[id_jugador]["CartasEspeciales"])<3:
            self.tablerocompartido[id_jugador]["CartasEspeciales"].append(Carta)
            self.quitarCarta_Mano(id_jugador,Carta)
        else:
            print(f"No se pudo incluir esa carta, espacio lleno") ## para avisarle al jugador que alcanzó el límite¿?no estoy segura de esto


    def quitarCartaTablero(self,Carta,id_jugador): #parametro carta añadido, id_jugador
        '''metodo para quitar cartas del tablero, 
        eliminar de las listas'''
        if isinstance(Carta,CartaMonstruo): #isintance es como instanceof de java
            self.__tablerocompartido[id_jugador]["CartasMonstruo"].remove(Carta)
        else:
            self.__tablerocompartido[id_jugador]["CartasEspeciales"].remove(Carta)
    
    def quitarCarta_Mano(self,id_jugador,Carta):
            '''funcion que me ayuda a quitar la carta de la mano del jugador una vez que se coloca en el tablero'''
            if id_jugador==1:
                self.__jugador1.getCartasEnMano().remove(Carta)
            elif id_jugador ==2:
                self.__jugador2.getCartasEnMano().remove(Carta)
    

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



    
    def toString(self):
        cartas_j1 = self.tablerocompartido[1]
        cartas_j2= self.tablerocompartido[2]
        car_monstruos_j1 = []
        car_especiales_j1=[]
        car_monstruos_j2=[]
        car_especiales_j2=[]
        def llenarlistas(listavacia1,listavacia2,diccionario): #listavacia1 sera de monstruos y lista2 de especiales
            for carta in diccionario["CartasMonstruo"]:
                nombreCarta = carta.getNombre();
                listavacia1.append(nombreCarta);
            for carta in diccionario["CartasEspeciales"]:
                nombre = carta.getNombre();
                listavacia2.append(nombre)
        llenarlistas(car_monstruos_j1,car_especiales_j1,cartas_j1)
        llenarlistas(car_monstruos_j2,car_especiales_j2,cartas_j2)
        return f'''{"TABLERO".center(55,"-")}
{"Jugador 1".center(70,"=")}
Monstruo: {car_monstruos_j1}
Especiales: {car_especiales_j1}
{"Jugador 2".center(70,"=")}
Monstruo: {car_monstruos_j2}
Especiales: {car_especiales_j2}

'''



