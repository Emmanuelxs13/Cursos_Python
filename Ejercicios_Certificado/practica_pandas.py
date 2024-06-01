# PANDAS

"Usada para la manipulación de marcos de datos (dataframe) y analizar datos"

import pandas as pd

data = {
  "ID_producto": [1421, 1230, 9080],
  "ventas": [500, 40, 4550]
}

df = pd.DataFrame(data)

print(df) 

data = {
  "ID_producto": [1421,None, 9080],
  "ventas": [500, 40, 4550]
}

df = pd.DataFrame(data)

print(df) 

df.dropna(inplace = True)

print(df) 

data = {
  "ID_producto": [1421,None, 9080],
  "ventas": [500, 40, 4550]
}

df = pd.DataFrame(data)

print(df) 

df.fillna(130, inplace = True)

print(df) 