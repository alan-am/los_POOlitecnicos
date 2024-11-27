import Partida
from Tablero import Tablero;
from Cartas import *;
from Deck import *
class Jugador:

    #Atributo estatico
    jugadores = 0

    #Constructor
    def __init__(self,nombre, deck):

        Jugador.jugadores += 1;
        self.__id = Jugador.jugadores;
        self.__puntosVida = 4000;
        self.__nombre = nombre;
        self.__deck = Deck(); #es una lista de Cartas
        self.__cartasEnMano = [];
        self.__noagregoMonstruo = True; #por defecto, cambia en cada turno porque solo puede agregar un monstruo por vez
    
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
    def setNoAgregoMonstruo(self,boolean):
        self.__noagregoMonstruo = boolean #si el ingresado es false, significa que ya agregó una en ese turno
        #y que no puede agregar más 
    

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
        eleccion = input("1. Si \n2. No \n > ");
        while eleccion != "1"  and eleccion != "2":
            print("Elige un numero entre 1 y 2")
            eleccion = input(" > ");

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
                seleccion = input(" > ")
            
            cartaSeleccionada = espacioCartasMonstruo[int(seleccion) - 1];
            cartaSeleccionada.setIsInAtaque(not(cartaSeleccionada.getIsInAtaque()));
            
        else:
            print("WARNING| No existen cartas Monstruo boca Arriba para cambiar su posicion")
            
            
    
    def declararBatalla(self, enemigo, partida): 
        '''Metodo para iniciar batalla entre cartas,
        se asocia con ataqueEntreCartas() de Tablero'''
                #TypeHint para evitar confusiones
        tablero : Tablero = partida.getTablero();
        espacioCartasMonstruoJ = tablero.tablerocompartido[self.__id]["CartasMonstruo"]

        #Validacion existan cartas monstruo
        #Verifica que haya cartas en modo ataque e implicitamente q existan cartas en el espacio
            #preguntamos si desea atacar
        print("|    Ejecutar ataque?")
        eleccion = input("1. Si \n2. No \n > ");
        #validamos su seleccion
        while eleccion != "1"  and eleccion != "2":
            print("Elige un numero entre 1 y 2")
            eleccion = input(" > ");
        #Validacion existan cartas monstruo
        while tablero.hayCartasMonstruoEnAtaque(self) and eleccion == "1": #Verifica que haya cartas en modo ataque e implicitamente q existan cartas en el espacio
            #si enetró en el while es porque quiere atacar
            print("Elige tu carta de ataque: ")
            i = 0;
            #mostramos las cartas a elegir del jugador propio, y solo las que estan en posicion de ataque y estan
            #boca arriba damos permiso de atacar;
            for cartaMonstruo in espacioCartasMonstruoJ:
                print(f'{i+1}. {cartaMonstruo.toString3()}')
                i += 1;
            seleccion = input(" > ")
            # validacion por si el usuario pone letras  o se pasa del rango-_-
            while (not seleccion.isdigit()) or (int(seleccion)> i  or int(seleccion) <= 0):
                print("Por favor, ingresa un número válido.")
                seleccion = input(" > ")

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
                        print(f"{cartaTrampa.getNombre()} detiene el ataque de un monstruo con tipo de atributo {cartaTrampa.getTipoAtributo()}")
                        print("| Carta Trampa eliminada del tablero")
                        tablero.quitarCartaTablero(cartaTrampa, enemigo.getId())
                        cartaSeleccionada.setPuedeAtacar(False);


                        
                    #caso en el que no tenga
                    else: 
                        #el danio del atacante aniadido con las cartas magicas lo sacamos accediendo a su carta magica asociada
                        incAtkJugador = cartaSeleccionada.getMagica().getIncrementoAtaque()
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
                            print(f'{i+1}. {cartaMonstruo.toString2()}')
                        else: 
                            print(f'{i+1}. CARTA MONSTRUO|| *** Carta boca abajo ***')
                        i+=1
                    seleccion = input(" > ")
                    # validacion por si el usuario pone letras  o se pasa del rango-_-
                    while (not seleccion.isdigit()) or (int(seleccion)> i  or int(seleccion) <= 0):
                        print("Por favor, ingresa un número válido.")
                        seleccion = input(" > ")
                    
                    cartaEnemigaSeleccionada = espacioEnemigo[int(seleccion)-1]

                    #Ejecutamos el ataque:

                    danioAEnemigo , danioAJugador = tablero.ataqueEntreCartas(cartaSeleccionada, cartaEnemigaSeleccionada, self, enemigo)

                    #Actualizamos la vida de los jugadores
                    #!comprobar si se puede acceder directamente
                    self.__puntosVida = self.__puntosVida - danioAJugador;
                    enemigo.__puntosVida =  enemigo.__puntosVida - danioAEnemigo;
                    cartaSeleccionada.setPuedeAtacar(False);

            else:
                    #dividimos en un if para ser mas especifico con la advertencia al usuario
                if cartaSeleccionada.getIsInAtaque():
                    print("WARNING| La carta seleccionada ya ha atacado en este Turno.")
                elif cartaSeleccionada.getPuedeAtacar():
                    print("WARNING| La carta seleccionada no esta en modo de ataque")            #cambiamos el estado de la carta  seleccionada para que ya no se pueda utilizar en el turno. OJO
            #Especificaciones funcion:
            # verificar si no es el primer turno -> se lo valida en otra funcion de partida o del main CHEC (en "ronda")
            #Da a elegir al jugador con q carta Monstruo de su tablero quiere atacar y a cual de la otras quiere atacar CHECK
            # se ataca directamente implicitamente CHECK
            # primero verifica si tiene cartas mosntruo en el tablero, sino ataca directamente CHECK
            # actualiz la vida del jugador CHECK
            # se cambia el atributo  de la carta elegida puedeAtacar a False CHECK
            '''vuelve a preguntar y eleccion se actualiza'''
            print("|    Ejecutar ataque?")
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
        #1 mostrar en cada turno del jugador sus cartas en mano, luego preguntarle si desea aniadir alguna
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
            if len(tablero.tablerocompartido[self.__id]["CartasMonstruo"])<3 and self.__noagregoMonstruo:
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
                self.setNoAgregoMonstruo(False)
            else:
                #if para especificar mejor la advertencia al usuario
                if len(tablero.tablerocompartido[self.__id]["CartasMonstruo"])<3:
                    print("WARNING| Ya no puedes colocar mas cartas mosntruos en este turno")
                else:
                    print("WARNING| Has alcanzado el limite de cartas mosntruos en el tablero")
        #Caso si la carta es trampa
        elif isinstance(cartaSeleccionada, CartaTrampa):
            #validamos que haya espacio
            if len(tablero.tablerocompartido[self.__id]["CartasEspeciales"])<3:
                #Aniadimos la carta a tablero
                tablero.aniadirCartaTablero(cartaSeleccionada, self.__id)
            else:
                print("WARNING| No se puede agregar mas cartas Magicas o Trampa") 
        #Caso si la carta seleccionada es Magica
        elif isinstance(cartaSeleccionada, CartaMagica):
            #validamos que ya exista un monstruo en el tablero con mismo atributo de la carta
            if tablero.validarAgregacionCartaMagica(cartaSeleccionada, self):
                espacioCartasMonstruoJ = tablero.tablerocompartido[self.__id]["CartasMonstruo"]
                #Mostramos las cartas monstruo:
                print("| Selecciona el monstruo al cual asociar la carta Magica")
                i = 0 
                for cartaMonstruo in espacioCartasMonstruoJ:
                    print(f'{i+1}. {cartaMonstruo.toString3()}')
                    i += 1       

                seleccion = input("Selecciona la carta a Asociar: \n > ")
                # validacion por si el usuario pone letras  o se pasa del rango-_-
                while  (not seleccion.isdigit()) or (int(seleccion)> i  or int(seleccion) <= 0):
                    print("Por favor, ingresa un número válido.")
                    seleccion = input(" > ")
                cartaAAsociar: CartaMonstruo = espacioCartasMonstruoJ[int(seleccion)-1]

                #validamos que la cartaMonstruo seleccionada a asociar sea del mismo atributo que la carta
                #magica seleccionada previamente
                if cartaAAsociar.getTipoMonstruo() == cartaSeleccionada.getTipoMonstruo():
                    #seteamos la nueva carta magica a esta carta Monstruo
                    cartaAAsociar.setMagica(cartaSeleccionada)
                    tablero.aniadirCartaTablero(cartaSeleccionada, self.__id)

                else: 
                    print(f'WARNING| La carta Magica elegida no se puede asociar a la carta Monstruo "{cartaAAsociar.getNombre()}" ')
            else: 
                print(f'WARNING| No existe carta Monstruo en tablero con la cual asociarla')
       

    def imprimirMano(self):
        ###Imprime por consola las cartas en mano que tiene el jugador'''
        for Carta in self.__cartasEnMano:
            print(Carta.toString2())

    def listarCartasEnMano(self):
        ###retorna una lista solo con el nombre de las cartas en mano
        cartas = []
        for Carta in self.__cartasEnMano:
            cartas.append(Carta.getNombre())
        return cartas


    #Metodos de la maquina

    def declararBatallaComoMaquina(self, tablero: Tablero, oponente):
    
        input(f"La {self.getNombre()} te va a declarar batalla!! {oponente.getNombre()} estás preparadx?: " )

        # Obtener monstruos en ataque que pueden atacar
        monstruosAtacantes = []
        cartasMagicas=[]
        cartasTrampa=[]
        
        for carta in tablero.getTableroCompartido()[self.getId()]["CartasMonstruo"]:
            if carta.getIsInAtaque() and carta.getPuedeAtacar():
                monstruosAtacantes.append(carta)

        # Si no hay monstruos en ataque, cambiar a modo defensa
        if len(monstruosAtacantes) == 0:
            print(f"La {self.getNombre()} no tiene monstruos disponibles para atacar. Se coloca a la defensiva.")
            for carta in tablero.tablerocompartido[self.getId()]["CartasMonstruo"]:
                if carta.getIsInAtaque():
                    carta.setIsInAtaque(False)
                    carta.setIsBocaArriba(False)
                    print(f"---> {self.getNombre()} pone al monstruo {carta.getNombre()} en defensa.")
            return
        
        # Obtener monstruos del oponente
        monstruosOponente = tablero.tablerocompartido[oponente.getId()]["CartasMonstruo"]

        #Obtener cartas magicas y cartas trampa
        for carta in tablero.getTableroCompartido()[self.getId()]["CartasEspeciales"]:
            if isinstance(carta, CartaTrampa):
                cartasTrampa.append(carta)
            elif isinstance(carta, CartaMagica):
                cartasMagicas.append(carta)

        #Funcion de carta magica
        for cartaMagica in cartasMagicas:
            if tablero.validarAgregacionCartaMagica(cartaMagica, self):
                for monstruo in tablero.getTableroCompartido()[self.getId()]["CartasMonstruo"]:
                    if monstruo.getTipoMonstruo() == cartaMagica.getTipoMonstruo():
                        if cartaMagica.getIncrementoAtaque() > 0:
                            monstruo.setAtaque(monstruo.getAtaque() + cartaMagica.getIncrementoAtaque())
                            print(f"---> {self.getNombre()} equipa '{cartaMagica.getNombre()}' a '{monstruo.getNombre()}', aumentando su ataque en {cartaMagica.getIncrementoAtaque()}.")
                        elif cartaMagica.getIncrementoDefensa() > 0:
                            monstruo.setDefensa(monstruo.getDefensa() + cartaMagica.getIncrementoDefensa())
                            print(f"---> {self.getNombre()} equipa '{cartaMagica.getNombre()}' a '{monstruo.getNombre()}', aumentando su defensa en {cartaMagica.getIncrementoDefensa()}.")
                        tablero.quitarCartaTablero(cartaMagica, self.getId())  # Eliminar la carta mágica tras equiparla
                        break      

        #Funcion de carta mounstro y carta  trampa               
        for cartaAtacante in monstruosAtacantes:
            cartaTrampa = tablero.verificarCartaTrampa(oponente, cartaAtacante)
            if cartaTrampa:
                print(f"---> {oponente.getNombre()} activa la carta trampa '{cartaTrampa.getNombre()}' y detiene el ataque de '{cartaAtacante.getNombre()}'.")
                tablero.quitarCartaTablero(cartaTrampa, oponente.getId())  # Descarta la carta trampa
                continue
            if len(monstruosOponente) > 0:
                cartaDefensora = monstruosOponente[0]
                print(f"---+ {cartaAtacante.getNombre()} ataca a {cartaDefensora.getNombre()}!")
                tablero.ataqueEntreCartas(cartaAtacante, cartaDefensora, self, oponente)
            else:
                print(f"{cartaAtacante.getNombre()} realiza un ataque directo")
                oponente.setPuntosVida(oponente.getPuntosVida() - cartaAtacante.getAtaque())
            cartaAtacante.setPuedeAtacar(False)

            print(f"{self.getNombre()} ha terminado su fase de batalla.")
            print(f"=========================================================")



    def llenarTableroMaquina(self, tablero: Tablero):
        print(f"La {self.getNombre()} está organizando su tablero.")
        input("Loading....")
        #print(self.imprimirMano()) solo fue para encontrar el error
        mano_maquina = self.getCartasEnMano().copy()
        print("")
        # Colocar cartas de monstruo
        for carta in mano_maquina:
            if isinstance(carta, CartaMonstruo):
                if self.__noagregoMonstruo: #si no se ha agregadomonstruo en ese turno #seactualiza en fase (Partida())
                    if len(tablero.tablerocompartido[2]["CartasMonstruo"]) < 3:
                        tablero.aniadirCartaTablero(carta, 2) #quita automat la carta de la mano
                        print(f"{self.getNombre()} coloca al monstruo {carta.getNombre()} en el tablero.")
                        self.setNoAgregoMonstruo(False)#yatieneun monstruo agregado

        # Colocar cartas mágicas o trampas
            else: #si no es monstruo será cualquier otra
                if len(tablero.tablerocompartido[2]["CartasEspeciales"]) < 3:
                    tablero.aniadirCartaTablero(carta, 2)
                    print(f"{self.getNombre()} coloca una carta especial: {carta.getNombre()}.")

        print(f"{self.getNombre()} ha terminado de organizar su tablero.")
        input("Enter para seguir  ")

        ### FIN DE LAS FUNCIONES DE MAQUINA
    
        
    def esDerrotado(self):
        ##verifica que el jugador fue derrotado
        NoTieneCartas= len(self.getCartasEnMano())==0 and len(self.getDeck().getBaraja())==0
        return self.getPuntosVida()<=0 or NoTieneCartas
     #devuelve true si esderrotado
    
         
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

