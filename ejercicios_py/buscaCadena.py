#realice un programa que verifique si dentro de una cadena hay otra subcadena
cad = input("Ingrese un texto: ")
subcad = input("Ingrese un subtexto: ")

if cad.find(subcad) > -1:
    print("La",cad,"contiene",subcad)
else:
    ("Error")

if subcad in cad:
    print("Se confirma")
else:
    print("Horror")