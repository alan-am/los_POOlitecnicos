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

class TipoPosicion(e.Enum):
    ATAQUE = "Boca arriba"
    DEFENSA= "Boca abajo"

class bocaAbajo(e.Enum):
    TRUE = "boca abajo"
    FALSE = "boca arriba"
