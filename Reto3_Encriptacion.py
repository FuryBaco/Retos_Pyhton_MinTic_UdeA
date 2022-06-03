from random import shuffle
import numpy as np

texto = 'Today is Caturday!'

def encriptado(texto):
    lista_texto = [char for char in texto]
    t_matriz =(int(len(texto)**(1/2)) + ((len(texto)**(1/2)%1!=0)))
    while len(lista_texto) < (t_matriz**2):
        lista_texto.append('_')
    lista_clave = list(range(len(lista_texto)))
    l_combinada = list(zip(lista_texto,lista_clave))
    shuffle(l_combinada)
    lista_encriptada, clave = zip(*l_combinada)
    matriz_encriptado=np.array(lista_encriptada).reshape(t_matriz,t_matriz)
    
    return matriz_encriptado, clave
    
retorno = encriptado(texto)

def desencriptado(matriz_encriptado, clave):
    l_des = matriz_encriptado.flatten().tolist()
    l_mensaje = list(range(len(l_des)))
    idx = 0
    for num in clave:
      l_mensaje[num] = l_des[idx]
      idx +=1
    l_mensaje = filter(lambda char: char != '_', l_mensaje)
    mensaje = ''.join(l_mensaje)
      
    return mensaje

print(desencriptado(retorno[0], retorno[1]))
    