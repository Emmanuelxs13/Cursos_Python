#  Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Emmanuel", "Apellido":"Berrio", "Edad":19, 1:"Python"}

my_dict = {
        "Nombre":"Emmanuel",
        "Apellido":"Berrio", 
        "Edad":19, 
        "Lenguajes":{"Python", "Swift", "Kotlin"},
        1:1.75
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict[1])

my_dict["Nombre"] = "Manuel"
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle Emmanuel"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Emmanuel" in my_dict) #Aqui dice false, porque estamos buscando por clave y no por valor
print("Apellido" in my_dict)

print(my_dict.items()) # .items sirve para que nos devuelva una tupla con las claves y los valores del diccion
print(my_dict.keys()) # .keys sirve para  obtener las claves de un diccionario
print(my_dict.values()) # . values sirve para retornar todos los valores
print(my_other_dict.fromkeys("Nombre", 1))

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict) # Crea un diccionario sin valores

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Berri")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))
