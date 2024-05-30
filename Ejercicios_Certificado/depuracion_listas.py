#En cualquier modelo, siempre es útil identificar valores duplicados, ya sea para encontrar una tendendcia o para eliminarlos y 
# evitar ruido en el análisis que se esté dando.

#Así es importante tener en cuenta  que una lista de valores de cualquier tipo puede ser fácilmente 'depurada' para su tratamiento, ejemplo:

# Declaramos nuestra lista
lista = [10, 20, 10, 30, 40, 20]
print(lista)

# usamos el método list dict.fromkeys, para eliminar los valores que se presentan más de una vez
lista_depurada = list(dict.fromkeys(lista))
print(lista_depurada)

# Ahora inténtelo ud mismo.
# Suponga que tiene la siguiente lista y quiere depurar para eliminar los valores que aparecen más de una vez.
# ["peras", "bananas", "manzanas", "bananas", "uvas", "manzanas"]

#Debe obtener el siguiente resultado:
# ['peras', 'bananas', 'manzanas', 'uvas']
lista2 = ["peras", "bananas", "manzanas", "bananas", "uvas", "manzanas"]
lista_depurada2 = list(dict.fromkeys(lista2))

print(lista_depurada2)
