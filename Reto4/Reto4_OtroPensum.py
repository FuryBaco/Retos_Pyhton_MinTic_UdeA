pensum = [

        {"0123": {"nombre": "intro a la ing", "creditos": 2},

        "4567": {"nombre": "ingles", "creditos": 1}},

        {}, {}

     ]

def es_semestre_valido(pensum, semestre):
  semestre = semestre - 1
  if semestre < 0 or (semestre) >= (len(pensum)):
    return False
  return True

def es_semestre_vacio(pensum,semestre): 
  semestre = semestre - 1
  if pensum[semestre] == {}:
    return True
  return False

def es_materia_valida(pensum, semestre, materia):
  semestre = semestre - 1
  if not materia in pensum[semestre]:
    return False
  return True

def modificar_materia(pensum, semestre, materia, nombre, creditos):
  
  if es_semestre_valido(pensum, semestre) and es_semestre_vacio(pensum,semestre) and es_materia_valida(pensum, semestre, materia):
    semestre = semestre - 1
    pensum[semestre][materia]['nombre'] = nombre
    pensum[semestre][materia]['créditos'] = creditos

def eliminar_materia(pensum, semestre, materia):
  
  if es_semestre_valido(pensum, semestre) and es_semestre_vacio(pensum,semestre) and es_materia_valida(pensum, semestre, materia):
    semestre = semestre - 1
    del pensum[semestre][materia]
        
modificar_materia(pensum, -1, '0123','AI', 4)
print(pensum)