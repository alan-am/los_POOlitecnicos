class Carta:
    def __init__(self, nombre,descripcion):
        self.__nombre = nombre
        self.__descripcion = descripcion
        
    #Getters y setters
    def getNombre(self):
        return self.__nombre
    def getDescripcion(self):
        return self.__descripcion
    def setNombre(self,nombrenuevo):
        self.__nombre = nombrenuevo
    def setDescripcion(self,descrnueva):
        self.__descripcion = descrnueva


#un commit
