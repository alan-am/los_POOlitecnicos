class Deck:
    
    def __init__(self,rutaArchivo):
        listaCartas = self.cargarCartas(rutaArchivo);
        self.__baraja = self.asignarCartas(self.barajear(listaCartas));

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