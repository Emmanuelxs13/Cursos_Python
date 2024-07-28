numeros = [1,2,3,4]
datos = [4, "Una cadena",-15,3.4,"otra cadena"]
datos[0]
datos[-1]

datos[-2:]

numeros + [5,6,7,8]

pares = [0,2,4,5,8,10]
pares[3] = 6

# Agregar al final con el append
pares.append(12)

pares.append(7*2)

letras = ['a','b','c','d','e','f']

letras[:3]

letras[:3] = ['A','B','C']

letras[:3] = []

letras = []

# Longitud
len(letras)
len(pares)

# Listas anidadas
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

r = [a,b,c]

r[1][1]