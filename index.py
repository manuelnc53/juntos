import pandas as pd

csv_cultos = pd.read_csv('./datasets/registro-nacional-cultos.csv')

nombre_provincia="San Juan"


## Iglesias por ciudad
provincia_cultos = csv_cultos[csv_cultos.provincia==nombre_provincia].sort_values(by=['ciudad','nombre']).reset_index().drop(['index'], axis=1)
provincia_cultos.to_csv("./resultados/"+nombre_provincia+"_iglesias.csv")

## Ciudades en donde hay iglesias
ciudades_con_iglesia = provincia_cultos['ciudad'].str.upper().drop_duplicates().reset_index().drop(['index'], axis=1)
ciudades_con_iglesia.drop_duplicates().to_csv("./resultados/"+nombre_provincia+"_ciudades_con_iglesias.csv")


