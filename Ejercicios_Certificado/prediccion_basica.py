#Ya vamos teniendo idea de la regresión lineal, así que retomando lo que ya habíamos hecho:

import numpy as np #Librería numérica
import matplotlib.pyplot as plt # Para crear gráficos
#%matplotlib inline # gráficos dentro de un notebook
from sklearn.linear_model import LinearRegression #Regresión Lineal con scikit-learn una librería especializada

def f(x):  # función f(x) = 0.12*x + 1.25 + 0.2*Ruido_Gaussiano
    np.random.seed(42)
    y = 0.12*x + 1.25 + 0.2*np.random.randn(x.shape[0])
    return y

x = np.arange(0, 20, 0.4)
y = f(x)
plt.scatter(x=x,y=y,label='data', color='blue')
plt.title('Datos');
plt.show()

#Pasamos a conocer como se entrena de forma simple un modelo de regresión lineal:

#Para entrenar el modelo, hacemos uso de scikit-learn. 
#El método fit se encarga de ajustar los parámetros de regresión lineal a los datos:

# Importamos la clase de Regresión Lineal de scikit-learn
from sklearn.linear_model import LinearRegression

# creamos una instancia de LinearRegression
regresion_lineal = LinearRegression() 

# direccionamos a la regresión lineal para que aprenda de los datos (x,y)
regresion_lineal.fit(x.reshape(-1,1), y)

# mostramos los parámetros que ha estimado la regresión lineal
print('w = ' + str(regresion_lineal.coef_) + ', b = ' + str(regresion_lineal.intercept_))

#Teniendo en cuenta que el modelo es Y = wX+b, tenemos valores muy aproximados a los dados para obtener los valores aleatorios función f(x) = 0.12*x + 1.25 + 0.2*Ruido_Gaussiano
# En pocas palabras, realizamos un intento para devolvernos desde los valores hasta la función

# Ahora intentemos realizar una predicción con esta información:
#Con el modelo de regresión lineal entrenado, podemos hacer predicciones usando el método predict de la clase LinearRegression. 
#Por ejemplo, si quisiéramos saber qué valor de y corresponde para x, lo hacemos así:

# Usando un x = 3
nuevo_x = np.array([3]) 
prediccion = regresion_lineal.predict(nuevo_x.reshape(-1,1))
print(prediccion)

#El valor obtenido es la estimación de Y con el valor X propuesto.
# Imagine que sus datos son obtenidos de del consumo de un producto o servicio, en teoría y apudiera realizar una predicción de lo que se puede consumir un cliente con determinadas características.