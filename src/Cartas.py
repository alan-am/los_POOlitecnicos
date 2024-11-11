class Carta:
    def __init__(self, id,nombre,descripcion,deck):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._deck = deck
    def mostrar_info(self):
        return f"Nombre {self._nombre}\nDescripcion: {self._descripcion}"

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
    def mostrar_info(self):
        return f"Nombre {self._nombre}\nDescr {self._descripcion}\nataque {self.__ataque}\nTipo de Atributo :{self.__tipoatributo}"

class CartaTrampa(Carta):
    def __init__(self,id,nombre, descripcion,deck,bocaAbajo,TipoAtributo):
        super().__init__(id,nombre, descripcion,deck)
        self.__bocaAbajo = bocaAbajo
        self.__TipoAtributo = TipoAtributo
    
