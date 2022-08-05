resultado = 1
num = int(input("Dime un numero: "))
for contador in range (2, num+1):
    resultado = resultado * contador
print("El factorial de",num, "es: ",resultado)

# resultado = 1
# num = int(input("Ingrese un numero: "))
# contador = 2
# while contador <= num:
#     resultado = resultado * contador
#     contador =  contador + 1 
# print("El resultado es: ", resultado)