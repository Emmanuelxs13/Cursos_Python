#La estadística es un "universo" de conocimiento tan basto que está fuera del alcance de deste curso, sin embargo,
#existen conceptos básicos que ayudarán a iniciarse en este interesante tema:

#Veamos las medidas más importantes que pueden resumir las variables:
#Una vez que haya recopilado un conjunto de datos, lo siguiente es ver con qué está tratando.
#¿Qué podemos aprender de las variables antes de comenzar a modelarlas?
#Hay un par de enfoques que puede utilizar para responder a esta pregunta. En particular, muchas personas se sienten atraídas por las gráficas pero primero, veremos lo básico de estadística para la analítica.
#Queremos tener una idea de la distribución de valores y otras particularidades, como los valores atípicos.

#Importemos nuestros módulos primero:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.datasets as dsets
a = [1,3,5,7,9,11,13]
b = [2,4,6,8,10,12,15]

# Importamos un dataset disponible en scikit learn:
dataset = dsets.load_wine()

# Aunque no siempre está disponible, podemos obtener la descripción que nos dará información útil:
print(dataset['DESCR'])

# Ahora podemos crear un dataframe para las variables independientes, en este caso 'data' y 'feature_names' :
wine_data = pd.DataFrame(data=dataset['data'],columns=dataset['feature_names'])

# Y ahora un dataframe para la variable dependiente, que en este caso es 'target':
wine_classes = pd.DataFrame(data=dataset['target'],columns=['target'])

#¿Puede usted observar de qué se trata este set de datos?
# Tenga en cuenta que en condiciones normales, usted ya debe estar familiarizado con los datos a analizar.

#Veamos si puede responder a lo siguiente:

#1. ¿Cuántos atributos tiene el dataset?

atributos = input("INGRESE EL NÚMERO DE ATRIBUTOS DEL DATASET")
print(type(atributos))
c = a[1]+b[4]
if isinstance(atributos, str)==False:
    atributos = await (atributos)

assert atributos == str(c), "Incorrecto, Ejecute nuevamente desde la celda anterior"
print("Correcto, el número de atributos del dataset es: ",atributos)

#2. ¿Cuántas clases tiene el dataset?

clases = input("INGRESE EL NÚMERO DE CLASES DEL DATASET")
if isinstance(clases, str)==False:
    clases = await (clases)

assert clases == str(len(wine_classes)), "Incorrecto, Ejecute nuevamente desde la celda anterior"
print("Correcto, el número de atributos del dataset es: ",clases)

#CALCULO DE LA MEDIA:
"La media muestra la tendencia general que está presente en un conjunto de puntos de datos numéricos"
"Si su conjunto de datos tiene tamaño , entonces calculamos la media como la suma de los datos, dividido entre la cantidad de datos."
"Numpy nos permite realizar esta tarea de forma sencilla:"

# 'mean' es el método que nos permite calcular la media, así, si quieremos
# calcular la media de la intensidad de color presente en nuestro dataset:

mean = np.mean(wine_data['color_intensity'])
#Podemos redondear nuestro reultado con la cantidad de decimales deseados usando el método 'round':
print('Media: '+str(round(mean,2)))

#CALCULO DE LA MEDIANA
#La mediana es unA estadística de posición central que parte la distribución en dos, es decir, 
#deja la misma cantidad de valores a un lado que a otro. 
#Para calcular la mediana es importante que los datos estén ordenados de mayor a menor, o vieversa.

# 'median' es el método que nos permite calcular la mediana.
"Es la observación intermedia del conjunto de datos"
" Por ejemplo, el 50% de todos los datos tiene un valor inferior y el 50% de los datos tiene un valor superior a la mediana cuando decimos que la mediana,"
" es el valor del cuantil 50%. También podemos calcular el cuantil 25% y 75% respectivamente, por ejemplo, donde el 25% (75%) de los datos tienen un valor inferior,"
" y el 75% (25%) tiene un valor superior a esa estadística. El percentil del 25 % (75 %) se calcula como la mediana de la parte inferior (superior) del conjunto de datos en caso de que sea uniforme,"
" y la mediana de la parte inferior (superior) incluida la mediana en caso de que sea desigual."
"Para lo cual numpy también nos permite realizarlo demanera sencilla:"

median = np.median(wine_data['color_intensity'])
print('Mediana: '+str(round(median,2)))

#CÁLCULO DE LA DESVIACIÓN ESTANDAR
# La desviación es la separación que existe entre un valor cualquiera de la serie y la media.

"La desviación estándar, es una medida que ofrece información sobre la dispersión media de una variable (separación)."
" La desviación estándar es siempre mayor o igual que cero."
" Para lo cual numpy también nos permite realizarlo demanera sencilla:"

std = np.std(wine_data['color_intensity'])
print('Desviación std: '+str(round(std,2)))

#Tambien existe una forma de obtener una descripción estadística de nuestros datos a nivel general
# Se puede usar para una o varias variables:

"Para una variables:"
print(wine_data['color_intensity'].describe())

"Para múltiples variables:"
print(wine_data.describe())
