dia = int(input("Ingrese un dia: "))
mes = int(input("Ingrese un mes: "))
anio = int(input("Ingrese un año: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias_del_mes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_del_mes = 30
elif mes == 2:
    if(anio % 4 ==0 and not (anio % 100 == 0)) or anio % 400 == 0:
        dias_del_mes = 29
    else:
        dias_del_mes = 28
else:
    print("fecha incorrecta")
if dia < 0 or dia > dias_del_mes:
    print("fecha incorrecta")
else:
    print("fecha correcta")