# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

# Respuesta
# print("¡Hola Mundo!")

# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

# Respuesta
# my_cadena = "!Hola Mundo!"  
# print(my_cadena)

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
# muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido. 

# Respuesta
# name =  input("Introduce tu nombre: ") 
# print ("!Hola " + name)


# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
# (3+2/2*5)2

# Respuesta
# Operacion = ((3+2)/(2*5)) ** 2
# print(Operacion)


# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

# Respuesta
# horas_trabajo = float(input("Digite le número de horas trabajadas:"))
# precio_hora = float(input("Digite el precio por hora:"))
# resultado = horas_trabajo * precio_hora
# print("Tu pago es:", resultado)

# Escribir un programa que lea un entero positivo, 
# N introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
#  N. La suma de los N primeros enteros positivos puede ser calculada de la siguiente forma:
# suma = n(n + 1)/2

# Respuesta
# N = int(input("Ingrese un número: "))

# suma = N * (N + 1)/2
# print("La suma de los primeros números enteros desde 1 hasta", N , "es:", suma)

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal
#  y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice
#  de masa corporal calculado redondeado con dos decimales.

# Respuesta
# peso = float(input("Ingrese su peso en kg:"))
# estatura = float(input("Ingrese su estatura en metros:"))

# imc = round(float(peso)/float(estatura)**2,2)

# print("Su índice de masa carporal es de:", str(imc))

# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> 
# donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

# n = input("Ingresa el dividendo (entero): ")
# m = input("Ingrese el divisor (entero): ")

# # Cociente
# c = int(n) // int(m)

# # Resto
# r = int(n) % int(m)

# print(n, "entre", m, "da un resultado de", str(c), "y un resto de", str(r))

# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
#  y muestre por pantalla el capital obtenido en la inversión.

# Resultado
# dinero_inversion = float(input("Ingrese la cantidad de dinero que desea invertir: "))
# interes_anual = float(input("Ingrese el porcentaje de interés anual: "))
# años_inversion = float(input("Ingrese el tiempo de duración de la inversión en años: "))

# capital_obtenido = float(dinero_inversion) * ((1+float(interes_anual/100)) ** float(años_inversion))

# print("Su capital obtenido en la inversión es de:", str(capital_obtenido))

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y 
# la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y 
# muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.