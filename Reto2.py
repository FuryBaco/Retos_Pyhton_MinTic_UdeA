
pensum = [{'0123': {'nombre': 'intro a la ing', 'créditos': 2}, '4567': {'nombre': 'inglés', 'créditos': 1}}, {}, {}]

# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

# NO MODIFICAR EL NOMBRE, PARÁMETROS O RETORNO DE LA FUNCIÓN

from calendar import c

def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN modificar_materia (En este espacio debes 
    # poner el código necesario para implementar esta funcionalidad)
    semestre = semestre - 1
    if not 0 <= semestre < len(pensum):
        mensaje_idx = 0
    elif pensum[semestre] == {}:
        mensaje_idx = 1
    elif not materia in pensum[semestre] :
        mensaje_idx = 2    
    else:
        pensum[semestre][materia]['nombre'] = str(nombre)
        pensum[semestre][materia]['créditos'] = int(creditos)
        mensaje_idx = 3  
    mensajes=["Ingrese un semestre válido","El semestre no tiene materias", "La materia no existe", "Modificada con éxito"]
    mensaje = mensajes[mensaje_idx]
    
    # ACÁ TERMINA LA FUNCIÓN modificar_materia
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return mensaje

resultado = modificar_materia(pensum, 1, '0123', 'IA', 5)
print(pensum)
print(resultado)

