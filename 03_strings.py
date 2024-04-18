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