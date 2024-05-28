#Siempre tendremos que realizar cálculos complejos que pueden escribirse en python de maneras sencillas y obtener resultados precisos.

# Así por ejemplo, Calcular cuántos años necesitas para obtener una determinada cantidad partiendo de una cantidad inicial y una tasa de interés determinada. No tiene que ser una tarea complicada.
#No lo olvides: usamos interés compuesto: obtienes interés sobre tu interés.
#Veamos:

#Si tenemos una catidad de 1000 y queremos llegar a 1020 (objetivo), con un interés del 0.01 (1%) diario, tendremos que sumarle a nuestra cantidad inicial ese porcentaje, 
#convirtiéndose en nuestra nueva cantidad, a la que le sumaremos nuevamente ese porcentaje hasta obtener el valor objetivo.

# Declaramos nuestras variables:
cantidad = 1000
interes = 0.01
dia = 0
# Realizamos el primer cálculo (día 1):
cantidad = cantidad + (cantidad*0.01)
dia = dia + 1
# Visualizamos nuestra nueva cantidad:
print("Cantidad: $",cantidad)
print("Día: #", dia)

# Repetimos:
cantidad = cantidad + (cantidad*0.01)
dia = dia + 1
# Visualizamos nuestra nueva cantidad:
print("Cantidad: $",cantidad)
print("Día: #", dia)

# Podemos ver que obtenemos nuestro objetivo en dos (2 días).
# Sin embargo, si fuera necesario duplicar la cantidad, sería necesario repetir el cálculo muchas veces de forma incómoda e innecesaria.

# En este caso el ciclo while puede ser de gran utilidad, ya que se puede condicionar para obtener lo buscado. Ejemplo:

a = 0
b = 10
c = 0
#Queremos saber cuantas iteraciones toma sumarle 0.1 a la variable 'a' hasta llegar a 10, una vez se cumpla la condición nos mostrará la cantidad de veces que realizó la operación:
while a < b:
    a = a + 0.1
    c = c+1
print(c)

# Ahora inténtelo ud mismo, suponga que desea saber cuantos días le toma a la cantidad del primer ejemplo en triplicarse.
# Debe obtener 111 días

# Declaramos las variables:
cantidad_inicial = 1000
cantidad_objetivo = 3 * cantidad_inicial
interes_diario = 0.01
cantidad_actual = cantidad_inicial
dias = 0

# Usamos un ciclo while para iterar hasta que la cantidad actual sea igual o mayor al objetivo:
while cantidad_actual < cantidad_objetivo :
    cantidad_actual += cantidad_actual * interes_diario
    dias += 1

#Resultados
print("Cantidad alcanzada: $", cantidad_actual)
print("Días necesarios: ", dias)