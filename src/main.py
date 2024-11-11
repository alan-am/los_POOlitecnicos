import Cartas
import Deck
import TiposEnum as t

def main():
    monstruo = Cartas.CartaMonstruo(1,"Dragon","escupe fuego","deck",45,78,t.TipoMonstruo.D, t.TipoAtributo.AGUA.value,t.TipoPosicion.ATAQUE.value)
    return monstruo
print(main().mostrar_info())