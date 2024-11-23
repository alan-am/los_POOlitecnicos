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



# isInAtaque = true/false;   de ser falso siginificaria q esta en defensa
# isBocaArriba = true/false;  de ser falso significaria q esta boca abajo

