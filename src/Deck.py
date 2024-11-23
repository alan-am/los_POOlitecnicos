import random
from Cartas import *
from TiposEnum import *
class Deck:
    #atributo estatico para contabilizar
    decks = 0

    #Constructor
    def __init__(self):
        Deck.decks += 1;
        self.__id = Deck.decks
        self.__baraja = self.cargarCartas();
    
    #Metodos

    ###
    def cargarCartas(self):
        '''Crea cartas de Monstruos, Trampas y Magicas apartir de varios archivos;
          y las aniade a una lista de cartas, luego la retorna'''

        #!Procesamiento de cartas monstruo
        baraja = [];
        cartas_monstruo = [];
        with open("src/archivoCartasMonstruo.txt", "r") as archivo:
            archivo.readline();
            for linea in archivo:
                lst_datos = linea.split(', ')
                nombre = lst_datos[0];
                tipoMonstruo = lst_datos[1];
                atributo = lst_datos[2];
                atk = int(lst_datos[3]);
                defensa = int(lst_datos[4]);
                descripcion = lst_datos[5]
                cartas_monstruo.append(CartaMonstruo(nombre, descripcion, atk, defensa,TipoMonstruo[tipoMonstruo], TipoAtributo[atributo]))
        
        #barajeamos las cartas monstruo
        self.barajear(cartas_monstruo); #no devuelve, desordena directamente

        #agregamos 20 cartas monstruo a la baraja final
        i = 0 
        for i in range(20):
            baraja.append(cartas_monstruo[i]);
            i += 1;
        
        #!Procesamiento de cartas Magicas
        cartas_magicas = [];
        with open("src/archivoCartasMagicas.txt", "r") as archivo:
            archivo.readline();
            for linea in archivo:
                lst_datos = linea.split(", ");
                nombre = lst_datos[0];
                descripcion = lst_datos[1];
                incrementoAtaque = int(lst_datos[2]);
                incrementoDefensa = int(lst_datos[3]);
                tipoMonstruo = lst_datos[4].strip();
                cartas_magicas.append(CartaMagica(nombre, descripcion, incrementoAtaque,incrementoDefensa, TipoMonstruo[tipoMonstruo]));
        #barajeamos las cartas:
        self.barajear(cartas_magicas)

        #agregamos 5 cartas magicas a la baraja final
        i = 0;
        for i in range(5):
            baraja.append(cartas_magicas[i]);
            i += 1;
        
        #!Procesamiento de las cartas Trampas
        cartas_trampas = []
        with open("src/archivoCartasTrampa.txt","r") as archivo:
            archivo.readline();
            for linea in archivo:
                lst_datos = linea.split(", ");
                nombre = lst_datos[0];
                descripcion = lst_datos[1];
                atributo = lst_datos[2].strip();
                cartas_trampas.append(CartaTrampa(nombre, descripcion, TipoAtributo[atributo]))
        #barajeamos las cartas trampas
        self.barajear(cartas_trampas);
        #guardamos 5 cartas trampa en la baraja final
        i = 0;
        for i in range(5):
            baraja.append(cartas_trampas[i]);
            i += 1;

        #se barajea la baraja final y se retorna
        self.barajear(baraja);
        return baraja
    
    def barajear(self, listaCartas):
        '''desordena una lista de cartas'''
        random.shuffle(listaCartas)

    def robarCarta(self):
        '''devuelve una carta para el jugador traida de la baraja y la borra
        de la baraja'''
        return self.__baraja.pop(0) #elimina y devuelve la carta

    #Getters y setters 
    def getBaraja(self):
        return self.__baraja;
    def setBaraja(self, nuevaBaraja):
        self.__baraja = nuevaBaraja;

    def getJugador(self):
        return self.__jugador;
    def setJugador(self, nuevo_jugador):
        self.__jugador = nuevo_jugador;

    def getId(self):
        return self.__id;

    #toString
    def toString(self):
        lst_aMostrar = [];
        for Carta in self.__baraja:
            nombreCarta = Carta.getNombre();
            lst_aMostrar.append(nombreCarta);
        return lst_aMostrar


