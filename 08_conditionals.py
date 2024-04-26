#  Condicionales

my_condition = True

if my_condition: # Es lo mismo que if my_condition == True
    print("Se ejecuta la condición del if")

print("La ejecución continua")

my_condition = 5 * 2

if my_condition == 10:  
    print("Se ejecuta la condición del segundo if")

if my_condition > 10 and my_condition < 20:  
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es es menor o igual que 10 o mayor o igual que 20")

print("La ejecución continua")

my_string = ""

if not my_string:
    print("My cadena de texto es vacia")

if my_string == "Mi cadena de texto00000":
    print("My cadena de texto coinciden")
