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
    #getters 
    def getTipoMonstruo(self):
        return self.__tipoMonstruo
    def getincrementoAtaque(self):
        return self.__incrementoAtaque
    def getincrementoDefensa(self):
        return self.__incrementoDefensa
    #setters
    def setincrementoDefensa(self,n_incrementodefensa):
        self.__incrementoDefensa = n_incrementodefensa
    def setincrementoAtaque(self,n_incrementoataque):
        self.__incrementoAtaque = n_incrementoataque
    def setTipoMonstruo(self,tipoMonstruo):
        self.__tipoMonstruo = tipoMonstruo


    #to String
    def toString(self):
        return f'''{"CARTA MAGICA".center(55,"~")}
{super().getNombre().center(55, "~")}
    Tipo: {self.__tipoMonstruo.value}
    Incremento Ataque: {self.__incrementoAtaque}
    Incremento Defensa: {self.__incrementoDefensa}
{"Descripcion".center(55, "~")}
{super().getDescripcion().center(55)}
{"~".center(55, "~")}'''
    

#SUB-CLASE 
class CartaMonstruo(Carta):
    def __init__(self,nombre,descripcion,ataque,defensa,TipoMonstruo,TipoAtributo):
        super().__init__(nombre, descripcion)
        self.__ataque = ataque
        self.__defensa = defensa
        self.__tipoMonstruo = TipoMonstruo 
        self.__tipoAtributo = TipoAtributo 
        self.__isInAtaque = True; #* por defecto
        self.__isBocaArriba = True; #* por defecto
        self.__puedeAtacar = True; #* por defecto

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
    
    def getTipoMounstro(self):
        return self.__tipoMonstruo
    def setTipoMounstro(self, nuevoTipoMounstro):
        self.__tipoMonstruo=nuevoTipoMounstro

    def getTipoAtributo(self):
        return self.__tipoAtributo
    def setTipoAtributo(self, nuevoTipoAtributo):
        self.__tipoAtributo=nuevoTipoAtributo
    

    #Metodos
    def atacar(Carta):
        '''Debe atacar a otra cara '''
        pass

    #to String
    def toString(self):
        return f'''{"CARTA MONSTRUO".center(55, "-")}
{super().getNombre().center(55, "-")}
    Tipo: {self.__tipoMonstruo.value}{f"Atributo: {self.__tipoAtributo.value}":>22}
    ATK: {self.__ataque}{f"DEF: {self.__defensa}":>27} 
    MODO DE ATAQUE: {self.__isInAtaque}
{"Descripcion".center(55, "-")}
{super().getDescripcion().center(55)}
{"-".center(55, "-")}'''  

#lo de :> era para intentar darle mejor aspecto pero no se logró


#SUB-CLASE
class CartaTrampa(Carta):
    def __init__(self,nombre, descripcion,TipoAtributo):
        super().__init__(nombre, descripcion)
        self.__isBocaArriba = True; #* por defecto
        self.__tipoAtributo = TipoAtributo

                                                    
    #Getters y setters
    def getIsBocaArriba(self):
        return self.__isBocaArriba
    def setIsInAtaque(self, valor_booleano):
        self.__isBocaArriba = valor_booleano;

    def getIsTipoAtributo(self):
        return self.__tipoAtributo
    def setIsTipoAtributo(self, nuevoTipoAtributo):
        self.__tipoAtributo=nuevoTipoAtributo

        


    #to String
    def toString(self):
        return f'''{"CARTA TRAMPA".center(55, ".")}
{super().getNombre().center(55, ".")}
    Atributo: {self.__tipoAtributo.value}
{"Descripcion".center(55, ".")}
{super().getDescripcion().center(55)}
{".".center(55, ".")}'''   



