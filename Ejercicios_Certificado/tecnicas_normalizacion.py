"La normalización de la base de datos es el proceso de estructuración de una base de datos, generalmente una base de datos relacional, de acuerdo con una serie de las llamadas formas normales para reducir la redundancia de datos y mejorar la integridad de los datos."

#Importamos las librería necesarias
import pandas as pd 
import matplotlib.pyplot as plt


#Creamos un dataframe para ayudar en el ejercicio
df = pd.DataFrame([ 
                   [160000, 100, 28.7, 2400],  
                   [340000, 705, 24.7, 1500],  
                   [210000, 130, 16.5, 900],  
                   [58000, 250, 11.2, 2100]],  
    
                   columns=['A', 'B', 
                            'C', 'D']) 
#Mostramos el Dataframe
display(df)

# Grafiacmos nuestros datos:
df.plot(kind = 'bar')

"APLIQUEMOS ALGUNAS TÉCNICAS DE NORMALIZACIÓN:"

"La escala absoluta máxima:"
"Esta cambia la escala de cada característica entre -1 y 1 al dividir cada observación por su valor absoluto máximo."
"Podemos aplicarla usando los métodos .max() y .abs() de Pandas."

# Hacemos una copia del dataframe:
df_max_scaled = df.copy() 
 
#Para cada columna aplicamos la escala absoluta máxima:   
for column in df_max_scaled.columns: 
    df_max_scaled[column] = df_max_scaled[column]  / df_max_scaled[column].abs().max() 

#Mostramos el resultado:
display(df_max_scaled)

#Ahora, grafiquemos el como quedó el dataframe normalizado:
df_max_scaled.plot(kind = 'bar')

" La escala de función mínima-máxima:"
"Este cambia la escala de laa característicaa a un rango de [0,1] restando el valor mínimo de la característica y luego divide por el rango."
" Usando los métodos .min() y .max(). de Pandas, obtenemos:"

#Copiamos nuestro dataframe
df_min_max_scaled = df.copy() 

#Para cada columna aplicamos el método:
for column in df_min_max_scaled.columns: 
    df_min_max_scaled[column] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (df_min_max_scaled[column].max() - df_min_max_scaled[column].min())     

#Mostramos el resultado    
display(df_min_max_scaled)

# Ahora veamos:
df_min_max_scaled.plot(kind = 'bar')

"Método de puntuación z:"
"Este método transforma la información en distribución con una media de 0 y una desviación típica de 1."
"Cada valor estandarizado se calcula restando la media de la característica correspondiente y luego se divide por la desviación de calidad."

#copiamos nuestro dataframe
df_z_scaled = df.copy() 

#Se aplica el método con cada columna
for column in df_z_scaled.columns: 
    df_z_scaled[column] = (df_z_scaled[column] -
                           df_z_scaled[column].mean()) / df_z_scaled[column].std()     
#Mostrar el resultado  
display(df_z_scaled)

# Ahora veamos:
df_z_scaled.plot(kind = 'bar')

#Comparemos los 3 métodos:
df_max_scaled.plot(kind = 'bar')
df_min_max_scaled.plot(kind = 'bar')
df_z_scaled.plot(kind = 'bar')

