#SUPER-CLASE
class Carta:
    def __init__(self, id,nombre,descripcion,deck):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__deck = deck


    def mostrar_info(self):
        return f"Nombre: {self._nombre}\nDescripcion: {self._descripcion}"

    def ponerBocaArriba():
        pass
    def ponerBocaAbajo():
        pass

     #GETTER Y SETTERS
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
    
    def getDescripcion(self):
        return self.__descripcion
    def setDescripcion(self, nuevaDescripcion):
        self.__descripcion = nuevaDescripcion

#SUB-CLASE
class CartaMagica(Carta):
    def __init__(self, id, nombre, descripcion,deck, incrementoAtaque, incrementoDefensa, TipoMonstruo):
        super().__init__(id,nombre, descripcion,deck)
        self.__incrementoAtaque = incrementoAtaque
        self.__incrementoDefensa = incrementoDefensa
        self.__tipomonstruo = TipoMonstruo
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}\nIncremento Ataque: {self.__incrementoAtaque}\nIncremento Defensa: {self.__incrementoDefensa}\nTipo de Monstruo: {self.__TipoMonstruo.value}"

#SUB-CLASE
class CartaMonstruo(Carta):
    def __init__(self,id,nombre,descripcion,deck,ataque,defensa,TipoMonstruo,TipoAtributo,TipoPosicion):
        super().__init__(id,nombre, descripcion,deck)
        self.__ataque = ataque
        self.__defensa = defensa
        self.__tipomonstruo = TipoMonstruo
        self.__tipoatributo = TipoAtributo
        self.__tipoPosicion = TipoPosicion
    def mostrar_info(self):
        return f"{super().mostrar_info()}\nAtaque: {self.__ataque}\nDefensa: {self.__defensa}\nTipo de Monstruo:{self.__tipomonstruo.value}\nTipo de atributo: {self.__tipoatributo.value}\nTipo de Posicion: {self.__tipoPosicion.value}"
    def atacar(Carta):
        #ataque a otra carta
        pass
    def cambiarPosicion(Posicion):
        pass

    #GETTER Y SETTERS
    def getAtaque(self):
        return self.__ataque
    
    def setAtaque(self, nuevoAtaque):
        self.__ataque = nuevoAtaque

    
    def getDefensa(self):
        return self.__defensa
    
    def setDefensa(self, nuevaDefensa):
        self.__defensa = nuevaDefensa

#SUB-CLASE
class CartaTrampa(Carta):

    def __init__(self,id,nombre, descripcion,deck,bocaAbajo,TipoAtributo):
        super().__init__(id,nombre, descripcion,deck)
        self.__bocaAbajo = bocaAbajo
        self.__TipoAtributo = TipoAtributo
        
    def mostrar_info(self):
        return f"{super().mostrar_info()}\nTipo de Atributo: {self.__TipoAtributo.value}"

