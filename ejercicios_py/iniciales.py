name = input("Ingrese su nombre: ")
firstName = input("Ingrese su primer apellido: ")
LastName = input("Ingrese su segundo apellido: ")

iniciales = name[0]
iniciales = iniciales + firstName[0]
iniciales = iniciales + LastName[0]

iniciales = iniciales.upper()

print ("Las iniciales de tu nombre son: ",iniciales)


