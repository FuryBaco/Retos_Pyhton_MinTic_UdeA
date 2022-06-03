from random import shuffle

tipos_cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', 'Q', 'K']
n_palos = int(4)


def generar_baraja(tipos_cartas, n_palos):
    # ACÁ INICIA LA FUNCIÓN
    #baraja = [item for item in tipos_cartas for i in range(n_palos)]
    #shuffle(baraja)
    #baraja = tuple(baraja)
    baraja=[]
    for carta in tipos_cartas:
        for palo in range(n_palos):
            baraja.append(carta)
    shuffle(baraja)
    baraja=tuple(baraja)
    # ACÁ TERMINA LA FUNCIÓN
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return baraja

respuesta = generar_baraja(tipos_cartas, n_palos)
print(respuesta)