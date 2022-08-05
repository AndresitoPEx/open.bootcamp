es_primo = True
num = int(input("Ingrese un numero: "))
for var in range(2,num):
    if num % var == 0:
        es_primo = False
        break
if es_primo:
    print("es Primo")
else:
    print("no es primo")
