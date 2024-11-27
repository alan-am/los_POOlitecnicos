from Deck import Deck
from Cartas import *
class Tablero:

    #Constructor
    def __init__(self):
        from Jugador import Jugador
        self.__id = 1;
        self.__jugador1 = self.aniadirJugador();
        self.__jugador2 = Jugador("Maquina", Deck());            
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
            print(f"+----Carta {Carta.getNombre()} añadida")
            self.quitarCarta_Mano(id_jugador,Carta)
            
        elif (isinstance(Carta,CartaMagica) or isinstance(Carta,CartaTrampa)) and len(self.tablerocompartido[id_jugador]["CartasEspeciales"])<3:
            self.tablerocompartido[id_jugador]["CartasEspeciales"].append(Carta)
            print(f"+----Carta {Carta.getNombre()} añadida")
            self.quitarCarta_Mano(id_jugador,Carta)
        else:
            print(f"No se pudo incluir esa carta, espacio lleno") ## para avisarle al jugador que alcanzó el límite¿?no estoy segura de esto


    def quitarCartaTablero(self,Carta,id_jugador): #parametro carta añadido, id_jugador
        '''metodo para quitar cartas del tablero, 
        eliminar de las listas'''
        if isinstance(Carta,CartaMonstruo): #isintance es como instanceof de java
            self.tablerocompartido[id_jugador]["CartasMonstruo"].remove(Carta)
        else:
            self.tablerocompartido[id_jugador]["CartasEspeciales"].remove(Carta)
    
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
    
    def destruirCartaMagica(self, id_jugador):
        '''Verifica si existen cartasMonstruo en el tablero con igual atributos de
        cartas magicas en el tablero, carta magica que no encuentra coincidencias es eliminada
        del tablero.'''
        #puede ser usada cuando un monstruo muera en batalla
        espacioEspecialesJ = self.tablerocompartido[id_jugador]["CartasEspeciales"]
        espacioMonstruosJ = self.tablerocompartido[id_jugador]["CartasMonstruo"]
        CartasMagicas = []
        Tip_Monstruo=[]
        #hace una lista de solo cartas magicas
        for cartaEspecial in espacioEspecialesJ:
            if isinstance(cartaEspecial, CartaMagica):
                CartasMagicas.append(cartaEspecial)
        #recoge los atributos de las cartasmosntruos del tablero
        for cartaMonstruo in espacioMonstruosJ:
            Tip_Monstruo.append(cartaMonstruo.getTipoMonstruo())
        #si no hay monstruos de igual tipo que la carta, esta se elimina del tablero
        for cartita in CartasMagicas:
            if cartita.getTipoMonstruo() not in Tip_Monstruo:
                espacioEspecialesJ.remove(cartita)
  



        
    
    #Revisar lo que recibe
    def ataqueEntreCartas(self, cartaJugador: CartaMonstruo, cartaEnemigo, jugador, enemigo):    #!->>> devuelvo una tupla bien definida?
        '''Realiza la logica del ataque entre cartas , verificando si existen cartas trampas o 
        magicas que beneficien a los jugadores y tiene en cuenta los distintos caso de ataque - ataque y 
        ataque - defensa; retorna una tupla con el valor real del danio recibido al enemigo y al atacante'''
        jugadorID = jugador.getId();
        enemigoID = enemigo.getId();

        #Antes de atacar debo verificar si existen cartas trampas q impidan el ataque
        if self.verificarCartaTrampa(enemigo, cartaJugador) is None:
            
            #Antes de atacar debo verificar si existen cartas magicas q incrementen los valores de ataque
            incAtkJugador, incDefJugador = cartaJugador.getCartaMagica().getIncrementoAtaque(), cartaJugador.getCartaMagica().getIncrementoDefensa()
            incAtkEnemigo, incDefEnemigo = cartaEnemigo.getCartaMagica().getIncrementoAtaque(), cartaEnemigo.getCartaMagica().getIncrementoDefensa()

            #Comprobamos si la carta enemigo esta en ataque
            if cartaEnemigo.getIsInAtaque():
                
                if (cartaJugador.getAtaque() + incAtkJugador ) > (cartaEnemigo.getAtaque()+incAtkEnemigo):
                    danioRealAEnemigo = (cartaJugador.getAtaque() + incAtkJugador ) - (cartaEnemigo.getAtaque()+incAtkEnemigo) ;
                    danioRealAJugador = 0;
                    #formato salida
                    print(f"|| Choque de ataques ||     ||{cartaJugador.getNombre()} vs {cartaEnemigo.getNombre()}||")
                    print(f"\t {cartaJugador.getAtaque()} + {incAtkJugador}  -->  <--  {cartaEnemigo.getAtaque()} + {incAtkEnemigo}")
                    print(f"| {cartaJugador.getNombre()} destruyó a {cartaEnemigo.getNombre()} en batalla!")
                    #Se elimina la carta magica asociada y la propia carta del enemigo
                    self.quitarCartaTablero(cartaEnemigo,enemigoID)
                    self.eliminarCartaMagicaAsociada(enemigo, cartaEnemigo)
                    return danioRealAEnemigo, danioRealAJugador;
            
                elif (cartaJugador.getAtaque() + incAtkJugador ) == (cartaEnemigo.getAtaque()+incAtkEnemigo):
                    danioRealAJugador = 0;
                    danioRealAEnemigo = 0;
                    print(f"|| Choque de ataques ||     ||{cartaJugador.getNombre()} vs {cartaEnemigo.getNombre()}||")
                    print(f"\t {cartaJugador.getAtaque()} + {incAtkJugador}  -->  <--  {cartaEnemigo.getAtaque()} + {incAtkEnemigo}")
                    print(f"| {cartaJugador.getNombre()} destruyó a {cartaEnemigo.getNombre()} en batalla!")
                    print(f"| {cartaEnemigo.getNombre()} destruyó a {cartaJugador.getNombre()} en batalla!")

                    self.quitarCartaTablero(cartaEnemigo,enemigoID)
                    self.eliminarCartaMagicaAsociada(enemigo, cartaEnemigo)
                    self.quitarCartaTablero(cartaJugador,jugadorID)
                    self.eliminarCartaMagicaAsociada(jugador, cartaJugador)

                    return danioRealAEnemigo, danioRealAJugador;
            
                #elif (cartaJugador.getAtaque() + incAtkJugador ) < (cartaEnemigo.getAtaque()+incAtkEnemigo):
                else: #si no es mayor y no es igual, el último caso es que será menor
                    #hice esto porque tiraba error, ya que no todos los caminos tenían un return válido
                    danioRealAEnemigo = 0
                    danioRealAJugador = (cartaEnemigo.getAtaque()+incAtkEnemigo) - (cartaJugador.getAtaque() + incAtkJugador )
                    print(f"|| Choque de ataques ||     ||{cartaJugador.getNombre()} vs {cartaEnemigo.getNombre()}||")
                    print(f"\t {cartaJugador.getAtaque()} + {incAtkJugador}  -->  <--  {cartaEnemigo.getAtaque()} + {incAtkEnemigo}")
                    print(f"| {cartaEnemigo.getNombre()} destruyó a {cartaJugador.getNombre()} en batalla!")
                    self.quitarCartaTablero(cartaJugador,jugadorID);
                    self.eliminarCartaMagicaAsociada(jugador, cartaJugador)


                    return danioRealAEnemigo, danioRealAJugador;
            
            else:
                if (cartaJugador.getAtaque() + incAtkJugador ) >= (cartaEnemigo.getDefensa() + incDefEnemigo):
                    print(f"|| Ataque y Defensa ||      ||{cartaJugador.getNombre()} vs {cartaEnemigo.getNombre()}||")
                    print(f"\t {cartaJugador.getAtaque()} + {incAtkJugador}  -->  <--  {cartaEnemigo.getDefensa()} + {incDefEnemigo}")
                    print(f"| {cartaJugador.getNombre()} destruyó a {cartaEnemigo.getNombre()} en batalla!")
                    self.quitarCartaTablero(cartaEnemigo,enemigoID)
                    self.eliminarCartaMagicaAsociada(enemigo, cartaEnemigo)
                    
                    #la carta en defensa debe cambiar a boca arriba
                    cartaEnemigo.setIsBocaArriba(True)
                    #aunque no lo dice el juego, puse >= para que no dé error
                    #no se realiza danio ni al atacante ni al defensor
                    return 0, 0

                elif (cartaJugador.getAtaque() + incAtkJugador ) < (cartaEnemigo.getDefensa() + incDefEnemigo):
                    danioRealAJugador = (cartaEnemigo.getDefensa() + incDefEnemigo) - (cartaJugador.getAtaque() + incAtkJugador )
                    print(f"|| Ataque y Defensa ||      ||{cartaJugador.getNombre()} vs {cartaEnemigo.getNombre()}||")
                    print(f"\t {cartaJugador.getAtaque()} + {incAtkJugador}  -->  <--  {cartaEnemigo.getDefensa()} + {incDefEnemigo}")
                    danioRealAEnemigo = 0 

                    #la carta en defensa debe cambiar a boca arriba
                    cartaEnemigo.setIsBocaArriba(True)
                    #no se destruye ningun monstruo
                    return danioRealAEnemigo, danioRealAJugador;
    
        else: 
            #Si no es None Significa que si hay una carta trampa que detiene el ataque del jugador
            cartaTrampa = self.verificarCartaTrampa(enemigo, cartaJugador);
            print(f"|    La carta trampa {cartaTrampa.getNombre()} detuvo el Ataque!")
            #eliminamos la carta trampa ya utilizada del tablero del enemigo
            self.quitarCartaTablero(cartaTrampa, enemigoID);
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
    def getTableroCompartido(self):
        return self.tablerocompartido


    def eliminarCartaMagicaAsociada(self, jugador, cartaMonstruo: CartaMonstruo):
        '''Recibe un jugador, evalua si la carta monstruo dada posee una carta magica 
        asociada, una vez verificado determina el id de la carta magica y luego busca
        en el tablero del jugador dicha carta por su id , y procede a eliminarla'''

        #validamos que la carta mosntruo tenga una carta asociada
        if cartaMonstruo.getCartaMagica().getNombre() != "Carta Defecto":
            id_cartaMagicaAsociada = cartaMonstruo.getCartaMagica().getId()
            espacioCartasEspecialesJ = self.tablerocompartido[jugador.getId()]["CartasEspeciales"]
            i = 0
            indiceCarta = None;
            for cartaEspecial in espacioCartasEspecialesJ:
                id_cartaEspecial = cartaEspecial.getId()
                if isinstance(cartaEspecial, CartaMagica) and id_cartaMagicaAsociada == id_cartaEspecial:
                    indiceCarta = i;
                i+=1;
            cartaAEliminar = espacioCartasEspecialesJ[indiceCarta]
            self.quitarCartaTablero(cartaAEliminar,jugador.getId())


    def validarAgregacionCartaMagica(self, cartaMagica: CartaMagica, jugador):
        '''Recibe un carta magica, determina su tipo de atributo e itera el espacio
        de mosntruos del jugador par aver si existe algun mosntruo del mismo atributo, retorna
        un boolean'''
        espacioMonstruosJ = self.tablerocompartido[jugador.getId()]["CartasMonstruo"]
        i = 0 ;
        for cartaMonstruo in espacioMonstruosJ:
            if cartaMonstruo.getTipoMonstruo() == cartaMagica.getTipoMonstruo():
                i += 1;

        return i > 0 

    
    def toString(self):
        cartas_j1 = self.tablerocompartido[1]
        cartas_j2= self.tablerocompartido[2]
        dic_m_1= {}
        dic_e_1 ={}
        dic_m_2 ={}
        dic_e_2 ={}
        mostrar_m1=[]
        def llenar_dic(dic_m,dic_e,diclleno): #diclleno seria cartas_j1
            cartas_m = diclleno["CartasMonstruo"]
            cartas_e = diclleno["CartasEspeciales"]
            i = 1
            a = 1
            for monstruo in cartas_m:
                if monstruo.getIsBocaArriba():
                    dic_m[i] = [monstruo.getNombre(),monstruo.getAtaque(),monstruo.getDefensa()]
                else:
                    dic_m[i] = [monstruo.getNombre(),"|--???--|","|--???--|"]
                i+=1
            for especial in cartas_e:
                if isinstance(especial,CartaMagica):
                    if especial.getIsBocaArriba():
                        dic_e[a] = [especial.getNombre(),especial.getIncrementoAtaque(),especial.getIncrementoDefensa()]
                    else:
                        dic_e[a] = [especial.getNombre(),"|--???--|","|--???--|"]

                else: #si es de trampa solo se guarda el nombre
                    dic_e[a] = [especial.getNombre(),"----Carta Trampa----"]
                a+=1
        
               
        llenar_dic(dic_m_1,dic_e_1,cartas_j1)
        llenar_dic(dic_m_2,dic_e_2,cartas_j2)
        


        return f'''{"TABLERO".center(70,"-")}
{"Jugador 1".center(70,"=")}
----+ Puntos de vida :{self.getJugador1().getPuntosVida()}
Monstruo        Ataque---Defensa
{dic_m_1.get(1,"----+espacio vacío+----")}
{dic_m_1.get(2,"----+espacio vacío+----")}
{dic_m_1.get(3,"----+espacio vacío+----")}

Especiales: 
Mágicas          Inc.ATK---Inc.DEF
{dic_e_1.get(1,"----+espacio vacío+----")}
{dic_e_1.get(2,"----+espacio vacío+----")}
{dic_e_1.get(3,"----+espacio vacío+----")}

{"Máquina".center(70,"=")}
----+ Puntos de vida :{self.getJugador2().getPuntosVida()}
Monstruo        Ataque---Defensa
-------------------------------------------------------
{dic_m_2.get(1,"----+espacio vacío+----")}
{dic_m_2.get(2,"----+espacio vacío+----")}
{dic_m_2.get(3,"----+espacio vacío+----")}

Especiales: 
Mágicas          Inc.ATK---Inc.DEF
{dic_e_2.get(1,"----+espacio vacío+----")}
{dic_e_2.get(2,"----+espacio vacío+----")}
{dic_e_2.get(3,"----+espacio vacío+----")}


'''
    





#OBSOLETA
'''
def verificarCartasMagicas(self, jugador, cartaMonstruo):
    #Itera en el espacio de cartas especiales del jugador, validando cuales
    #coinciden con el tipo de monstruo de 'carta' y va sumando los incrementos de ataque y defensa
    #retorna dicha tupla de valores 
    espacioEspecialesJ = self.tablerocompartido[jugador.getId()]["CartasEspeciales"]
    incAtk = 0;
    incDef = 0;
    for cartaEspecial in espacioEspecialesJ:
        if isinstance(cartaEspecial, CartaMagica):
            if cartaEspecial.getTipoMonstruo() == cartaMonstruo.getTipoMonstruo():
                incAtk += cartaEspecial.getIncrementoAtaque()
                incDef += cartaEspecial.getIncrementoDefensa()

    return incAtk, incDef; 

'''



