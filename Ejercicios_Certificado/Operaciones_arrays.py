# Supongamos que queremos obtener la suma de los elemnentos numéricos de dos arreglos:

#Por ejemplo si queremos tener la suma de un arreglo como este:
arreglo1 = [1,2,3]

#Sería simplemente sumar los tres elementos para obtener un valor igual a 6, 
#sin emabrago, en un arreglo donde seguramente tenedremos muchos más elmentos, necesitaremos la ayuda del loop for así:

#Se inicializa la suma:
s=0
#Creamos el for para iterar con la suma de cada término
for suma1 in arreglo1:
    s=suma1+s
#Mostramos el resultado obtenido
print(s)

