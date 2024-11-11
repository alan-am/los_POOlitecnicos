class Carta:
    def __init__(self, id,nombre,descripcion,Deck):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._deck = Deck
    def ponerBocaArriba():
        pass
    def ponerBocaAbajo():
        pass

class CartaMagica(Carta):
    def __init__(self, id, nombre, descripcion,deck, incrementoAtaque, incrementoDefensa, TipoMonstruo):
        super().__init__(id,nombre, descripcion,deck)
        self.__incrementoAtaque = incrementoAtaque
        self.__incrementoDefenda = incrementoDefensa
        self.__tipomonstruo = TipoMonstruo

class CartaMonstruo(Carta):
    def __init__(self,id,nombre,descripcion,deck,ataque,defensa,TipoMonstruo,TipoAtributo,TipoPosicion):
        super().__init__(id,nombre, descripcion,deck)
        self.__ataque = ataque
        self.__defensa = defensa
        self.__tipomonstruo = TipoMonstruo
        self.__tipoatributo = TipoAtributo
        self.__tipoPosicion = TipoPosicion

class CartaTrampa(Carta):
    def __init__(self,id,nombre, descripcion,deck,bocaAbajo,TipoAtributo):
        super().__init__(id,nombre, descripcion,deck)
        self.__bocaAbajo = bocaAbajo
        self.__TipoAtributo = TipoAtributo
    
