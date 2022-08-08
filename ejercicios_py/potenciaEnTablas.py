#Realizar la potencia al cuadrado y cubo de una lista random
import random
lista_numeros = []
#primer recorrido para leer la lista
for indice in range(1,11):
    lista_numeros.append(random.randint(1,10))
#segundo recorrido para operar los numeros aleatorios
for num in lista_numeros:
    print(num," : ",num**2," : ",num**3)

