import math
cateto1 = int(input("Ingrese el valor del cateto 1: "))
cateto2 = int(input("Ingrese el valor del cateto 2: "))
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print ("La hipotenusa es: %.2f" % hipotenusa)