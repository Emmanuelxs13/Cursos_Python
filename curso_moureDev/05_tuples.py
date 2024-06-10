#  Tuplas
# Las tuplas son  una estructura de datos en Python que nos permiten almacenar varios valores en un solo dato. 

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (19, 1.74, "Emmanuel", "Berrio")
my_other_tuple = (35, 24, 62, 52, 30, 30, 17)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])

print(my_tuple.count(19))

# .index sirve para  encontrar la posicion de un elemento en una tupla 
print(my_tuple.index("Emmanuel"))

print(my_tuple.index("Berrio"))

# my_tuple[1] = 1.80  no se puede porque las tuplas son inmutables
my_sum_tuple = my_tuple + my_other_tuple

print(my_sum_tuple[3:6])

list(my_tuple)
print(type(my_tuple))

my_tuple[2] = "Jimenez"
my_tuple.insert(1, 'Azul')
my_tuple = tuple(my_tuple)
print(my_tuple)

del my_tuple
# print(my_tuple)  # No existe