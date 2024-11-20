from TiposEnum import *
#SUPER-CLASE
class Carta:
    #atributo estatico para manejar los id
    cartas = 0
    def __init__(self,nombre,descripcion):
        Carta.cartas += 1;
        self.__id = Carta.cartas;  
        self.__nombre = nombre
        self.__descripcion = descripcion
        #self.__deck = deck


     #GETTER Y SETTERS
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
    
    def getDescripcion(self):
        return self.__descripcion
    def setDescripcion(self, nuevaDescripcion):
        self.__descripcion = nuevaDescripcion
    
    def getId(self):
        return self.__id;

#SUB-CLASE
class CartaMagica(Carta):
    def __init__(self, nombre, descripcion, incrementoAtaque, incrementoDefensa, TipoMonstruo):
        super().__init__(nombre, descripcion)
        self.__incrementoAtaque = incrementoAtaque
        self.__incrementoDefensa = incrementoDefensa
        self.__tipoMonstruo = TipoMonstruo

    #Getters y Setters

    #String Of
    def stringOf(self):
        return f'''{self.__nombre.center(40, "~")}
        ~   Tipo: {self.__tipoMonstruo.value}                   ~
        ~   Incremento Ataque: {self.__incrementoAtaque}        ~
        ~   Incremento Defensa: {self.__incrementoDefensa}      ~
        ~  {"Descripcion".center(40, "~")}
        ~{self.__descripcion}
        {"~".center(40, "~")}'''   
    

#SUB-CLASE
class CartaMonstruo(Carta):
    def __init__(self,nombre,descripcion,ataque,defensa,TipoMonstruo,TipoAtributo):
        super().__init__(nombre, descripcion)
        self.__ataque = ataque
        self.__defensa = defensa
        self.__tipoMonstruo = TipoMonstruo #falta getter y setter
        self.__tipoAtributo = TipoAtributo #falta getter y setter
        self.__isInAtaque = True; #* por defecto
        self.__isBocaArriba = True; #* por defecto
        self.__puedeAtacar = True; #* por defecto
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}\nAtaque: {self.__ataque}\nDefensa: {self.__defensa}\nTipo de Monstruo:{self.__tipoMonstruo.value}\nTipo de atributo: {self.__tipoAtributo.value}\n ModoAtaque: {self.__isInAtaque}"
    
    def atacar(Carta):
        #ataque a otra carta
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
    
    def getIsBocaArriba(self):
        return self.__isBocaArriba;
    def setIsBocaArriba(self, valor_Booleano):
        self.__isBocaArriba = valor_Booleano;

    def getIsInAtaque(self):
        return self.__isInAtaque
    def setIsInAtaque(self, valor_booleano):
        self.__isInAtaque = valor_booleano;

    def getPuedeAtacar(self):
        return self.__puedeAtacar;
    def setPuedeAtacar(self, valor_booleano):
        self.__puedeAtacar = valor_booleano;
    
    #String Of
    def stringOf():
        pass;


#SUB-CLASE
class CartaTrampa(Carta):

    def __init__(self,nombre, descripcion,TipoAtributo):
        super().__init__(nombre, descripcion)
        self.__isBocaArriba = True; #* por defecto
        self.__TipoAtributo = TipoAtributo
        
    def mostrar_info(self):
        return f"{super().mostrar_info()}\nTipo de Atributo: {self.__TipoAtributo.value}"


    #Getters and Setters

    def getIsBocaArriba(self):
        return self.__isBocaArriba;
    def setIsBocaArriba(self, valor_Booleano):
        self.__isBocaArriba = valor_Booleano;

    #String Of
    def stringOf():
        pass;