lista_texto = ['Swiftly', 'now,', 'the', 'pursuers', 'turned', 'and', 'followed', 'the', 'new', 'path.', 'As', 'if', 'fresh', 'from', 'a', 'night’s', 'rest', 'they', 'sprang', 'from', 'stone', 'to', 'stone.', 'At', 'last', 'they', 'reached', 'the', 'crest', 'of', 'the', 'grey', 'hill,', 'and', 'a', 'sudden', 'breeze', 'blew', 'in', 'their', 'hair', 'and', 'stirred', 'their', 'cloaks:', 'the', 'chill', 'wind', 'of', 'dawn.', 'They', 'turned', 'and', 'walked', 'side', 'by', 'side', 'slowly', 'along', 'the', 'line', 'of', 'the', 'river.', 'Behind', 'them', 'the', 'light', 'grew', 'in', 'the', 'East.', 'As', 'they', 'walked', 'they', 'compared', 'notes,', 'talking', 'lightly', 'in', 'hobbit-fashion', 'of', 'the', 'things', 'that', 'had', 'happened', 'since', 'their', 'capture.', 'No', 'listener', 'would', 'have', 'guessed', 'from', 'their', 'words', 'that', 'they', 'had', 'suffered', 'cruelly,', 'and', 'been', 'in', 'dire', 'peril,', 'going', 'without', 'hope', 'towards', 'torment', 'and', 'death;', 'or', 'that', 'even', 'now,', 'as', 'they', 'knew', 'well,', 'they', 'had', 'little', 'chance', 'of', 'ever', 'finding', 'friend', 'or', 'safety', 'again.', '…in', 'the', 'Old', 'Entish', 'as', 'you', 'might', 'say.', 'It', 'is', 'a', 'lovely', 'language,', 'but', 'it', 'takes', 'a', 'very', 'long', 'time', 'to', 'say', 'anything', 'in', 'it,', 'because', 'we', 'do', 'not', 'say', 'anything', 'in', 'it,', 'unless', 'it', 'is', 'worth', 'taking', 'a', 'log', 'time', 'to', 'say,', 'and', 'to', 'listen', 'to', 'All', 'that', 'day', 'they', 'walked', 'about', 'in', 'the', 'woods', 'with', 'him,', 'singing,', 'and', 'laughing;', 'for', 'Quickbeam', 'often', 'laughed.', 'He', 'laughed', 'if', 'the', 'sun', 'came', 'out', 'from', 'behind', 'a', 'cloud,', 'he', 'laughed', 'if', 'they', 'came', 'upon', 'a', 'stream', 'or', 'spring:', 'then', 'he', 'stooped', 'and', 'splashed', 'his', 'feet', 'and', 'head', 'with', 'water;', 'he', 'laughed', 'sometimes', 'at', 'some', 'sound', 'or', 'whisper', 'in', 'the', 'trees.', 'Whenever', 'he', 'saw', 'a', 'rowan-tree', 'he', 'halted', 'a', 'while', 'with', 'his', 'arms', 'stretched', 'out,', 'and', 'sang,', 'and', 'swayed', 'as', 'he', 'sang.','','','','','','','','','','','','','','','',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#lista_texto=[]
#with open("LoTR.txt", "r", encoding="utf8") as f:
    #lista_texto = f.read().split()
# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN.
#RECUERDE QUE SU SOLUCIÓN DEBE REQUERIR DE POR LO MENOS OTRA
#FUNCIÓN MÁS APARTE DE LA FUNCIÓN main

def main(lista_texto):
    # ACÁ INICIA LA FUNCIÓN main
    from collections import Counter as ct
    pun = ['-','¿','?','.',',','¡','!',':','"','–',' ']
    new_list = [''.join(char.lower() for char in pal if char not in pun) for pal in lista_texto if pal]
    d_conteo= ct(filter(lambda pal: pal != '', new_list))
    lista_conteo_p = list(map(list, d_conteo.items()))
    lista_conteo = (sorted(lista_conteo_p, key=lambda pal: pal[1] , reverse=True))[:20]
    # ACÁ TERMINA LA FUNCIÓN main
    # NO MODIFICAR LA SIGUIENTE LÍNEA
    return lista_conteo

respuesta = main(lista_texto)
print(respuesta)
