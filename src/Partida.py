from Tablero import Tablero
from Cartas import *
import random
import Jugador

class Partida:
    
    #Constructor
    def __init__(self):
        self.__id = 1;
        self.__turno = 1;
        self.__tablero = Tablero();
        self.__jugadoractual = 1; #por defecto es 1, es el id del jugador actual
        self.__ronda = 1; 
    

   #Getters y setters
    def getId(self):
        return self.__id
    def setId(self, nuevo_id):
        self.__id = nuevo_id

    def getTablero(self):
        return self.__tablero;
    def setTablero(self, nuevo_tablero):
        self.__tablero = nuevo_tablero;

    def getTurno(self):
        return self.__turno
    def setTurno(self, nuevo_turno):
        self.__turno = nuevo_turno

    def getJugadorActual(self):
        return self.__jugadoractual
    def getRonda(self):
        return self.__ronda
   
    #Metodos


    #una "ronda" es un turno por jugador (2 en total), en la primera ronda no se puede declarar batalla
    def ronda(self):
        '''se encarga de que el juego tenga secuencia'''
        j1 = self.getTablero().getJugador1()
        maquina = self.getTablero().getJugador2()
        jugador_actual = self.getJugadorActual()
        if self.__ronda == 1:
            #no se puede declarar batalla
            for i in range(2):
                self.faseTomarCarta(j1,maquina)
                self.fasePrincipal(j1,maquina)
                #print del tablero para que el jugador vea como queda
                print(self.getTablero().toString()) #Aniadido Alan
                self.cambiarTurno()
            print("Es su primer turno, no puede declarar batalla")
        else: 
            for i in range(2):#por cada jugador
                self.faseTomarCarta(j1,maquina)
                
                self.fasePrincipal(j1,maquina)
                print(f"{"-"*30}")
                self.faseBatalla(j1,maquina)
                #luego de la batalla, busca las cartas inservibles y chao
                self.getTablero().destruirCartaMagica(jugador_actual)
                #print del tablero para que el jugador vea como queda
                self.getTablero().toString() #Aniadido Alan 
                #reestablece el estado de las cartas para el siguiente turno
                self.resetearEstadoCartasMounstro(jugador_actual)
                #cambia de un jugador a otro, cambia turno
                self.cambiarTurno()  
        #por cada ronda se hace esto:

        self.__ronda+=1
        print("Comenzará una nueva ronda")
        print(f"{'=='*40}")




    def faseTomarCarta(self,j1,j2):
        """Es la fase en la cual un jugador roba una carta de su deck, si es su primer turno, toma 5 cartas"""
        if self.__turno <=3 and (len(j1.getCartasEnMano())==0 or len(j2.getCartasEnMano())==0): #verifica que sea el primer turno de cada jugador
            if j1.getId() == self.__jugadoractual:
                j1.tomar5Cartas()
            else:
                self.__tablero.getJugador2().tomar5Cartas()
        else: #cuando haya pasado la primera ronda, se toma una sola carta por turno
            if self.__jugadoractual ==1:
                j1.tomarCartaEnTurno()
            else:
                print(f"{"Turno de la maquina".center(30,"-")}") #!Print para test, luego eliminar
                j2.tomarCartaEnTurno()
        
 

    def fasePrincipal(self,j1:Jugador,maquina:Jugador):
        
        if self.getJugadorActual() ==1: #si está jugando el usuario se llama a la función jugar carta
            #!Logica aniadida para para que el jugador elija cuantas quiera ...
            jugar = input("--> Desea añadir una carta en su tablero? (si/no) ").lower()
            #while jugar not in ["si","no"]:
            #    jugar = input("--> ¿Desea añadir una carta en su tablero? (si/no) ").lower()
            while jugar == "si":
                j1.jugarCarta(self)
                jugar = input("--> ¿Desea añadir una carta en su tablero? (si/no) ").lower()


        else: #si es el turno de la maquina, se llama a 
            maquina.llenarTableroMaquina(self.getTablero())
    
    def faseBatalla(self,j1:Jugador,maquina:Jugador):
        #verifica quien va a declarar batalla, de quien es el turno
        if self.getJugadorActual() ==1:
            j1.declararBatalla(maquina,self)
        else: #es decir si el turno es de la maquina
            maquina.declararBatallaComoMaquina(self.getTablero(), j1)

       
    



    def sorteoInicios(self,j1, j2):
        print("¡Bienvenido al juego de YuGiOH!")
        JugadoresIniciales = [j1,j2]
        JugadorEmpieza = random.choice(JugadoresIniciales)
        self.__turno = JugadorEmpieza.getId()#con esto ya modifiqué el turno por primera vez
        self.__jugadoractual = self.__turno 
        print(f"El jugador que empieza es: {JugadorEmpieza.getNombre()} -Id: {JugadorEmpieza.getId()}")
        
    def cambiarTurno(self):
        ###Cambia el turno al siguiente jugador
        '''los turnos irán aumentando siempre
        jugador 1: turnos:1,3,5,... (impares)
        jugador 2: turnos:2,4,6,...(pares)
        para el jugador 1 su primer turno será self.___turno = 1 y para el jugador 2 : self.__turno = 2
        esto ayudará en el control de la fase inicial'''
        self.__turno+=1
        if self.__turno %2==0:
            self.__jugadoractual = 2 #id de jugador, turno del jugador 2
        else:
            self.__jugadoractual = 1 
        
        #intenté acomodar este método


    def resetearEstadoCartasMounstro(self, id_jugador):
        """Después de cada turno, resetear el estado de las cartas monstruo"""
        jugador = None
        if id_jugador == 1:
            jugador = self.getTablero().getJugador1()
        else:
            jugador = self.getTablero().getJugador2()
        for carta in jugador.getCartasEnMano():
            if isinstance(carta, CartaMonstruo):
                carta.setPuedeAtacar(True)
                #by Alan, lo de abajo no va, solo se resetea el PuedeAtacar 
                #carta.setIsInAtaque(True)
    
    
    def finalizarPartida(self, j1, j2):
        """Finaliza la partida determinando el ganador."""
        if j1.esDerrotado():
            print(f"El jugador{j1.getNombre()} ha sido derrotado.")
            print(f"El ganador es {j2.getNombre()}!")
        elif j2.esDerrotado():
            print(f"El jugador {j2.getNombre()} ha sido derrotado.")
            print(f"El ganador es {j1.getNombre()}!")
        else:
            print("La partida se acabo, terminaron en empate !!")


    


        