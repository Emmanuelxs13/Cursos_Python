#CLASIFICACIÓN
#En aprendizaje automático y estadística, la clasificación estadística es el problema de identificar a cuál de un subconjunto de categorías pertenece una nueva observación, sobre la base de un conjunto de datos de formación que contiene observaciones cuya categoría de miembros es conocida. 
#Un ejemplo sería asignar a un correo electrónico dado la clasificación de "spam" o "no spam".

#Asumamos un dataset donde podemos ver el asunto de algunos correos y en los que queremos tratar de identificar si es un posible SPAM
dicc1={"correo1":"Hola amigo","correo2":"ganaste la loteria","correo3":"informe anual","correo4":"reclamo de herencia"}
#Podemos hacer un recorrido por nuestro conjunto de datos usando for:
for x in dicc1:
    #Condicionar algunas palabras clave para identificar en cuales correos puede ser catalogado como SPAM, por ejemplo las palabra 'loteria' o 'herencia'
    #Para ello hay distintas funciones al alcance de python, en este caso usaremos el método "count" que nos ayuda a identificar una cadena específica de caractéres:
    if dicc1[x].count("loteria")==True or dicc1[x].count("herencia")==True:
        print("SPAM", x)
#print (dicc1.count("loteria"))

#Cómo podemos ver, en estos ejemplos es relativamente simple realizar este tipo de clasificaciones. En ejemplo de datasets más grandes, será necesario el uso de técnicas más avanzadas que vermos más adelante.