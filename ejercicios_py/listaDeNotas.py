#Crear un programa donde se pueda ingresar 5 notas entre 0 y 10
#Imprimir la media de las notas, la nota maxima y la nota minima

notas = []
for indice in range(1,6):
    while True:
        nota = int(input("Introduce una nota %d: " %indice))
        if nota>=0 and nota<=10:
            break
    notas.append(nota)
#muestro los resultados
print("Notas: ",end="")
for nota in notas:
    print(nota," ",end=" ")
print()
print("Nota media: ",sum(notas)/len(notas))
print("Nota max: ",max(notas))
print("Nota min: ",min(notas))
