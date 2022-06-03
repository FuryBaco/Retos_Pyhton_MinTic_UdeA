E1= {'cédula': '104689054', 'nombre': 'Valeria', 'nota_fundamentos': 5}

E2= {'cédula': '72877564', 'nombre': 'Cris', 'nota_fundamentos': 2.3}

E3= {'cédula': '34987567', 'nombre': 'Francis', 'nota_fundamentos': 3.7}

E4= {'cédula': '187654345', 'nombre': 'Johan', 'nota_fundamentos': 4.35}

E5= {'cédula': '187654348', 'nombre': 'Johan', 'nota_fundamentos': 4.35}

grupo= [E1, E2 ,E3, E4, E5]

def calcular_promedio_y_cuadro_honor(grupo) :
    #ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
        
    ntas = [] 
    for valor in (grupo):
        ntas.append(valor["nota_fundamentos"])
    promedio = float(sum(ntas) / len(grupo))
    notas = set(ntas)
    notas = list(sorted(notas))
    cuadro_honor={}
    cuadro_honor[1] = []
    cuadro_honor[2] = []
    cuadro_honor[3] = []
    for valor in grupo:
        if valor["nota_fundamentos"] == notas[-1]:
           cuadro_honor[1].append(valor["cédula"])
        if valor["nota_fundamentos"] == notas[-2]: #==-2 -3
            cuadro_honor[2].append(valor["cédula"])
        if valor["nota_fundamentos"] == notas[-3]: #2  2
            cuadro_honor[3].append(valor["cédula"])
    return promedio, cuadro_honor

print(calcular_promedio_y_cuadro_honor(grupo))