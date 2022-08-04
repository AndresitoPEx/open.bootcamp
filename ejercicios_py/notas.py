parcial1= int(input("Ingrese nota 1: "))
parcial2= int(input("Ingrese nota 2: "))
parcial3= int(input("Ingrese nota 3: "))

examen = int(input("Ingrese nota del examen: "))
trabajo = int(input("Ingrese nota del trabajo: "))

nota = ((parcial1+parcial2+parcial3)/3)*0.55 + 0.3*examen + 0.15*trabajo

print ("nota final: ",nota)