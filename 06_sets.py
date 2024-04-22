#  Sets

my_set = set()

my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Emmanuel", "Berrio", 19}
print(type(my_other_set)) 

print(len(my_other_set))

my_other_set.add("Berri")

print(my_other_set) # Un set no es ina estructura ordenada

my_other_set.add("Berri") # Un set no admite repetidos

print(my_other_set)

# Sintaxis para comprobar que un elemento existe dentro de un set
print("Berrio" in  my_other_set) 
print("Berryo" in  my_other_set) 

my_other_set.remove("Berri")
print(my_other_set)

# Borra todos los elementos del conjunto 
my_other_set.clear()
print(len(my_other_set))

# Elimina por completo el set
del my_other_set
# print (my_other_set)

my_set = {"Emmanuel", "Berrio", 19}

my_list = list(my_set)

print(my_list[0])

my_other_set = {"kotlin", "Swift", "Python"}

#  .union sirve para  combinar dos sets y devuelve una nueva instancia de Set con la union de ambos conjuntos, sin eliminar ninguno de ellos
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

#  .difference sirve para  obtener la diferencia entre dos conjuntos, es decir aquellos elementos que existen en uno y no en otro
print(my_new_set.difference(my_set))
