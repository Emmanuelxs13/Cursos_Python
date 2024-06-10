#  Variables en Python

my_variable = "My string variable"
print(my_variable)

my_int_variable = 777
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_variable))

# Variables en una sola linea, aunque se pueda hacer no es una buena practica a la hora de codificar
name, last_name, alias, age = "Emmanuel", "Berrio", "berrio", 19
print("Me llamo:",name, last_name,"Mi edad es:", age, "Y mi alias es:", alias)

# Inputs

"""name = input("Ingrese su nombre: ")
age = input("¿Cuantos años tienes? ")

print("Tu nombre es:",name) 
print("Tu edad es: ",age)"""

# Cambiamos su tipo
name = 25
age = "Emmanuel"

print(name)
print(age)

#  Forzamos el tipo
address: str = "Mi dirección"
print(address)