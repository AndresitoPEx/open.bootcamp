# Queremos guardad los nombres y edades de los alumnos de un curso
# Realizar un programa que introduzca el nombre y edad de cada alumno
# El proceso de lectura terminara cuando se introduzca un * 
# Al finalizar se mostrara el nombre y la edad de los alumnos mayores

nombres=[]
edades=[]
#Inicializamos la lista hasta que intruzca un *
while True:
    nombre = input("Ingrese el nombre del alumno: ")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Ingrese su edad: ")))
    if nombre == "*":
        break
#calculamos la edad maxima
edad_max = max(edades)
#alumnos mayores de edad
print("Alumnos mayores de edad: ")
print("============================")
for nombre,edad in zip(nombres,edades):
    if edad >= 18:
        print(nombre)
#alumnos mayores
print("Alumnos mayores")
print("============================")
for nombre,edad in zip(nombres,edades):
    if edad == max(edades):
        print(nombre)

