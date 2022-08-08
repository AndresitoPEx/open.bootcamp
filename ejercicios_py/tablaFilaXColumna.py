# Diseñar un algoritmo que 
# Crear una tabla bidimensional de 5x5 enteros
# Cargar la tabla con valores numericos enteros
# Sumar todos los enteros de cada fila y de cada columna

tabla = []
for indice_fila in range(1,6):
    fila = []
    for indice_col in range(1,6):
        fila.append(int(input("Introduce el numero de fila %d y columna %d:" % (indice_fila,indice_col))))
    tabla.append(fila)
#sumar filas
indice_fila = 1
for fila in tabla:
    print("La suma de los elementos de la fila %d es %d" % (indice_fila,sum(fila)))
    indice_fila += 1
#suma columnas
for indice_col in range(1,6):
    suma = 0
    for fila in tabla:
        suma =  suma + fila[indice_col - 1]
    print("La suma de los elementos de la columna %d es %d" % (indice_col, suma))
