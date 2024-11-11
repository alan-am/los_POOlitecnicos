from Deck import Deck
from Jugador import Jugador
from Partida import Partida
from Tablero import Tablero
import TiposEnum as t
import Cartas


def main():
    monstruo = Cartas.CartaMonstruo(1,"Dragon","escupe fuego","deck",45,78,t.TipoMonstruo.D, t.TipoAtributo.AGUA.value,t.TipoPosicion.ATAQUE.value)
    nom = monstruo.getNombre()
    return nom
    

print(main())

tablero1 = Tablero(1)
deck1 = Deck('a')
j1  = Jugador(1, 4000, tablero1, deck1)

print(j1.getPuntosVida())
