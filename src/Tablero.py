class Tablero:

    #Constructor
    def __init__(self, id):
        self.__id = id;
        cartasMonstruo = [];
        cartasEspeciales = [];
    
    #Getters y setters
    def getId(self):
        return self.__id
    def setId(self, nuevo_id):
        self.__id = nuevo_id

    def getCartasMonstruo(self):
        return self.__cartasMonstruo
    def setCartasMonstruo(self, nuevas_cartas):
            self.__cartasMonstruo = nuevas_cartas

    def getCartasEspeciales(self):
        return self.__cartasEspeciales
    def setCartasEspeciales(self, nuevas_cartas):
            self.__cartasEspeciales = nuevas_cartas


    #Metodos
    def aniadirCarta(c):
        '''metodo para aniadir cartas al tablero, a las listas'''
        pass;

    def quitarCarta(c):
        '''metodo para quitar cartas del tablero, 
        eliminar de las listas'''
        pass;



