#PERSPECTIVA VISUALIZANDO DATOS

"Supongamos que ahora queremos obtener algo de perspectiva de algunos datos."

#Ya sabemos como realizar algunas gráficas, veamos que información se puede obtener, inténtelo ud mismo:

#Tenemos los siguientes servicios en un determinado negocio:
# ['Asesorias, Acompañamiento, Diseños, Mediciones']

#Las veces que se ha reportado el uso de los servicios en el último año ha sido:
#[150,241,58,89]

# Y queremos intentar ver que nos puede decir del negocio una gráfica como las barras:

import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
# Entregamos los datos de cada eje a ser graficado:

servicios = ['Asesorias', 'Acompañamiento', 'Diseños', 'Mediciones']
usos = [150,241,58,89]

#Solicitamos al método bar el armado de los puntos
ax.bar(servicios,usos)
#Se muestra la gráfica
plt.show()

"Podemos decir que el servicio de acompañamiento, ha sido el más utilizado y el de diseños el menos utilizado."
" Sin embargo, no podemos afirmar que las utilidades de los acompañamientos sean mayores a los diseños"

# Si usamos la gráfica de barras con la siguiente información donde se nos indica el valor promedio de venta de una serie de articulos durante un año y luego la identificación del artículo
vr_md = [2618.68531411,2388.8833164,2376.61828509, 2493.28288939, 2482.6863909, 2618.00807557, 2564.67218461, 2630.97510584, 2411.60592363, 2601.18867417, 535.31928936,3001.83301633, 2546.90786323, 2321.59223762, 2528.40753807, 2368.19012295, 2551.30511975, 2564.31092771, 2506.69936216, 563.58077374]
articulo = [1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21]
# Use esta linea adicional para mejorar la visualización:
ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21])

"¿Puede decir que el artículo 13 es uno de los mejores promedios de venta del año?"

"Una gráfica de barras para los datos anteriores nos pueden mostrar fácilmente que el artículo 13 parece ser el de mejor promedio de venta."
"¿Y una gráfica circular nos podrá confirmar esta información del artículo 13? "

#Realice la gráfica circular correspondiente a los datos anteriores e intente verificar que información puede dar:

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
#Escriba aquí la línea que hace falta para visualizar la gráfica circular

plt.show()


"En definitiva es dificil decir que el artículo 13 es el de mejor promedio de venta en una gráfica circular."
" Pero esto es para el ejemplo en particular, ya que como podrá haber observado, se puede decir cuales artículos son los de menor promedio"

#En la próxima gráfica depuntos hay un pequeño error. 
# solucione el error para que pueda responder:
"¿Cuál es el artículo que más consumen hombres y mujeres respectivamente?"

cantidades_mujer = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
cantidades_hombre = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
ID_articulo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fig=plt.figure()
ax=fig.add_axes([1,0,1,1])
ax.scatter(ID_articulo, cantidades_mujer, color='r')
ax.scatter(ID_articulo, cantidades_hombre, color='b')
ax.set_xticks(ID_articulo)
ax.set_xlabel('ID de artículo')
ax.set_ylabel('Cantidades consumo')
ax.set_title('Gráfica de puntos, Rojo: mujer, Azul:hombre')
plt.show()

"Esta vez estuvo fácil. La gráfica muestra con claridad que para los hombres es el artículo 4 y para las mujeres,"
" es el artículo 7 el de mayor consumo"

# Y si quisiéramos graficar los cuartiles 25%,50% y 75%,solo de las cantidades de sonsumo para mujeres y para hombres sin importar el articulo,

"¿Qué debemos cambiar en el siguiente código para visualizarlos?"

#Datos a graficar
data =(cantidades_mujer,cantidades_mujer)

#Ahora graficamos los datos creados:
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
bp = ax.boxplot(data)
plt.show()


"Si fue cuidadoso con la información, habrá descubierto que se estaba graficando parte de la información dos veces y hacía falta uno de los sets de datos"

"HABRÁ CONCLUIDO QUE AUNQUE HAY MUCHAS FORMAS DE VISULIZAR LOS DATOS, ES IMPORTANTE TENER CUIDADO EN EL COMO HACERLO Y QUE NO EN TODOS LOS CASOS SIRVEN LOS MISMOS TIPOS DE GRAFICAS"