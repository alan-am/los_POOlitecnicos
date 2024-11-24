import Partida;
from Tablero import Tablero;
from Cartas import *;

class Jugador:

    #Atributo estatico
    jugadores = 0

    #Constructor
    def __init__(self,nombre, deck):

        Jugador.jugadores += 1;
        self.__id = Jugador.jugadores;
        self.__puntosVida = 4000;
        self.__nombre = nombre;
        self.__deck = deck; #es una lista de Cartas
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
        

    
    #En jugarCarta una vez finalizado todo el proceso se debe hacer un print de como queda el tablero?
    def cambiarPosicionAtaque(self, partida):
        '''Da la opcion a un jugador de cambiar la posicion de ataque de una carta, solo 1 vez(por ahora)'''
        tablero = partida.getTablero();
        espacioCartasMonstruo = tablero.tablerocompartido[self.__id]["CartasMonstruo"]

        print("Deseas cambiar la posicion de una carta?")
        eleccion = input("1. Si \n 2. No \n");
        while eleccion != "1"  and eleccion != "2":
            print("Elige un numero entre 1 y 2")
            eleccion = input("1. Si \n 2. No \n");

        if eleccion == "1" and tablero.hayCartasMonstruoBocaArriba(self.__id):
            #Mostramos las cartas mosntruo en el tablero:
            print("Selecciona la carta monstruo a cambiar: ");
            i = 1;
            for carta in espacioCartasMonstruo:
                print(f'{i}. {carta.getNombre()}')
                i += 1;
            
            seleccion = input("> ")
            # validacion por si el usuario pone letras  o se pasa del rango-_-
            while not (seleccion.isdigit()) or int(seleccion) > i or int(seleccion) <= 0:
                print("Por favor, ingresa un número válido.")
                seleccion = input("> ")
            
            cartaSeleccionada = espacioCartasMonstruo[int(seleccion) - 1];
            cartaSeleccionada.setIsInAtaque(not(cartaSeleccionada.getIsInAtaque()));
            
        else:
            print("No exiten cartas Monstruo boca Arriba para cambiar su posicion")
            
            
    
    def declararBatalla(self, enemigo, partida): 
        '''Metodo para iniciar batalla entre cartas,
        se asocia con ataqueEntreCartas() de Tablero'''
                #TypeHint para evitar confusiones
        tablero : Tablero = partida.getTablero();
        espacioCartasMonstruoJ = tablero.tablerocompartido[self.__id]["CartasMonstruo"]

        #Validacion existan cartas monstruo
        while tablero.hayCartasMonstruoEnAtaque(self.__id): #Verifica que haya cartas en modo ataque e implicitamente q existan cartas en el espacio
            #preguntamos si desea atacar
            print("Deseas atacar?")
            eleccion = input("1. Si \n 2. No \n");
            #validamos su seleccion
            while eleccion != "1"  and eleccion != "2":
                print("Elige un numero entre 1 y 2")
                eleccion = input("1. Si \n 2. No \n");
            #entramos en los casos de seleccion
            if eleccion == "1":
                print("Elige tu carta de ataque: ")
                i = 1;
                #mostramos las cartas a elegir del jugador propio, y solo las que estan en posicion de ataque y estan
                #boca arriba damos permiso de atacar;
                for cartaMonstruo in espacioCartasMonstruoJ:
                    print(f'{i}. {cartaMonstruo.getNombre()}') #A lomejor tambien mostrar ATK y DEF 
                    i += 1;
                seleccion = input("> ")
                # validacion por si el usuario pone letras  o se pasa del rango-_-
                while not (seleccion.isdigit()) or seleccion > i or seleccion <= 0:
                    print("Por favor, ingresa un número válido.")
                    seleccion = input("> ")

                cartaSeleccionada = espacioCartasMonstruoJ[int(seleccion)-1]
                #validamos que la carta elegida este en posicion de ataque y pueda atacar #!si esta en ataque esta boca arriba !!
                if cartaSeleccionada.getIsInAtaque() and cartaSeleccionada.getPuedeAtacar():
                    #logica de mostrarle la seleccion de las cartas enemigas
                    espacioEnemigo = tablero.tablerocompartido[enemigo.getId()]["CartasMonstruo"]
                    # primero verificamos si el enemigo tiene o no cartas en su tablero
                    #para ver si realizamos ataque directo o no
                    if len(espacioEnemigo) == 0:
                        #atacamos directamente

                        #primero verificamos si el enemigo tiene cartas trampa que impidan el ataque
                        #caso en el que si tenga:
                        if tablero.verificarCartaTrampa(enemigo, cartaSeleccionada) is not None:
                            print("| Se ha atacado directamente! pero una carta Trampa se interpuso")
                            #eliminamos la carta trampa q se interpuso
                            cartaTrampa = tablero.verificarCartaTrampa(enemigo, cartaSeleccionada)
                            print(f"{cartaTrampa.getNombre()} detiene el ataque de un monstruo con tipo de atributo {cartaTrampa.getTipoAtributo().value}")
                            print("Carta Trampa eliminada del tablero")
                            tablero.quitarCartaTablero(cartaTrampa, enemigo.getId())

                            
                        #caso en el que no tenga
                        else: 
                            #determinamos el danio del atacante aniadido con las cartas magicas
                            incAtkJugador, incDefJugador = tablero.verificarCartasMagicas(self, cartaSeleccionada)

                            danio = cartaSeleccionada.getAtaque() + incAtkJugador;
                            print(f"| Se ha atacado directamente con {cartaSeleccionada.getNombre()}")
                            print(f" \t {cartaSeleccionada.getAtaque()}  +  {incAtkJugador} -->  {enemigo.getPuntosVida()} Puntos Vida {enemigo.getNombre()} ")
                            #Se actualiza la vida del enemigo
                            n_vidaenemigo = enemigo.getPuntosVida() - danio;
                            enemigo.setPuntosVida(n_vidaenemigo);

                    else:
                        # damos a elegir que carta quiere atacar
                        print("Elige la carta Enemiga a atacar: ")
                        i = 0;
                        for cartaMonstruo in espacioEnemigo:
                            #mostramos los datos de la carta solo si esta boca arriba
                            if cartaMonstruo.getIsBocaArriba():
                                print(f'{i}. {cartaMonstruo.getNombre()}') #? aniadir ATK y DEF?
                            else: 
                                print(f'{i}. Carta sin desvelar')
                            i+=1
                        seleccion = input("> ")
                        # validacion por si el usuario pone letras  o se pasa del rango-_-
                        while not (seleccion.isdigit()) or seleccion > i or seleccion <= 0:
                            print("Por favor, ingresa un número válido.")
                            seleccion = input("> ")
                        
                        cartaEnemigaSeleccionada = espacioEnemigo[int(seleccion)-1]

                        #Ejecutamos el ataque:

                        danioAEnemigo , danioAJugador = tablero.ataqueEntreCartas(cartaSeleccionada, cartaEnemigaSeleccionada, self, enemigo)

                        #Actualizamos la vida de los jugadores
                        #!comprobar si se puede acceder directamente
                        self.__puntosVida = self.__puntosVida - danioAJugador;
                        enemigo.__puntosVida =  enemigo.__puntosVida - danioAEnemigo;

                else:
                    print("La carta seleccionada no esta en modo Ataque o ya ha atacado en este turno.")
            #cambiamos el estado de la carta  seleccionada para que ya no se pueda utilizar en el turno. OJO
            cartaSeleccionada.setPuedeAtacar(False);
            #Especificaciones funcion:
            # verificar si no es el primer turno -> se lo valida en otra funcion de partida o del main
            #Da a elegir al jugador con q carta Monstruo de su tablero quiere atacar y a cual de la otras quiere atacar CHECK
            # se ataca directamente implicitamente CHECK
            # primero verifica si tiene cartas mosntruo en el tablero, sino ataca directamente CHECK
            # actualiz la vida del jugador CHECK
            # se cambia el atributo  de la carta elegida puedeAtacar a False CHECK
    
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


    def declararBatallaComoMaquina():
        '''Metodo para la instancia Maquina
        es la forma predeterminada en la que declarará batalla
        ayudarse de declararbatalla de jugador'''
        pass;
    def llenarTableroMaquina():
        '''llena el tablero de la maquina, puede ayudarse de algo parecido a Jugarcarta()'''
        pass
    
        
    def esDerrotado(self):
        ##verifica que el jugador fue derrotado
        return self.getPuntosVida() <=0 #devuelve true si esderrotado
    
         
    #toString
    def toString(self):
         return f'''Datos Jugador - {self.__nombre} -
Id: {self.__id}
Puntos de vida: {self.__puntosVida}
{" Baraja ".center(25, "-")}
{self.__deck.toString()}
{" Cartas en Mano ".center(26, "-")}
{self.listarCartasEnMano()}
-----------------------------------'''

