# Programa: Calculo del área sobrada en una figura
# Autor: Emmanuel Berrio
# Fecha: 16/05/2024
# Versión: V1.0

print("======================================================")
print("==============CALCULO DEL ÁREA SOMBREADA==============")
print("======================================================")

#  === Sección de asignación de valores ========
altura = int(input("Ingresa el valor de la altura"))

#  === Sección de calculos =========
# Calcular el área del rectangulo
area_rect = (2*altura)*altura

# Calcular el área del triangulo
area_tri = altura*altura/2

# Área circulo
area_circ = 3.1416*(altura/2)**2

area_total = area_rect + area_tri - area_circ

#  === Resultados ==============
print(f"El área de la figura sombreada es: {area_total}")