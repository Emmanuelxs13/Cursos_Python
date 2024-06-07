# En este ejercicio, intentaremos identificar datos atípicos, basados en datos de consumo, una relativa geografía de consumo y nivel salarial:

# Importamos las librerías necesarias:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

#Carguemos nuestros datos a evaluar:
dataset = pd.read_excel(r'E:\Drive\Drive\Pascual Bravo\MOOC analitica basica con python\Modulo 3\Saber 2\Data.xlsx',index_col=0)
print(dataset.head())

# Vamos a remover variables que se consideren innecesarias en el ejercicio:
# Para este caso, las categorías de producto y su identificación, no se consideran pertinentes:

#Primero creamos un array que nos permita almacenar el nombre de las columnas que queremos eliminar
Remove = ['Product_Category_1','Product_Category_2', 'Product_Category_3', 'Product_ID']

#Removemos según lo deseado usando el método drop:
purchase_data = dataset.drop(Remove, axis=1)

# Ahora agrupamos la información de interés, en este caso agrupamos alrededor del usuario: 
purchase_data = purchase_data.groupby( ['User_ID', 'Gender', 'Age', 'Occupation', 'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status']).sum()

#Agregamos una columna resultado:
purchase_data = purchase_data.add_suffix('_Sum').reset_index()

# Ahora vamos a hacer uso de otr fuente de datos relacionada para nuestro ejercicio
customer_data = pd.read_excel(r'E:\Drive\Drive\Pascual Bravo\MOOC analitica basica con python\Modulo 3\Saber 2\Data2.xlsx',index_col=0)

#unimos los dos dataset que tenemos para hacer más robusto nuestro insumo:

#hacemos una copia de nnuestro útimo dataset para realizar
final_data = purchase_data.copy()  

#Ahora unimos los datos para evaluarlos de forma conjunta:
final_data = pd.merge(final_data, customer_data, on='User_ID', how='left')

#Veamos que tipos de datos tenemos:
print(final_data.dtypes)

# Si todo va bien, podemos realizar algunas gráfica que nos pueden dar idea del comportamiento de nuestros datos:

for var in final_data.columns:
    if var in final_data.select_dtypes(include=['float64', 'float32', 'int64', 'int32', 'object']):
        plt.hist(final_data[var].fillna(0))
    else:
        plt.bar(x = final_data[var].unique(), height = final_data[var].value_counts())
    plt.title(var)
    plt.show()

# Como se puede observar, obtuvimos un error de incompatibilidad de algunas variables.
# Observando el dataset, encontramos que la columna 'Stay_In_Current_City_Years', hay valores que deben ser reemplazados:
final_data = final_data.replace(str('4+'),4)


for var in final_data.columns:
    if var in final_data.select_dtypes(include=['float64', 'float32', 'int64', 'int32', 'object']):
        plt.hist(final_data[var].fillna(0))
    else:
        plt.bar(x = final_data[var].unique(), height = final_data[var].value_counts())
    plt.title(var)
    plt.show()

#Sigamos haciendo depuración de datos:

#Podemos retirar el 'User_ID', ya que no nos está entregando información relevante:
fixed_id_data = final_data.drop(['User_ID'], axis=1)
#Mostramos como va el dataset
print(final_data.head())

# veamos las variables categíricas y transformémoslas:

#Creamos una copia para evitar un mal uso:
transformed_data = fixed_id_data.copy()

#Definimos las que queremos transformar:
to_transform = ['Age', 'Gender', 'City_Category', 'Stay_In_Current_City_Years']

#Aplicamos la transformación:
for var in to_transform:
    transformed_data = pd.concat([transformed_data.drop(var, axis=1), pd.get_dummies(transformed_data[var].values, prefix=var, drop_first=True)], axis=1)

#Veamos como van nuestros datos:
transformed_data

# La columna 'proximity_town', tiene valores vaciós, por lo que es necesario hacer algo.
# en nuestro caso optaremos por sacara ma media de la columna y reemplazar.

#Primero sacamos la media:
mean = np.nanmean(transformed_data['proximity_town'])
print(mean)

#Ahora realizamos el reemplazo correspondiente
transformed_data['proximity_town'] = transformed_data['proximity_town'].fillna(mean)

#Veamos como van nuestros datos:
transformed_data

# Ahora busquemos datos atípicos (outliers)

#Creamos una copia de los datos:
marked_outliers = transformed_data.copy()

#Definimos en una variable los parámetros para determinar los datos atípicos:
loc= LocalOutlierFactor(n_neighbors = 20, contamination = 0.1)

#Realizamos la identificación:
outliers_loc = loc.fit_predict(marked_outliers)

#Agregamos los datos a nuestro dataset:
marked_outliers['outlier'] = pd.DataFrame(outliers_loc)

#Veamos como va el dataset:
marked_outliers

#Ahora, antes de sacar conclusiones, debemos normalizar algunos de los datos

#Creamos un array para determinar lo que queremos normalizar
to_normalise = ['annual_income', 'proximity_town', 'Occupation', 'Purchase_Sum', 'number_of_children']  

#Creamos una copia de los datos
normalised_data = marked_outliers.copy()

#Definimos una normalización estándar
ss = StandardScaler()

#Realizamos la normalización:
norm_data = ss.fit_transform(normalised_data[to_normalise].values)

#Organizamos el dataset
normalised_data[to_normalise] = norm_data

#VEamos como vamos:
normalised_data

#Finalmente ya con nuestros datos listos, podemos tratar de encontrar lo importante:

# Lo primero es alistar los datos para uan regresión lineal,
# teniendo en cuenta que nuestr avariable principal será 'Purchase_Sum':
lin_r = LinearRegression()
y = normalised_data[['Purchase_Sum']]

# Ahora si podemos realizar la predicción, iterando con nuestros datos y graficando:
for variable in ['proximity_town', 'annual_income']:
    x = normalised_data[[variable]]
    
    lin_r.fit(x, y)
    predictions = lin_r.predict(x)

    plt.title(variable)
    plt.scatter(x, y, color = 'blue')
    plt.scatter(x, predictions, color = 'red')
    plt.show()