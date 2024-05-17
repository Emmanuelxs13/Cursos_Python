# Requerimiento:
# Una entidad bancaria realiza préstamos hipotecarios a sus clientes y requiere un programa que permita mostrarle al usuario cuál sería el monto prestado,
#  la cuota inicial y los pagos mensuales y anuales que pagaría en un periodo de 15 años.

monto_prestamo = float(input("Ingrese el monto del préstamo: "))
ingresos_mensuales = float(input("Digite sus ingresos mensuales: "))

if ingresos_mensuales < 2000000 :
    print("No se puede prestar por bajos ingresos")
elif ingresos_mensuales >= 3200000 :
    cuota_inicial = monto_prestamo * 0.35
    monto_maximo = 180000000
    print("Cuota inicial: $", cuota_inicial)
    print("Monto máximo: $", monto_maximo)
    print("Pagos mensuales para 10 años: $", (monto_prestamo - cuota_inicial)/120)
    print("Pagos mensuales para 15 años: $", (monto_prestamo - cuota_inicial)/180)
elif ingresos_mensuales >= 2000000 :
    cuota_inicial = monto_prestamo * 0.25
    monto_maximo = 120000000 if monto_prestamo > 120000000 else monto_prestamo
    print("Cuota inicial: $", cuota_inicial)
    print("Pagos mensuales para 10 años: $", (monto_prestamo - cuota_inicial)/120)
    print("Pagos mensuales para 15 años: $", (monto_prestamo - cuota_inicial)/180)
    
    