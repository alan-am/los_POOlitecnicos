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
            print("--- Es su primer turno, no puede declarar batalla")
        else: 
            for i in range(2):#por cada jugador
                if not j1.esDerrotado() and not maquina.esDerrotado():
                    self.faseTomarCarta(j1,maquina)
                    print(f"{'-'*30}")
                    self.fasePrincipal(j1,maquina)
                    print(f"{'-'*30}")
                    self.faseBatalla(j1,maquina)
                    #luego de la batalla, busca las cartas inservibles y chao
                    #funcion desactualizada
                    #self.getTablero().destruirCartaMagica(jugador_actual)
                    #print del tablero para que el jugador vea como queda
                    input("> Da enter para mostrar el tablero actualizado ")
                    print(self.getTablero().toString()) #Aniadido Alan 
                    #reestablece el estado de las cartas para el siguiente turno
                    self.resetearEstadoCartasMounstro2()
                    #cambia de un jugador a otro, cambia turno
                    self.cambiarTurno()  
        #por cada ronda se hace esto:
        if not j1.esDerrotado() and not maquina.esDerrotado():
            self.__ronda+=1
            input(f"Presione enter para comenzar una nueva ronda ")
            input("Loading...")

            print(f"------> Ronda {self.__ronda} comienza:")
            print(f"{'=='*40}")
    




    def faseTomarCarta(self,j1,j2):
        """Es la fase en la cual un jugador roba una carta de su deck, si es su primer turno, toma 5 cartas"""
        if self.__turno <=3 and (len(j1.getCartasEnMano())==0 or len(j2.getCartasEnMano())==0): #verifica que sea el primer turno de cada jugador
            if j1.getId() == self.__jugadoractual:
                j1.tomar5Cartas()
                print(f"|   {j1.getNombre()} ha tomado 5 cartas del deck")
            else:
                self.__tablero.getJugador2().tomar5Cartas()
                print(f"|   {j2.getNombre()} ha tomado 5 cartas del deck")
        else: #cuando haya pasado la primera ronda, se toma una sola carta por turno
            if self.__jugadoractual ==1:
                print("-Es tu turno de robar una carta-")
                input("Presiona enter para tomar la carta del Deck...  ")
                j1.tomarCartaEnTurno()
            else:
                print(f'{"Turno de la maquina".center(30,"-")}')
                 #!Print para test
                print("|    La máquina ya ha robado su carta")
                j2.tomarCartaEnTurno()
        
 

    def fasePrincipal(self,j1:Jugador,maquina:Jugador):
        
        if self.getJugadorActual() ==1: #si está jugando el usuario se llama a la función jugar carta
            #!Logica aniadida para que el jugador elija cuantas quiera ...
            j1.setNoAgregoMonstruo(True)
            input("|--> Presiona enter para visualizar tus cartas en mano ")
            j1.imprimirMano()
            print("Desea añadir una carta en su tablero??")
            eleccion = input("1. Si \n2. No \n>");
            #validamos su seleccion
            while eleccion != "1"  and eleccion != "2":
                print("Elige un numero entre 1 y 2")
                eleccion = input("> ");
            #while jugar not in ["si","no"]:
            #    jugar = input("--> ¿Desea añadir una carta en su tablero? (si/no) ").lower()
            while eleccion == "1":
                j1.jugarCarta(self)
                print("Desea añadir una carta en su tablero?")
                eleccion = input("1. Si \n2. No \n>");
                while eleccion != "1"  and eleccion != "2":
                    print("Elige un numero entre 1 y 2")
                    eleccion = input("> ");


        else: #si es el turno de la maquina, se llama a 
            maquina.setNoAgregoMonstruo(True)
            maquina.llenarTableroMaquina(self.getTablero())
    
    def faseBatalla(self,j1:Jugador,maquina:Jugador):
        #verifica quien va a declarar batalla, de quien es el turno
        if self.getJugadorActual() ==1:
            j1.declararBatalla(maquina,self)
        else: #es decir si el turno es de la maquina
            maquina.declararBatallaComoMaquina(self.getTablero(), j1)

       
    



    def sorteoInicios(self,j1, j2):
        print("¡Bienvenido al juego de 𝐘𝐔𝐆𝐈-𝐎𝐇 !")
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


    def resetearEstadoCartasMounstruo(self, id_jugador):
    #Después de cada turno, resetear el estado de las cartas monstruo de ataque se reinicia 
        jugador = None
        if id_jugador == 1:
            jugador = self.getTablero().getJugador1()
        else:
            jugador = self.getTablero().getJugador2()
        for carta in jugador.getCartasEnMano():
            if isinstance(carta, CartaMonstruo):
                carta.setPuedeAtacar(True)               
               

    
    
    def finalizarPartida(self, j1, j2):
        """Finaliza la partida determinando el ganador."""
        if j1.esDerrotado():
            print(f"El jugador {j1.getNombre()} ha sido derrotado.")
            print(f"La ganadora es la {j2.getNombre()}!")
        elif j2.esDerrotado():
            print(f"La {j2.getNombre()} ha sido derrotada.")
            print(f"El ganador es {j1.getNombre()}!")



    def resetearEstadoCartasMounstro2(self): #Prueba # la funcion original parece que no etsa funcionando bien
        '''Resetea el atributo .puedeAtacar de las cartas mosntruo en el tablero de cada jugador'''
        #guardamos el id de cada jugador en el tablero
        idJ1 = self.__tablero.getJugador1().getId()
        idJ2 = self.__tablero.getJugador1().getId()

        #Accedemos al espacio de cartas monstruo de cada jugador
        espacioCartasMonstruoJ1 =  self.__tablero.tablerocompartido[idJ1]["CartasMonstruo"]
        espacioCartasMonstruoJ2 =  self.__tablero.tablerocompartido[idJ2]["CartasMonstruo"]

        #iteramos en cada carta mosntruo de cada espacio cambiando el atributo puedeAtacar
        for cartaMonstruo in espacioCartasMonstruoJ1:
            cartaMonstruo.setPuedeAtacar(True);
        for cartaMonstruo in espacioCartasMonstruoJ2:
            cartaMonstruo.setPuedeAtacar(True);






    def mostrarReglas(self):
        '''Muestra al usuario las reglas de este juego de cartas yugioh'''
        pass;
    
    def presentacionCreadores(self):
        print("\n\nJuego codificado por: \n")
        print("Mayra Lucas - Estudiante de Espol en ingeniería en Ciencias de la Computación".center(100))
        print("Geovanny Lacouture - Estudiante de Espol en ingeniería en Ciencias de la Computación".center(100))
        print("Alan Aguilar - Estudiante de Espol en ingeniería en Ciencias de la Computación".center(100))
        print("<3".center(100))

        input("...  Game over")

        