#ingrese una cadena y un caracter por el teclado y verifique que sea un caracter y tambien cuantas veces se repite en la cadena

cad = input("Ingrese una palabra: ")
while True:
    caracter = input("Ingrese un caracter: ")
    if len(caracter) > 1:
        print("Me tienes que dar solo un caracter")
    if len(caracter) == 1:
        break
print("En la cadena ",cad,"aparecen",cad.count(caracter),"veces el caracter",caracter)
