# CLASIFICACIÓN
# En aprendizaje automático y estadística, la clasificación estadística es el problema de identificar a cuál de un subconjunto de categorías pertenece una nueva observación, sobre la base de un conjunto de datos de formación que contiene observaciones cuya categoría de miembros es conocida.
# Un ejemplo sería asignar a un correo electrónico dado la clasificación de "spam" o "no spam".

# Asumamos un dataset donde podemos ver el asunto de algunos correos y en los que queremos tratar de identificar si es un posible SPAM
dicc1 = {"correo1": "Hola amigo", "correo2": "ganaste la loteria",
         "correo3": "informe anual", "correo4": "reclamo de herencia"}
# Podemos hacer un recorrido por nuestro conjunto de datos usando for:
for x in dicc1:
    # Condicionar algunas palabras clave para identificar en cuales correos puede ser catalogado como SPAM, por ejemplo las palabra 'loteria' o 'herencia'
    # Para ello hay distintas funciones al alcance de python, en este caso usaremos el método "count" que nos ayuda a identificar una cadena específica de caractéres:
    if dicc1[x].count("loteria") == True or dicc1[x].count("herencia") == True:
        print("SPAM", x)
# print (dicc1.count("loteria"))

# Cómo podemos ver, en estos ejemplos es relativamente simple realizar este tipo de clasificaciones.
# En ejemplo de datasets más grandes, será necesario el uso de técnicas más avanzadas que vermos más adelante.

# Ahora inténtelo ud mismo:
# Suponga que tiene un dataset que contiene edades de usuarios y productos o servicios consumidos, trate de realizar una clasificación básica,
# donde pueda obtener las edades de los usuarios del producto A:

dataset = {12: "juguete azul", 20: "camisa rayas", 40: "reloj lujo", 60: "viaje crucero", 10: "juguete azul", 18: "camisa rayas",
           35: "reloj lujo", 58: "viaje crucero", 13: "juguete azul", 27: "camisa rayas", 46: "reloj lujo", 65: "viaje crucero"}
print(dataset)

#Trate de identificar, como lo hicimos anteriormente, las edades correspondientes a:
#'juguete azul'
#'camisa rayas'
#'reloj lujo'
#'viaje crucero'

#Edad juguete azul: 12
#Edad juguete azul: 10
#Edad juguete azul: 13

#Edad camisa rayas: 20
#Edad camisa rayas: 18
#Edad camisa rayas: 27

#Edad reloj lujo: 40
#Edad reloj lujo: 35
#Edad reloj lujo: 46

#Edad viaje crucero: 60
#Edad viaje crucero: 58
#Edad viaje crucero: 65
# Crear diccionarios para agrupar las edades según el producto

juguete_azul = []
camisa_rayas = []
reloj_lujo = []
viaje_crucero = []

# Recorrer el dataset para clasificar las edades
for edad, producto in dataset.items():
    if producto == "juguete azul":
        juguete_azul.append(edad)
    elif producto == "camisa rayas":
        camisa_rayas.append(edad)
    elif producto == "reloj lujo":
        reloj_lujo.append(edad)
    elif producto == "viaje crucero":
        viaje_crucero.append(edad)

# Imprimir las edades correspondientes a cada producto
print("Edades de usuarios del producto 'juguete azul':")
for edad in juguete_azul:
    print(f"Edad juguete azul: {edad}")

print("\nEdades de usuarios del producto 'camisa rayas':")
for edad in camisa_rayas:
    print(f"Edad camisa rayas: {edad}")

print("\nEdades de usuarios del producto 'reloj lujo':")
for edad in reloj_lujo:
    print(f"Edad reloj lujo: {edad}")

print("\nEdades de usuarios del producto 'viaje crucero':")
for edad in viaje_crucero:
    print(f"Edad viaje crucero: {edad}")