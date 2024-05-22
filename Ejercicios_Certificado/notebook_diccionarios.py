#SI BIEN EN ANALITICA NOS PODEMOS ENCONTRAR CON CUALQUIER TIPO DE ESTRUCTURA DE DATOS (DATA FRAME), CONOCER Y ENTENDER LOS
#DICCIONARIOS, PROVEE ELEMENTOS DE GRAN IMPORTANCIA EN EL USO DE PYTHON CON LA ANALÍTICA.

#Los diccionarios en Python nos permiten almacenar una serie de 'mapeos' entre dos conjuntos de elementos, llamados keys and values 
# (Claves y Valores). Todos los elementos en el diccionario se encuentran encerrados en un par de corchetes 

#Asumamos que tenemos una lista e personas con sus edades, la podemos declarar así:
dicc = {"Ana": 20,"Bruno": 14,"Cata": 19,"Dani": 7,"Esteban": 12,"Fede": 5}

#La visualizamos en consola así:
print(dicc)

#Si queremos ver el valor de uno de los items usamos []:
print(dicc["Cata"])

#Si queremos saber el númeero de items del diccionario usamos 'len':
print(len(dicc))

#En este putno es importante recordar que python permite distintos tipos de arreglos (También llamados colecciones) ,
#  y con todos trabaja de forma distinta:
# 'Lista' es un arreglo ordenado mutable y permite duplicados.
# 'Tupla' es un arreglo ordenado inmutable y permite duplicados.
# 'Set' es un arreglo no ordenado, no indexado y no permite duplicados.
# 'Diccionario'es un arreglo ordenado inmutable y no permite duplicados.

#EJEMPLO DE LISTA:
#Las listas se usan para guardar items multiples en una sola variable:
lista = ["pera", "banana", "fresa"]
print(lista)

#EJEMPLO DE TUPLA:
#Las tuplas se usan para guardar items multiples en una sola variable. La diferencia con las listas es que a la tupla no se puede cambiar, agregar o cambiar items:
tupla = ("fresas", "uvas", "mangos")
print(tupla)

#EJEMPLO SET
#Los sets se usan para guardar items multiples en una sola variable, sin embargo, auque son inmutables, se puede agregar y quitar items:
set = {"naranja", "pera", "uchuva"}
print(set)

#Vamos a intentar varias accciones con los diccionarios mientras lo intenta usted mismo:
#nuestro diccionario contiene claves y valores que hacen referencia a nombres y edades {'Ana': 20, 'Bruno': 14, 'Cata': 19, 'Dani': 7, 'Esteban': 12, 'Fede': 5}

new_dic = {'Ana': 20, 'Bruno': 14, 'Cata': 19, 'Dani': 7, 'Esteban': 12, 'Fede': 5}

#Para acceder al valor de una de las claves, basta con asignarlo a una variable o simplemente pedirlo en consola con print. Por ejemplo, si nuestro diccionario se llama 'diccionario', para pedir el valor de cualquier clave:
# diccionario["clave1"], así:
diccionario ={"clave1": 44,"clave2":88}
print(diccionario["clave1"])

# Ahora inténtelo usted mismo con nuestro diccionario original de este notebook, solicite el valor de la clave "Bruno", 
# donde deberá obtener el número 14, adelante.
print(new_dic["Bruno"])

#Para cambiar el valor de alguna de las claves, basta con llamar la clave y asignarle el nuevo valor así:
diccionario["clave1"] = 77
print(diccionario["clave1"])

# Ahora inténtelo usted mismo con nuestro diccionario original de este notebook, cambie el valor de la clave "Bruno" por el valor 45, adelante.
new_dic["Bruno"] = 45
print(new_dic["Bruno"])

#Para adicionar una clave con valor a nuestro diccionario, solo basta con declar la nueva clave con su valor, así el diccionario quedará con una clave y valor nuevos. así:
diccionario["clave3"]=33
print(diccionario)

# Ahora inténtelo usted mismo con nuestro diccionario original de este notebook, agregue una nueva clave de nombre "Pepe" con un valor de 23, adelante.
new_dic["Pepe"] = 23

#Para remover un item a nuestro diccionario, se puede usar el método del indicando la clave, así el diccionario quedará sin el item indicado, así:
del diccionario["clave3"]
print(diccionario)

# Ahora inténtelo usted mismo con nuestro diccionario original de este notebook, remueva el item de clave "Pepe", debe obtener el diccionario así: {'Ana': 20, 'Bruno': 14, 'Cata': 19, 'Dani': 7, 'Esteban': 12, 'Fede': 5}, adelante.
del new_dic["Pepe"]
print(new_dic)

#Para recorrer un diccionario, se puede usar el loop for, así se obtienen los item de forma separada según la configuración del loop, para obtener las claves, así:
for x in diccionario:
  print(x)

#Para obtener los valores así:
for x in diccionario:
  print(diccionario[x])

#Para obtener claves y valores al mismo tiempo:
for x in diccionario:
  print(x,diccionario[x])

  # Ahora inténtelo usted mismo con nuestro diccionario original de este notebook, recorra el diccionario, pidiendo claves, valores y luego ambos. 
#   Su resultado debe ser así:

## CLAVES:
#Ana
#Bruno
#Cata
#Dani
#Esteban
#Fede

## VALORES:
#20
#14
#19
#7
#12
#5

## AMBOS:
#Ana 20
#Bruno 14
#Cata 19
#Dani 7
#Esteban 12
#Fede 5

dic_ejercicio = {"Ana":20, "Bruno":14, "Cata":19, "Dani":7, "Esteban":12, "Fede":5}

#Puede anidar diccionarios de la siguiente manera, lo que puede llegar a ser muy útil para crear y entender 'sets de datos' extensos:
diccionario_anidado ={"diccionario1":{"clave_d1-1":"val1-1","clave_d1-2":24},"diccionario2":{"clave_d2-1":"val2-1","clave_d2-2":31}}
print(diccionario_anidado)

# Ahora inténtelo usted mismo con nuestro diccionario original y el de los ejemplos (dicc y diccionario), el resultado del diccionario anidado debe ser:
# (Haga uso completo de lo indicado en el ejemplo para obtener el resultado esperado)
#{'dicc': {'Ana': 20, 'Bruno': 14, 'Cata': 19, 'Dani': 7, 'Esteban': 12, 'Fede': 5}, 'diccionario': {'clave1': 44, 'clave2': 88}}

