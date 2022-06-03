lista_texto=[]
with open("D:\MinTic\Programacion C1\Ejercicios-Python\Retos\Reto4\LoTR.txt", "r", encoding="utf8") as f:
    lista_texto = f.read().split()
# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN.
#RECUERDE QUE SU SOLUCIÓN DEBE REQUERIR DE POR LO MENOS OTRA
#FUNCIÓN MÁS APARTE DE LA FUNCIÓN main

def main(lista_texto):
    # ACÁ INICIA LA FUNCIÓN main
    pun = ['-','¿','?','.',',','¡','!',':','"','–']
    new_list = []
    for pal in lista_texto:
        for char in pal:
            if char in pun:
                pal = pal.replace(char,"")
        new_list.append(pal.lower()) 
    
    lista_conteo_p=[]
    for pal in new_list:
        conteo = new_list.count(pal)
        if not [pal, conteo] in lista_conteo_p:
            lista_conteo_p.append([pal, conteo])
    lista_conteo_p.sort(key=lambda name: name[1], reverse=True)
    lista_conteo = lista_conteo_p[:20]
    # ACÁ TERMINA LA FUNCIÓN main
    # NO MODIFICAR LA SIGUIENTE LÍNEA
    return lista_conteo

respuesta = main(lista_texto)
print(respuesta)