suma = 0
contador = 0

num = int(input("ingrese un numero: "))
while num != 0:
    suma = suma + num
    contador = contador + 1
    num = int(input("ingrese un numero: "))
if contador > 0:
    media = suma / contador
else:
    media = 0

print("suma: ",suma)
print("media : ",media)