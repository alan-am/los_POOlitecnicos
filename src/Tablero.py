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
        #cambie la importacion pq daba errores poniendola al pricipio.
        from Jugador import Jugador

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
    

    def hayCartasMonstruoBocaArriba(self, jugador):
        '''Verifica si existen cartas monstruo en ataque en el espacio del jugador,
        devuelve un booleano , si no hay -> False '''
        espacioMosntruosJ = self.tablerocompartido[jugador.getId()]["CartasMonstruo"]
        i = 0;
        for cartaMonstruo in espacioMosntruosJ:
            if cartaMonstruo.getIsBocaArriba():
                i += 1;
        
        return i > 0;
    def hayCartasMonstruoEnAtaque(self, jugador):
        espacioMosntruosJ = self.tablerocompartido[jugador.getId()]["CartasMonstruo"]
        i = 0;

        for cartaMonstruo in espacioMosntruosJ:
            if cartaMonstruo.getIsInAtaque():
                i += 1;
        
        return i > 0;

    def verificarCartaTrampa(self, enemigo, cartaAtacante):
        '''Funcion que verifica si el enemigo en su tablero tiene una carta Trampa que lo beneficie
         ante el ataque de una carta Del otro jugador, devuelve la carta Trampa encontrada. '''
        espacioEspecialesJ = self.tablerocompartido[enemigo.getId()]["CartasEspeciales"]
        cartaEncontrada = None
        for cartaEspecial in espacioEspecialesJ:
            if isinstance(cartaEspecial, CartaTrampa):
                atributoCarta = cartaEspecial.getTipoAtributo()
                if atributoCarta == cartaAtacante.getTipoAtributo():
                    cartaEncontrada = cartaEspecial;
        
        return cartaEncontrada
    
    def verificarCartasMagicas(self, jugador, cartaMonstruo):
        '''Itera en el espacio de cartas especiales del jugador, validando cuales
         coinciden con el tipo de monstruo de 'carta' y va sumando los incrementos de ataque y defensa
          retorna dicha tupla de valores '''
        espacioEspecialesJ = self.tablerocompartido[jugador.getId()]["CartasEspeciales"]
        incAtk = 0;
        incDef = 0;
        for cartaEspecial in espacioEspecialesJ:
            if isinstance(cartaEspecial, CartaMagica):
                if cartaEspecial.getTipoMonstruo() == cartaMonstruo.getTipoMonstruo():
                    incAtk += cartaEspecial.getIncrementoAtaque()
                    incDef += cartaEspecial.getIncrementoDefensa()

        return incAtk, incDef; 

    def destruirCartaMagica(self, jugador):
        '''Verifica si existen cartasMonstruo en el tablero con igual atributos de
        cartas magicas en el tablero, carta magica que no encuentra coincidencias es eliminada
        del tablero.'''
        #puede ser usada cuando un monstruo muera en batalla
        espacioEspecialesJ = self.tablerocompartido[jugador.getId()]["CartasEspeciales"]
        espacioMonstruosJ = self.tablerocompartido[jugador.getId()]["CartasMonstruo"]
        CartasMagicas = []
        Tip_Monstruo=[]
        #hace una lista de solo cartas magicas
        for cartaEspecial in espacioEspecialesJ:
            if isinstance(cartaEspecial, CartaMagica):
                CartasMagicas.append(cartaEspecial)
        #recoge los atributos de las cartasmosntruos del tablero
        for cartaMonstruo in espacioMonstruosJ:
            Tip_Monstruo.append(cartaMonstruo.getTipoMonstruo().value)
        #si no hay monstruos de igual tipo que la carta, esta se elimina del tablero
        for cartita in CartasMagicas:
            if cartita.getTipoMonstruo().value not in Tip_Monstruo:
                espacioEspecialesJ.remove(cartita)
  



        
    
    #Revisar lo que recibe
    def ataqueEntreCartas(self, cartaJugador, cartaEnemigo, jugador, enemigo):    #!->>> devuelvo una tupla bien definida?
        '''Realiza la logica del ataque entre cartas , verificando si existen cartas trampas o 
        magicas que beneficien a los jugadores y tiene en cuenta los distintos caso de ataque - ataque y 
        ataque - defensa; retorna una tupla con el valor real del danio recibido al enemigo y al atacante'''
        jugadorID = jugador.getId();
        enemigoID = enemigo.getId();

        #Antes de atacar debo verificar si existen cartas trampas q impidan el ataque
        if self.verificarCartaTrampa(enemigo, cartaJugador) is None:
            
            #Antes de atacar debo verificar si existen cartas magicas q incrementen los valores de ataque
            incAtkJugador, incDefJugador = self.verificarCartasMagicas(jugador, cartaJugador)
            incAtkEnemigo, incDefEnemigo = self.verificarCartasMagicas(enemigo, cartaEnemigo)

            #Comprobamos si la carta enemigo esta en ataque
            if cartaEnemigo.getIsInAtaque():
                
                if (cartaJugador.getAtaque() + incAtkJugador ) > (cartaEnemigo.getAtaque()+incAtkEnemigo):
                    danioRealAEnemigo = (cartaJugador.getAtaque() + incAtkJugador ) - (cartaEnemigo.getAtaque()+incAtkEnemigo) ;
                    danioRealAJugador = 0;
                    #formato salida
                    print(f"| Choque de ataques | {cartaJugador.getNombre()} vs {cartaEnemigo.getNombre()}")
                    print(f"\t {cartaJugador.getAtaque()} + {incAtkJugador}  -->  <--  {cartaEnemigo.getAtaque()} + {incAtkEnemigo}")
                    print(f"| {cartaJugador.getNombre()} destruyó a {cartaEnemigo.getNombre()} en batalla!")
                    self.quitarCarta(cartaEnemigo,enemigoID)
                    return danioRealAEnemigo, danioRealAJugador;
            
                elif (cartaJugador.getAtaque() + incAtkJugador ) == (cartaEnemigo.getAtaque()+incAtkEnemigo):
                    danioRealAJugador = 0;
                    danioRealAEnemigo = 0;
                    print(f"| Choque de ataques | {cartaJugador.getNombre()} vs {cartaEnemigo.getNombre()}")
                    print(f"\t {cartaJugador.getAtaque()} + {incAtkJugador}  -->  <--  {cartaEnemigo.getAtaque()} + {incAtkEnemigo}")
                    print(f"| {cartaJugador.getNombre()} destruyó a {cartaEnemigo.getNombre()} en batalla!")
                    print(f"| {cartaEnemigo.getNombre()} destruyó a {cartaJugador.getNombre()} en batalla!")
                    self.quitarCarta(cartaEnemigo,enemigoID)
                    self.quitarCarta(cartaJugador,jugadorID)

                    return danioRealAEnemigo, danioRealAJugador;
            
                elif (cartaJugador.getAtaque() + incAtkJugador ) < (cartaEnemigo.getAtaque()+incAtkEnemigo):
                    danioRealAEnemigo = 0
                    danioRealAJugador = (cartaEnemigo.getAtaque()+incAtkEnemigo) - (cartaJugador.getAtaque() + incAtkJugador )
                    print(f"| Choque de ataques | {cartaJugador.getNombre()} vs {cartaEnemigo.getNombre()}")
                    print(f"\t {cartaJugador.getAtaque()} + {incAtkJugador}  -->  <--  {cartaEnemigo.getAtaque()} + {incAtkEnemigo}")
                    print(f"| {cartaEnemigo.getNombre()} destruyó a {cartaJugador.getNombre()} en batalla!")
                    self.quitarCarta(cartaJugador,jugadorID);

                    return danioRealAEnemigo, danioRealAJugador;
            
            else:
                if (cartaJugador.getAtaque() + incAtkJugador ) > (cartaEnemigo.getDefensa() + incDefEnemigo):
                    print(f"| Ataque y Defensa | {cartaJugador.getNombre()} vs {cartaEnemigo.getNombre()}")
                    print(f"\t {cartaJugador.getAtaque()} + {incAtkJugador}  -->  <--  {cartaEnemigo.getDefensa()} + {incDefEnemigo}")
                    print(f"| {cartaJugador.getNombre()} destruyó a {cartaEnemigo.getNombre()} en batalla!")
                    self.quitarCarta(cartaEnemigo,enemigoID)
                    #la carta en defensa debe cambiar a boca arriba
                    cartaEnemigo.setIsBocaArriba(True)

                    #no se realiza danio ni al atacante ni al defensor
                    return 0, 0

                elif (cartaJugador.getAtaque() + incAtkJugador ) < (cartaEnemigo.getDefensa() + incDefEnemigo):
                    danioRealAJugador = (cartaEnemigo.getDefensa() + incDefEnemigo) - (cartaJugador.getAtaque() + incAtkJugador )
                    print(f"| Ataque y Defensa | {cartaJugador.getNombre()} vs {cartaEnemigo.getNombre()}")
                    print(f"\t {cartaJugador.getAtaque()} + {incAtkJugador}  -->  <--  {cartaEnemigo.getDefensa()} + {incDefEnemigo}")
                    print("Has recibido daño!");
                    danioRealAEnemigo = 0 

                    #la carta en defensa debe cambiar a boca arriba
                    cartaEnemigo.setIsBocaArriba(True)
                    #no se destruye ningun monstruo
                    return danioRealAEnemigo, danioRealAJugador;
    
        else: 
            #Si no es None Significa que si hay una carta trampa que detiene el ataque del jugador
            cartaTrampa = self.verificarCartaTrampa(enemigo, cartaJugador);
            print(f"| La carta trampa {cartaTrampa.getNombre()} detuvo el Ataque!")
            #eliminamos la carta trampa ya utilizada del tablero del enemigo
            self.quitarCarta(cartaTrampa, enemigoID);
            return 0, 0




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



