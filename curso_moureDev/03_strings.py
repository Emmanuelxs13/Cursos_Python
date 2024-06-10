# Strings

my_string = "Mi string"
my_other_string = 'Mi string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \n con salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)

my_scape_string = "\\tEste es un string con tabulación"
print(my_scape_string)

# Formateo

name, surname, age = "Emmanuel", "Berrio", 19

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

# Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)

# División
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reverse_language  = language[::-1]
print(reverse_language)

# Funciones

# Primera letra Mayuscula
print(language.capitalize())

# Toda la cadena de texto en mayuscula
print(language.upper())

print(language.count('t')) # Cuenta las veces que aparece una letra o un carácter en una cadena

print(language.isnumeric()) # Devuelve True si todos los caracteres son numéricos, False en caso contrario

print(language.lower()) # Convierte todas las letras a minúsculas

print(language.upper().isupper() ) #Devuelve True si toda la cadena está en mayúscula, False en caso contrario

