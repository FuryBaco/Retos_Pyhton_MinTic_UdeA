import json


def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    import pandas as pd
    from collections import Counter
    df = pd.read_csv (r'D:\MinTic\Programacion C1\Ejercicios-Python\Retos\Reto5\GLOBANT.csv')
    d = pd.DataFrame(df)
    da = pd.DataFrame()

    da['Fecha'] = d['Date']
    da['Comportamiento de la accion'] = d.apply(lambda n: 'SUBE' if n.Close - n.Open > 0  else 'BAJA' if n.Close - n.Open < 0 else 'ESTABLE', axis=1)
    da['Punto medio HIGH-LOW'] = (d['High'] - d['Low'])/2
    da.to_csv(r'D:\MinTic\Programacion C1\Ejercicios-Python\Retos\Reto5\analisis_archivo.csv', sep='\t', index=False)

    data_set = {"date_lowest_price": [], "lowest_price" : [],"date_highest_price" :[], "highest_price" :[], "cantidad_veces_sube" :[], "cantidad_veces_baja" : [], "cantidad_veces_estable" :[]}
    c = Counter(list(zip(da['Comportamiento de la accion'])))
    data_set["date_lowest_price"] = ''.join(list(d.loc[d['Low'] == d['Low'].min()]['Date']))
    data_set["lowest_price" ] = d['Low'].min()
    data_set["date_highest_price"] = ''.join(list(d.loc[d['High'] == d['High'].max()]['Date']))
    data_set["highest_price" ] = d['High'].max()
    data_set["cantidad_veces_sube" ] = c['SUBE',]
    data_set["cantidad_veces_baja" ] = c['BAJA',]
    data_set["cantidad_veces_estable" ] = c['ESTABLE',]

    with open('D:\MinTic\Programacion C1\Ejercicios-Python\Retos\Reto5\detalles.json', 'w') as f:
      json.dump(data_set, f)


respuesta = solucion()


