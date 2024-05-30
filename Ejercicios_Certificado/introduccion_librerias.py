# INTRODUCCIÓN A LIBRERIAS Y FUNCIONES

# Hay distintas metodologías que simplifican enormemente el uso de código en cualquier lenguaje de programación.

# Así, para el uso de ciertas herramientas están sijetas a uso de 'librerias. Este concepto hace referencia al conjunto de 
#implementos funcionales que ayudan a codificar todo este lenguaje de programación para crear una interfaz independiente y simplificar
#el uso con fines específicos.

# Por ejemplo, para realizar cáculos con tiempo, se puede hacer uso de la librería 'time', y para ello se llama siempre al principio del código asi:
import time 

# Aunque con esto ya es posible llamar las distintas funcionalidades de la librería, lo usual es darle una palabra clave que nos permita simplificar su uso, ejemlo:
import time as tm

# Asi para su uso, solo necesitamos necesitamos usar 'tm' en lugar de time:
print(tm.time())
tm.time()

#para este caso la expresión devuelve el tiempo desde que que está activo el compilador en uso

# Por otro lado existen las denominadas funciones, las que nos facilitan el uso recurrente de ciertas ejecuciones. 
# La estructura de las funciones comienza con la palagra def, seguido de un nombre que identifica la función para ser llamada a su ejecución:

def funcion():
    print("Hola")

#Como habrá notado, la función no devuelve nada en su construcción, para ello debe ser llamada a ajecución:

funcion()

#Las funciones también pueden recibir y entregar variables, lo que hace que sean de uso casi ilimitado:

#Construcción:
def funcion_01(varaible1,variable2):
    suma = varaible1 + variable2
    print(suma)

#Llamado a ejecución:
funcion_01(2,3)

# Ahora, para obtener cálculos mas complejos que pueden ser recurrentes se puede llamar las veces que se considere necesaria, sin importar que su ejecución interna sea compleja:

# Se declaran e inicializan las variables necesarias:
posicion=0
listado={}

#Construcción de la función con las variables a solicitar:

def funcion_02(nombre, edad, producto):
    #Se globalizan las variables para que sean mutables posteriormente:
    global posicion
    global listado
    #Se ejecuta lo que se desea con las variables:
    listado[posicion]={nombre:{edad:producto}}
    #Se muestra el resultado:
    print(listado)
    posicion = posicion + 1

#Se ejecuta la función:
funcion_02("Pepe Grillo", 30, "consciencia")

#Ahora que hemos obtenido un resultado , podemos solicitar uno o varios adicionales, veamos:
funcion_02("Pinocho ", 2, "aventura")
funcion_02("Gepetto",50,"paternidad")

# Note que podemos llamar los diccionarios creados para realizar lo que se considere necesario con ellos, así si queremos llamar unicamente el que corresponde a la posición 1 lo hacemos así:
print(listado[1])

# Para agregar el uso de librerías, un ejemplo sencillo con lo visto en este ejercicio puede ser calcular el tiempo que transcurre entre el comienzo de la ejecución de la función y el final de la ejecución así:

import time as ti

pos1=0
list1={}


def funcion_03(nombre, edad, producto):
    
    inicio = ti.time()
    #Se globalizan las variables para que sean mutables posteriormente:
    global pos1
    global list1
    #Se ejecutoa lo que se desea con las variables:
    list1[pos1]={nombre:{edad:producto}}
    #Se muestra el resultado:
    print(list1)
    pos1 = pos1 + 1
    fin = ti.time()
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:{0:.16f}".format(tiempo_transcurrido))

funcion_03("Lucas", 25, "cerveza")
funcion_03("Pedro", 35, "wisky")
funcion_03("Juan", 55, "vino")

