tipos_cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', 'Q', 'K']
n_palos = int(4)

from random import shuffle

def generar_baraja(tipos_cartas, n_palos):
    # ACÁ INICIA LA FUNCIÓN
    baraja = tipos_cartas * n_palos
    shuffle(baraja)
    baraja = tuple(baraja)
    # ACÁ TERMINA LA FUNCIÓN
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return baraja

deck_shuffled = generar_baraja(tipos_cartas, n_palos)
print(deck_shuffled)

