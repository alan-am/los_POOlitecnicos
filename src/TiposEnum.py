import enum as e

class TipoAtributo(e.Enum):
    OSCURIDAD = "OSCURIDAD"
    LUZ = "LUZ"
    VIENTO = "VIENTO"
    AGUA = "AGUA"
    FUEGO = "FUEGO"
    TIERRA = "TIERRA"

class TipoMonstruo(e.Enum):
    L = "Lanzador de Conjuros"
    D = "Dragón"
    Z = "Zombi"
    G = "Guerrero"
    B = "Bestia"
    O = "Demonio"


#!Mayra elimina todo lo de abajo cuando lo veas xd, elimine estos enum pq 
#como literal son son 2 opciones que tienen tipoposicion y bocaabajo, 
#para no complicarnos es mejor dejar las variables como un booleano, tipo:
# isInAtaque = true/false;   de ser falso siginificaria q esta en defensa
# isBocaArriba = true/false;  de ser falso significaria q esta boca abajo

# class TipoPosicion(e.Enum):
#     ATAQUE = "ATAQUE"
#     DEFENSA= "DEFENSA"

# class bocaAbajo(e.Enum):
#     TRUE = "boca abajo"
#     FALSE = "boca arriba"
