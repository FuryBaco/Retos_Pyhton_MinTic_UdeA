grupo = [
{'cédula': '00014301503', 'nombre': 'Pepito', 'nota_fundamentos': 4.3},
{'cédula': '1037678471', 'nombre': 'Fulanito', 'nota_fundamentos': 3.2},
{'cédula': '71023567', 'nombre': 'Pancho', 'nota_fundamentos' : 5},
{'cédula': '32276123', 'nombre': 'Rita', 'nota_fundamentos' : 4.7},
{'cédula': '1036765245', 'nombre': 'Anita', 'nota_fundamentos' : 4.7},
{'cédula': '89122456', 'nombre': 'Pedrito' , 'nota_fundamentos': 4.7},
{'cédula': '289765345', 'nombre': 'Mat', 'nota_fundamentos' : 4.8},
{'cédula': '4576890', 'nombre': 'Dan', 'nota_fundamentos': 4.8}]

#nota_1ro = max(grupo, key=lambda x:x['nota_fundamentos'])
#print(nota_1ro)



def 𝑐𝑎𝑙𝑐𝑢𝑙𝑎𝑟_𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜_𝑦_𝑐𝑢𝑎𝑑𝑟𝑜_ℎ𝑜𝑛𝑜𝑟(𝑔𝑟𝑢𝑝𝑜:list):
    cuadro_honor_p = {1:[], 2:[],3:[]}
    notas= {i['nota_fundamentos'] for i in  grupo } 
    notas=list(sorted(notas))
    cuadro_honor_p[1]=[est['cédula'] for est in grupo if est['nota_fundamentos'] == notas[-1]]
    cuadro_honor_p[2]=[est['cédula'] for est in grupo if est['nota_fundamentos'] == notas[-2]]
    cuadro_honor_p[3]=[est['cédula'] for est in grupo if est['nota_fundamentos'] == notas[-3]]
    promedio = sum(nota['nota_fundamentos'] for nota in grupo)/len(grupo)
    return float(promedio),cuadro_honor_p

cuadro_honor = 𝑐𝑎𝑙𝑐𝑢𝑙𝑎𝑟_𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜_𝑦_𝑐𝑢𝑎𝑑𝑟𝑜_ℎ𝑜𝑛𝑜𝑟(𝑔𝑟𝑢𝑝𝑜)
print(cuadro_honor)

e=max(d['nota_fundamentos'] for d in grupo)
print(e)