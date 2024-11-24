from Tablero import Tablero
from Cartas import CartaMonstruo
import random
from Jugador import *

class Partida:
    
    #Constructor
    def __init__(self):
        self.__id = 1;
        self.__turno = 1;
        self.__tablero = Tablero();
        self.__jugadoractual = 1; #por defecto es 1, es el id del jugador actual
        self.__ronda = 0; 
    

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
        '''dentro de la ronda, pueden ejecutarse las funciones de fases,cada jugador tiene que pasar por todas
        las fases en cada ronda,¿?'''
        j1 = self.getTablero().getJugador1()
        maquina = self.getTablero().getJugador2()
        if self.__ronda ==1:
            #no se puede declarar batalla
            pass
        else: 
            #se ejecutan las 3 fases de forma normal
            pass
        #por cada ronda se hace esto:
        self.resetearEstadoCartasMounstro() 
        self.getTablero().destruirCartaMagica() 
        self.__ronda+=1



    def faseTomarCarta(self):
        """Es la fase en la cual un jugador roba una carta de su deck, si es su primer turno, toma 5 cartas"""
        j1= self.__tablero.getJugador1()
        j2 = self.__tablero.getJugador2()
        if self.__turno <=3 and (len(j1.getCartasEnMano())==0 or len(j2.getCartasEnMano())==0): #verifica que sea el primer turno de cada jugador
            if j1.getId() == self.__jugadoractual:
                j1.tomar5Cartas()
            else:
                self.__tablero.getJugador2().tomar5Cartas()
        else: #cuando haya pasado la primera ronda, se toma una sola carta por turno
            if self.__jugadoractual ==1:
                j1.tomarCartaEnTurno()
            else:
                j2.tomarCartaEnTurno()
 

    def fasePrincipal(self,j1,maquina):
        
        j1 = self.getTablero().getJugador1()
        if self.getJugadorActual() ==1: #si está jugando el usuario se llama a la función jugar carta
                pass
        else: #si es el turno de la maquina, se llama a 
            maquina.llenarTableroMaquina()
    
    def faseBatalla(self,j1,maquina):
        #verifica quien va a declarar batalla, de quien es el turno
        if self.getJugadorActual() ==1:
            j1.declararBatalla(maquina,self)
        else: #es decir si el turno es de la maquina
            maquina.declararBatallaComoMaquina()

       
    



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


    def resetearEstadoCartasMounstro(self, jugador):
        """Después de cada turno, resetear el estado de las cartas monstruo"""
        for carta in jugador.getCartasEnMano():
            if isinstance(carta, CartaMonstruo):
                carta.setPuedeAtacar(True)
                carta.setIsInAtaque(True)
    
    
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


    


        