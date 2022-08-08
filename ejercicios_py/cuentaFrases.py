#Programa para contar las palabras de una frase
contador = 0
posicion = 0 
cad = input("Ingrese una frase: ")
#elimino los espacios con stripe
cad = cad.strip()
#Voy buscando los espacios
posicion = cad.find(" ", posicion)
while (posicion != -1):
    contador += 1
    #No tengo en cuenta los espacios que hay entre cada palabra
    while cad[posicion+1] == " ":
        posicion += 1
    posicion = cad.find(" ", posicion + 1)
print("La frase tiene",contador+1,"palabras")
