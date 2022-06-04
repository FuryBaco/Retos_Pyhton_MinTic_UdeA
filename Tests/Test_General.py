import json
import pandas as pd
data = pd.read_csv(r'data.csv')
d_to_json = {}

def promedio(location):
    prom = list(data.loc[data['location'] == location][['temperature','pressure']].mean())
    return float('{0:.1f}'.format(prom[0])), float('{0:.1f}'.format(prom[1]))
locs = sorted(list(data['location'].unique()))
for location in locs:
    d_to_json[str(location)] = promedio(location)
with open('promedios.json', 'w') as f:
    json.dump(d_to_json, f)

data_nuevo = data
def above(cat, loct):
    return data_nuevo.apply(
    lambda n: 'SI' if n[loct] > d_to_json[str(n.location)][cat] else 'NO'
    if n[loct] < d_to_json[str(n.location)][cat] else 'IGUAL',
    axis=1)
data_nuevo['above_avg_temp'] = above(int(0), 'temperature')
data_nuevo['above_avg_pres'] = above(int(1), 'pressure')
data_nuevo.to_csv(r'data_nuevo.csv', index=False)
'''data_nuevo['above_avg_temp'] = data_nuevo.apply(
    lambda n: 'SI' if n.temperature > d_to_json[str(n.location)][0] else 'NO'
    if n.temperature < d_to_json[str(n.location)][0] else 'IGUAL',
    axis=1)
data_nuevo['above_avg_pres'] = data_nuevo.apply(
    lambda n: 'SI' if n.pressure > d_to_json[str(n.location)][1] else 'NO'
    if n.pressure < d_to_json[str(n.location)][1] else 'IGUAL',
    axis=1)'''




