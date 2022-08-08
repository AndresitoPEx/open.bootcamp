#realiza un programa que compruebe si una cadena inicia por otra subcadena ingresada por el teclado
cad = input("Ingrese un texto: ")
subcad = input("Ingrese otro texto: ")
if cad.startswith(subcad):
    print("La cadena empieza por la subcadena")
else:
    print("La cadena NO empieza por la subcadena")