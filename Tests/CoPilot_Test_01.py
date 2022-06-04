#Importar el archivo que esta en esta carpeta para ser convertido en un dataframe
import pandas as pd
import numpy as np

#Importar data.csv
data = pd.read_csv('data.csv')

#calcular el prmedio de la temperatura para la location 1

mean_temp_1 = data.loc[data['location'] == 1, 'temperature'].mean()
print("El promedio de la temperatura de la location 1 es: ", mean_temp_1)

