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



     #Getters y setters 
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
        self.__isBocaArriba = True; #* por defecto
    #getters 
    def getTipoMonstruo(self):
        return self.__tipoMonstruo.value
    def getIncrementoAtaque(self):
        return self.__incrementoAtaque
    def getIncrementoDefensa(self):
        return self.__incrementoDefensa
    def getIsBocaArriba(self):
        return self.__isBocaArriba;

    #setters
    def setIncrementoDefensa(self,n_incrementodefensa):
        self.__incrementoDefensa = n_incrementodefensa
    def setIncrementoAtaque(self,n_incrementoataque):
        self.__incrementoAtaque = n_incrementoataque
    def setTipoMonstruo(self,tipoMonstruo):
        self.__tipoMonstruo = tipoMonstruo
    def setIsBocaArriba(self, valor_Booleano):
        self.__isBocaArriba = valor_Booleano;


    ###to String
    def toString(self):
        return f'''{"CARTA MAGICA".center(55,"~")}
{super().getNombre().center(55, "~")}
    Tipo: {self.__tipoMonstruo.value}
    Incremento Ataque: {self.__incrementoAtaque}
    Incremento Defensa: {self.__incrementoDefensa}
{"Descripcion".center(55, "~")}
{super().getDescripcion().center(55)}
{"~".center(55, "~")}'''
    
    #Segundo to String, menos descriptivo y mas conciso
    def toString2(self):
        return f'''CARTA MAGICA|| {self.getNombre()} [INC ATK: {self.__incrementoAtaque}, INC DEF: {self.__incrementoDefensa}]
        Tipo: {self.__tipoMonstruo.value} '''
    

#SUB-CLASE 
class CartaMonstruo(Carta):
    def __init__(self,nombre,descripcion,ataque,defensa,TipoMonstruo,TipoAtributo):
        super().__init__(nombre, descripcion)
        self.__ataque = ataque
        self.__defensa = defensa
        self.__tipoMonstruo = TipoMonstruo 
        self.__tipoAtributo = TipoAtributo 
        self.__isInAtaque = True; #* por defecto #! si se pone en defensa se coloca boca abajo
        self.__isBocaArriba = True; #* por defecto #se muestra el atk/def al imrpimir
        self.__puedeAtacar = True; #* por defecto #true si puede atacar en ese turno

    #Getters y setters 
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
    
    def getTipoMonstruo(self):
        return self.__tipoMonstruo.value
    def setTipoMonstruo(self, nuevoTipoMounstro):
        self.__tipoMonstruo=nuevoTipoMounstro

    def getTipoAtributo(self):
        return self.__tipoAtributo.value #->
    def setTipoAtributo(self, nuevoTipoAtributo):
        self.__tipoAtributo=nuevoTipoAtributo
    

    #Metodos
    def atacar(self, cartaEnemiga):
        '''Debe atacar a otra carta ''' 
        


    ###to String
    def toString(self):
        return f'''{"CARTA MONSTRUO".center(55, "-")}
{super().getNombre().center(55, "-")}
    Tipo: {self.__tipoMonstruo.value}   Atributo: {self.__tipoAtributo.value}
    ATK: {self.__ataque}                DEF: {self.__defensa}
    MODO DE ATAQUE: {self.__isInAtaque}
{"Descripcion".center(55, "-")}
{super().getDescripcion().center(55)}
{"-".center(55, "-")}'''
    
    #Segundo to String, menos descriptivo y mas conciso
    def toString2(self):
        var = "Defensa"
        if self.__isInAtaque:
            var = "Ataque"

        return f'''CARTA MONSTRUO|| {self.getNombre()} [ATK: {self.__ataque}, DEF: {self.__defensa}]
        Tipo: {self.__tipoMonstruo.value}, ATR: {self.__tipoAtributo.value}, MODO: {var}'''





#SUB-CLASE
class CartaTrampa(Carta):
    def __init__(self,nombre, descripcion,TipoAtributo):
        super().__init__(nombre, descripcion)
        self.__isBocaArriba = False; #* por defecto
        self.__tipoAtributo = TipoAtributo

                                                    
    #Getters y setters
    def getIsBocaArriba(self):
        return self.__isBocaArriba
    def setIsInAtaque(self, valor_booleano):
        self.__isBocaArriba = valor_booleano;

    def getTipoAtributo(self):
        return self.__tipoAtributo.value    #Ojo debe ponerse .value
    def setTipoAtributo(self, nuevoTipoAtributo):
        self.__tipoAtributo=nuevoTipoAtributo

        


    ###to String
    def toString(self):
        return f'''{"CARTA TRAMPA".center(55, ".")}
{super().getNombre().center(55, ".")}
    Atributo: {self.__tipoAtributo.value}
{"Descripcion".center(55, ".")}
{super().getDescripcion().center(55)}
{".".center(55, ".")}''' 
    
    #Segundo to String, menos descriptivo y mas conciso
    def toString2(self):
        return f'''CARTA TRAMPA|| {self.getNombre()} Atributo: {self.__tipoAtributo.value}'''




