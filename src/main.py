from Deck import Deck
from Jugador import Jugador
from Partida import Partida
from Tablero import Tablero

tablero1 = Tablero(1)
deck1 = Deck('a')
j1  = Jugador(1, 4000, tablero1, deck1)

print(j1.puntosVida)

