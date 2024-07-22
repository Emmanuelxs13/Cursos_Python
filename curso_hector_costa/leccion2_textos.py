'Hello world'

"Hello world"

'Estes texto incluye unas comillas " " '

"Esta 'palabra' se encuentra escrita entre comillas simples"

"Esta \"palabra\" se encuentra escrita entre comillas dobles"

' Esta \'palabra\' se encuentra escrita entre comillas dobles'

"Una cadena"
'otra cadena'
'otra cadena más'

print("Una cadena")
print('otra cadena')
print('otra cadena mas')

print("Un texto\tuna tabulacion")

print("Un texto\nuna nueva linea")

# Para mostrar una cadena de enlace a un directorio y que no tome los \
print(r"C:\nombre\directorio")

print("""Una linea
      otra linea
      otra linea\tuna tabulación""")

c = "Esto es una cadena\ncon dos lineas"
print(c)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

palabra = "Python"
palabra[0] # Caracter en la posición cero

palabra[3]

palabra[-1] # Caracter en la posición final

palabra[0:2]

palabra[2:-1]

palabra = "N" + palabra[1:]
palabra

len(palabra)