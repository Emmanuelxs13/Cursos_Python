#Importemos nuestros módulos primero:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.datasets as dsets

#INVESTIGACIÓN DE INFORMACIÓN

'''Ahora suponga que estamos buscando uno de los atributos, cuya descripción estadística es:

count    4.420000e+02
mean    -8.045349e-16
std      4.761905e-02
min     -9.027530e-02
25%     -3.422907e-02
50%     -7.283766e-03
75%      3.124802e-02
max      1.705552e-01
Name: bmi, dtype: float64

'''

"Si todo va bien, ya se habrá  cuenta que en la descripción está el nombre del atributo que estamos buscando,"
" y si no va tan bien, podrá usar esta pista para identificar el dataset al cual hace referencia este atributo."

"Ahora que ya ha encontrado el dataset correcto le será facil aplicar la siguiente regresión lineal y graficar,"
" solo le bastará con reemplazar en las equis el nombre correcto para obtener la grafica correspondiente y los siguietnes valores:"

'''
Coefficients: 
 [938.23786125]
Mean squared error: 2548.07
Coefficient of determination: 0.47

'''


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

#Reemplace las equis por el dataser correcto, por ejemplo: d_X, d_y = datasets.load_boston(return_X_y=True)
# cargar el dataset:
d_X, d_y = datasets.XXXXXXXXXXXXXXXX(return_X_y=True)

# Usaremos solo una característica:
d_X = d_X[:, np.newaxis, 2]

# Dividimos el dataset entreenamiento/testeo (training/testing):
d_X_train = d_X[:-20]
d_X_test = d_X[-20:]

# Dividimos el target en entreenamiento/testeo (training/testing):
d_y_train = d_y[:-20]
d_y_test = d_y[-20:]

# Creamos el objeto para la regresión lineal:
regr = linear_model.LinearRegression()

# Entrenamos el modelo usando los sets de entrenamiento de las lineas anteriores:
regr.fit(d_X_train, d_y_train)

# Hacemos predicciones usando el set de testeo:
d_y_pred = regr.predict(d_X_test)

# Mostrar los coeficientes:
print("Coeficientes: \n", regr.coef_)
# Mostrar el error cuadrático medio
print("Error cuadratico medio: %.2f" % mean_squared_error(d_y_test, d_y_pred))
# Mostrar el coeficiente de determinación, donde 1 es una predicción perfecta:
print("Coeficiente de determinacion: %.2f" % r2_score(d_y_test, d_y_pred))

# Graficar resultados:
plt.scatter(d_X_test, d_y_test, color="black")
plt.plot(d_X_test, d_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
