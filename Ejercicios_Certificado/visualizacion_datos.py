#VISUALIZANDO DATOS

"Seguramente ya ha utilizado visualizaciones de datos en muchas ocasiones y formas diferentes."
" Es así cómo se pueden usar los datos para explicar, pero también ofuscar, ciertas tendencias y verdades."
" Al jugar con las variables, escalas y demás, se puede generar ideas, imágenes muy diferente de los mismos datos."

#En primer lugar, hay gráficos univariados, que se definen como gráficos que pertenecen a una sola variable.
# Para esto usaremos un módulo muy popular en python para hacer gráficos llamado matplotlib

import matplotlib.pyplot as plt
# Se asigna a una varible el métodos 'figure' para crear una figura:
fig = plt.figure()
# a la figura se le añaden las caracteristicas delos ejes [xmin, ymin, dx, dy] 
ax = fig.add_axes([0,0,1,1])
# Entregamos los datos de cada eje a ser graficado:
productos = ['Aceite', 'Mantequilla', 'Huevos', 'Leche', 'Harina']
clientes = [32,15,33,27,14]
#Solicitamos al método bar el armado de los puntos
ax.bar(productos,clientes)
#Se muestra la gráfica
plt.show()

"Una gráfica como esta, fácilmente nos puede dar idea del comportamiento de los datos"
"Al igual que podemos observar en un gráfico tipo histograma:"

import numpy as np
fig,ax = plt.subplots(1,1)
cantidad = np.array([22,87,7,43,53,73,55,54,11,22,51,5,81,31,22])
ax.hist(cantidad, bins = [0,25,50,75,100])
ax.set_title("histograma")
ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('dias')
ax.set_ylabel('cantidades')
plt.show()

"Ahora una distribución visual tipo circular, usando el método 'pie', "
"tendremos una gráfica con porcentajes que pueden dar mucha información relevante:"

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
productos = ['Aceite', 'Mantequilla', 'Huevos', 'Leche', 'Harina']
clientes = [32,15,33,27,14]
ax.pie(clientes, labels = productos,autopct='%1.2f%%')
plt.show()

#GRAFICAS DE PUNTOS
#Las gráficas de puntos suelen ser poco apreciadas, sin emabrago pueden entregar información visual muy interesante,
# como las distribuciones de consumo de ciertos productos, ejemplo:

cantidades_mujer = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
cantidades_hombre = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
ID_articulo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fig=plt.figure()
ax=fig.add_axes([1,0,1,1])
ax.scatter(ID_articulo, cantidades_mujer, color='r')
ax.scatter(ID_articulo, cantidades_hombre, color='b')
ax.set_xlabel('ID de artículo')
ax.set_ylabel('Cantidades consumo')
ax.set_title('Gráfica de puntos, Rojo: mujer, Azul:hombre')
plt.show()

#GRAFICAS DE CAJA
"Un diagrama de caja, también conocido como diagrama de bigotes, muestra un resumen de un conjunto de datos"
" que contiene el mínimo, el primer cuartil, la mediana, el tercer cuartil y el máximo. En un diagrama de caja, "
" dibujamos una caja desde el primer cuartil hasta el tercer cuartil. Una línea vertical atraviesa la caja en la mediana."
" Los bigotes van desde cada cuartil hasta el mínimo o el máximo. Veamos:"

# Generemos algunos datos aleatorios:
np.random.seed(10)
d_1 = np.random.normal(50, 25, 300)
d_2 = np.random.normal(70, 20, 300)
d_3 = np.random.normal(90, 30, 300)
d_4 = np.random.normal(100, 10, 300)
data =(d_1,d_2,d_3,d_4)

#Ahora graficamos los datos creados:
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
bp = ax.boxplot(data)
plt.show()