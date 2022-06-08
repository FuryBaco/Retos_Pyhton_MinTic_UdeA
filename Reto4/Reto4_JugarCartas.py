'''from random import shuffle
tipos_cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
n_palos = 4
baraja = tipos_cartas * n_palos
shuffle(baraja)
print(baraja)'''


baraja = ['3', 'A', '2', 'Q', 'J', '9', '6', '7', '10', '6', '7', 'A', 'Q', '9', 'J', '2', '3', 'K', '10', 'Q', 'J', '8', '4', '6', '4', '5', 'Q', '4', '7', '8', '8', 'A', '8', '3', '5', '5', '3', 'J', 'K', '6', '2', '4', '7', 'K', 'A', '10', '10', '5', '2', '9', 'K', '9']

def tiene_cartas_altas(cartas_siguientes):
  cartas_altas = ['A', 'J', 'Q', 'K']
  for carta in cartas_siguientes:
    if carta in cartas_altas:
      return True
  return False  

def jugar(baraja):
  p, p1, p2 = 1, 0, 0
  cartas_jugadas = []
  cartas_altas = {'A':1, 'J':2, 'Q':3, 'K':4}
  while len(baraja) > 0:
    p = 1 if p == 0 else 0
    carta_jugada = baraja.pop(0)
    cartas_jugadas.append(carta_jugada)
    if carta_jugada not in cartas_altas:
      continue
    else:
      cj = cartas_altas[carta_jugada] 
      if not tiene_cartas_altas(baraja[0:cj]) and len(baraja) > (cj - 1):
        p1,p2 = (p1+cj, p2+0) if p == 0 else (p1+0,p2+cj)
      
  return p1,p2

solucion = jugar(baraja)
print('------------------------------------------------------')
print(solucion[:2])
print('------------------------------------------------------')
'''print(solucion[2])
print('------------------------------------------------------')
print(solucion[3])'''

      
  
 
