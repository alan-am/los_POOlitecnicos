import Partida
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
        eleccion = input("1. Si \n2. No \n");
        while eleccion != "1"  and eleccion != "2":
            print("Elige un numero entre 1 y 2")
            eleccion = input("> ");

        if eleccion == "1" and tablero.hayCartasMonstruoBocaArriba(self.__id):
            #Mostramos las cartas mosntruo en el tablero:
            print("Selecciona la carta monstruo a cambiar: ");
            i = 0;
            for carta in espacioCartasMonstruo:
                print(f'{i+1}. {carta.getNombre()}')
                i += 1;
            
            seleccion = input("Selecciona la carta a añadir: \n > ")
            # validacion por si el usuario pone letras  o se pasa del rango-_-
            while (not seleccion.isdigit()) or (int(seleccion)> i  or int(seleccion) <= 0):
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
        print("Deseas atacar?")
        eleccion = input("1. Si \n2. No \n");
        #validamos su seleccion
        while eleccion != "1"  and eleccion != "2":
                print("Elige un numero entre 1 y 2")
                eleccion = input("> ");
        #Validacion existan cartas monstruo
        while tablero.hayCartasMonstruoEnAtaque(self) and eleccion == "1": #Verifica que haya cartas en modo ataque e implicitamente q existan cartas en el espacio
            #si enetró en el while es porque quiere atacar
            print("Elige tu carta de ataque: ")
            i = 0;
            #mostramos las cartas a elegir del jugador propio, y solo las que estan en posicion de ataque y estan
            #boca arriba damos permiso de atacar;
            for cartaMonstruo in espacioCartasMonstruoJ:
                print(f'{i+1}. {cartaMonstruo.getNombre()}') #A lomejor tambien mostrar ATK y DEF 
                i += 1;
            seleccion = input("> ")
            # validacion por si el usuario pone letras  o se pasa del rango-_-
            while (not seleccion.isdigit()) or (int(seleccion)> i  or int(seleccion) <= 0):
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
                        cartaSeleccionada.setPuedeAtacar(False);


                        
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
                        cartaSeleccionada.setPuedeAtacar(False);


                else:
                    # damos a elegir que carta quiere atacar
                    print("Elige la carta Enemiga a atacar: ")
                    i = 0;
                    for cartaMonstruo in espacioEnemigo:
                        #mostramos los datos de la carta solo si esta boca arriba
                        if cartaMonstruo.getIsBocaArriba():
                            print(f'{i+1}. {cartaMonstruo.getNombre()}') #? aniadir ATK y DEF?
                        else: 
                            print(f'{i+1}. Carta sin desvelar')
                        i+=1
                    seleccion = input("> ")
                    # validacion por si el usuario pone letras  o se pasa del rango-_-
                    while (not seleccion.isdigit()) or (int(seleccion)> i  or int(seleccion) <= 0):
                        print("Por favor, ingresa un número válido.")
                        seleccion = input("> ")
                    
                    cartaEnemigaSeleccionada = espacioEnemigo[int(seleccion)-1]

                    #Ejecutamos el ataque:

                    danioAEnemigo , danioAJugador = tablero.ataqueEntreCartas(cartaSeleccionada, cartaEnemigaSeleccionada, self, enemigo)

                    #Actualizamos la vida de los jugadores
                    #!comprobar si se puede acceder directamente
                    self.__puntosVida = self.__puntosVida - danioAJugador;
                    enemigo.__puntosVida =  enemigo.__puntosVida - danioAEnemigo;
                    cartaSeleccionada.setPuedeAtacar(False);

            else:
                print("La carta seleccionada no esta en modo Ataque o ya ha atacado en este turno.")
            #cambiamos el estado de la carta  seleccionada para que ya no se pueda utilizar en el turno. OJO
            #Especificaciones funcion:
            # verificar si no es el primer turno -> se lo valida en otra funcion de partida o del main CHEC (en "ronda")
            #Da a elegir al jugador con q carta Monstruo de su tablero quiere atacar y a cual de la otras quiere atacar CHECK
            # se ataca directamente implicitamente CHECK
            # primero verifica si tiene cartas mosntruo en el tablero, sino ataca directamente CHECK
            # actualiz la vida del jugador CHECK
            # se cambia el atributo  de la carta elegida puedeAtacar a False CHECK
            '''vuelve a preguntar y eleccion se actualiza'''
            print("Deseas atacar?")
            eleccion = input("1. Si \n2. No \n");
            #validamos su seleccion
            while eleccion != "1"  and eleccion != "2":
                print("Elige un numero entre 1 y 2")
                eleccion = input("> ");
    def jugarCarta(self, partida: Partida):
        '''Funcion que muestra las cartas en mano del jugador y le da a elegir
            que carta aniadir al tablero, luego de este haberlo seleccionado se la debe validar
            para confirmar que es una carta q se puede poner en tablero
            '''
        #PASOS
        #1 preguntar si desea jugar alguna carta de su mano, en caso de que si, llamar a esta funcion
        #1.5 complementar con un while para q el jugador pueda aniadir cuantas veces quiera
        #2 se complementa con la llamada de la funcion cambiarPosicionDeAtaque, luego de ejecutarse jugarCarta()
        #(lo de arriba iria en la funcion de fases de partida o directamente en el main)
        #3 mostrar las cartas en mano del jugador

        #guardamos la referencia de tablero a traves de partida
        tablero: Tablero = partida.getTablero();

        i = 0
    

        print("Cartas en mano".center(40, "-"))
        for carta in self.getCartasEnMano():
            #debo hacer un toString2 de cartas menos descriptivo
            print(f'{i+1}. {carta.toString2()} ')
            i += 1            
        seleccion = input("Selecciona la carta a añadir: \n > ")
    # validacion por si el usuario pone letras  o se pasa del rango-_-
        while  (not seleccion.isdigit()) or (int(seleccion)> i  or int(seleccion) <= 0):
            print("Por favor, ingresa un número válido.")
            seleccion = input("> ")
        cartaSeleccionada = self.getCartasEnMano()[int(seleccion)-1]
    #antes de aniadirla verificamos q tipo de carta es, validamos que 
    # tenga suficiente espacio para ese tipo y preguntamos(en el caso de cartas mosntruo q tipo de posicion)
    #Si es un carta monstruo
        if(isinstance(cartaSeleccionada, CartaMonstruo)):
            #validamos q haya espacio
            if len(tablero.tablerocompartido[self.__id]["CartasMonstruo"])<3:
                #preguntamos en que modo pone la carta
                print("Elige el modo de la carta: ")
                eleccion = input("1. Ataque \n2. Defensa \n");
                while eleccion != "1"  and eleccion != "2":
                    print("Elige un numero entre 1 y 2")
                    eleccion = input("> ");
                if eleccion == "1": 
                    #Si esta en ataque la carta debe quedar boca arriba
                    cartaSeleccionada.setIsInAtaque(True)
                    cartaSeleccionada.setIsBocaArriba(True)
                elif eleccion == "2": 
                    #Si esta en defensa la carta debe quedar boca abajo
                    cartaSeleccionada.setIsInAtaque(False)
                    cartaSeleccionada.setIsBocaArriba(False)
                
                #Aniadimos la carta a tablero
                tablero.aniadirCartaTablero(cartaSeleccionada, self.__id)
            else:
                print("Ya no puedes colocar mas cartas Monstruo")
        #Caso si la cartas es Magica o trampa
        elif isinstance(cartaSeleccionada, CartaMagica) or isinstance(cartaSeleccionada, CartaTrampa):
            #validamos que haya espacio
            if len(tablero.tablerocompartido[self.__id]["CartasEspeciales"])<3:
                #Aniadimos la carta a tablero
                tablero.aniadirCartaTablero(cartaSeleccionada, self.__id)
            else:
                print("No se puede agregar mas cartas Magicas o Trampa") 
       

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


    #Metodos de la maquina

    def declararBatallaComoMaquina(self, tablero: Tablero, oponente):
    
        print(f"{self.getNombre()} te va a declarar batalla. ¡Prepárate!")

        # Obtener monstruos en ataque que pueden atacar
        monstruosAtacantes = []
        for carta in tablero.getTableroCompartido()[self.getId()]["CartasMonstruo"]:
            if carta.getIsInAtaque() and carta.getPuedeAtacar():
                monstruosAtacantes.append(carta)

        # Si no hay monstruos en ataque, cambiar a modo defensa
        if len(monstruosAtacantes) == 0:
            print(f"{self.getNombre()} no tiene monstruos disponibles para atacar. Se coloca a la defensiva.")
            for carta in tablero.tablerocompartido[self.getId()]["CartasMonstruo"]:
                if carta.getIsInAtaque():
                    carta.setIsInAtaque(False)
                    carta.setIsBocaArriba(False)
                    print(f"{self.getNombre()} pone al monstruo {carta.getNombre()} en defensa.")
            return

        # Obtener monstruos del oponente
        monstruosOponente = tablero.tablerocompartido[oponente.getId()]["CartasMonstruo"]
        # Aca ataca con cada mounstro disponible 
        for cartaAtacante in monstruosAtacantes:
            if len(monstruosOponente) > 0:
                cartaDefensora = monstruosOponente[0]
                print(f"{cartaAtacante.getNombre()} ataca a {cartaDefensora.getNombre()}!")
                tablero.ataqueEntreCartas(cartaAtacante, cartaDefensora, self, oponente)
            else:
                print(f"{cartaAtacante.getNombre()} realiza un ataque directo")
                oponente.setPuntosVida(oponente.getPuntosVida() - cartaAtacante.getAtaque())
            cartaAtacante.setPuedeAtacar(False)

            print(f"{self.getNombre()} ha terminado su fase de batalla.")


    def llenarTableroMaquina(self, tablero: Tablero):
        print(f"{self.getNombre()} está organizando su tablero.")
        #print(self.imprimirMano()) solo fue para encontrar el error
        mano_maquina = self.getCartasEnMano().copy()

        # Colocar cartas de monstruo
        for carta in mano_maquina:
            if isinstance(carta, CartaMonstruo):
                if len(tablero.tablerocompartido[2]["CartasMonstruo"]) < 3:
                    tablero.aniadirCartaTablero(carta, 2) #quita automat la carta de la mano
                    print(f"{self.getNombre()} coloca al monstruo {carta.getNombre()} en el tablero.")

        # Colocar cartas mágicas o trampas
            else: #si no es monstruo será cualquier otra
                if len(tablero.tablerocompartido[2]["CartasEspeciales"]) < 3:
                    tablero.aniadirCartaTablero(carta, 2)
                    print(f"{self.getNombre()} coloca una carta especial: {carta.getNombre()}.")

        print(f"{self.getNombre()} ha terminado de organizar su tablero.")

        ### FIN DE LAS FUNCIONES DE MAQUINA
    
        
    def esDerrotado(self,id_jugador):
        ##verifica que el jugador fue derrotado
        NoTieneCartas= len(self.getCartasMano(id_jugador))==0 and len(self.getBaraja(id_jugador))==0
        if  self.getPuntosVida(id_jugador)<=0 or NoTieneCartas:
            return True #devuelve true si esderrotado
    
         
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

