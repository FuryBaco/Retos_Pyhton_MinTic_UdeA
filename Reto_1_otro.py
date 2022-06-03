ac = 0.0601
ap = 0.0305
av = -0.0244
edad = int(input('Ingrese edad: '))
peso = int(input('Ingrese peso: '))

if edad >= 5 and edad <= 10:
    if peso < 16:
        estado = "A"
        peso_objetivo = 22
    elif peso > 28:
        estado = "B"
        peso_objetivo = 24
    else:
        estado = "C"
        peso_objetivo = 28
elif edad > 10 and edad <= 13:
    if peso < 30:
        estado = "A"
        peso_objetivo = 32
    elif peso > 50:
        estado = "B"
        peso_objetivo = 43
    else:
        estado = "C"
        peso_objetivo = 50
elif edad > 13 and edad <= 17:
    if peso < 51:
        estado = "A"
        peso_objetivo = 56
    elif peso > 63:
        estado = "B"
        peso_objetivo = 58
    else:
        estado = "C"
        peso_objetivo = 63
if estado == "A":
    pc = 2
    pp = 1
    pv = 2
    para = "un peso saludable"
elif estado == "B":
    pc = 0.6
    pp = 1
    pv = 4
    para = "un peso saludable"
else:
    pc = 0.5
    pp = 0.7
    pv = 2
    para = "el peso maximo"
aporte_dia = (ac*pc) + (ap*pp) + (av*pv)
dias = 0

if peso > peso_objetivo:
  while peso != peso_objetivo:
      dias = dias + 1
      peso = (peso+aporte_dia)
      if peso < peso_objetivo:
          peso = int(peso)
          break
else:
  while peso != peso_objetivo:
      dias = dias + 1
      peso = (peso+aporte_dia)
      if peso > peso_objetivo:
          peso = int(peso)
          break


print(f'El estado nutricional del paciente es {estado} y se requieren {dias} dias de dieta para que alcance {para}')