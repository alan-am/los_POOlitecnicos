class Deck:
    
    def __init__(self,rutaArchivo):
        listaCartas = self.cargarCartas(rutaArchivo);
        self.baraja = self.asignarCartas(self.barajear(listaCartas));
    
    #Getters y setters 
    def getBaraja(self):
        return self.__baraja
    def setBaraja(self, nueva_baraja):
         self.__baraja = nueva_baraja

    def getListaCartas(self):
        return self.__listaCartas
    def setListaCartas(self, nueva_lista):
        self.__listaCartas = nueva_lista

       
    def baraja(self):
        return self.baraja
    
    def listacartas(self):
        return self._listaCartas
    
    def cargarCartas(rutaArchivo):
        '''Crea cartas y las aniade a una lista de cartas sacadas a partir de un
        archivo, luego la retorna'''
        pass;
    def barajear(listaCartas):
        '''desordena una lista de cartas'''
    def asignarCartas(listaCartas):
        '''De una lista de cartas, retorna una nueva lista con 
        20 cartas monstruo, 5 magicas y 5 trampas'''
    def robarCarta():
        '''devuelve un carta para el jugador traida de la baraja y la borra
        de la baraja'''