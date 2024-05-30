#REGRESION LINEAL

# Hasta ahora hemos visto como clasificar con varios ejemplos, ya que la clasificación suele ser un tema intuitivo por ser una de las d¡formas de decisión mas usadas por nosotros en casi cualquier ámbito.

#Sin embargo en analítica hay métodos importantes como la regresión Lineal. 
# La regresión lineal es una de las técnicas más usadas en Machine Learning. Su fortaleza estriba en su simplicidad e interpretabilidad.
# Básicamente es una técnica que permite predecir mediante la observación del pasado, para ello vamos directamente a algunas técnicas usadas en python:

# Importamos librerias necesarias:

import numpy as np #Librería numérica
import matplotlib.pyplot as plt # Para crear gráficos
#%matplotlib inline # gráficos dentro de un notebook
from sklearn.linear_model import LinearRegression #Regresión Lineal con scikit-learn una librería especializada

#Creamos una función para generar unos datos de forma aleatoria:
def f(x):  # función f(x) = 0.12*x + 1.25 + 0.2*Ruido_Gaussiano
    np.random.seed(42)
    y = 0.12*x + 1.25 + 0.2*np.random.randn(x.shape[0])
    return y

# generamos valores x de 0 a 20 en intervalos de 0.4:
x = np.arange(0, 20, 0.4)

# calculamos ejecutando la función que hemos generado antes:

y = f(x)

#Gráfico de los datos que hemos generado:
plt.scatter(x=x,y=y,label='data', color='blue')
plt.title('Datos');
plt.show()
