#  Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [36, 1.77, "Emmanuel", "Berrio"]

print(type(my_list))
print(type(my_other_list))

print("Mi edad:", my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(30))

age, height, name, surname = my_other_list
print(age)

print(my_list + my_other_list)


# .append sirve  para agregar un elemento al final de la lista
my_other_list.append("Jimenez")
print(my_other_list)

#  .insert sirve para  insertar un elemento en una posicion especifica de la lista
my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

#  .remove sirve para  eliminar un elemento de la lista
my_other_list.remove("Azul")
print(my_other_list)

#   .pop se utiliza para sacar el ultimo o el que esta en una posicion especificada
my_list.pop()
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

#  "del" sirve para  borrar una variable completa o en este caso un elemento de la lista
del my_list[2]
print(my_list)

# .copy  crea una copia exacta de la lista
my_new_list = my_list.copy()

# .clear  vacia completamente la lista 
my_list.clear()
print(my_list)
print(my_new_list)

# .reverse invierte los elementos de la lista
my_new_list.reverse()
print(my_new_list)

#  .sort ordena los elementos de la lista
my_new_list.sort()
print(my_new_list)

my_list = "Hola Python"
print(my_list)
print(type(my_list))