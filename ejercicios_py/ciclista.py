hora_partida = int(input("Ingrese la hora de salida: "))
minu_partida = int(input("Ingrese los minutos de salida: "))
segs_partida = int(input("Ingrese los segundos de salida: "))
segsViaje = int(input("ingrese el tiempo que tardo en segundos: "))
#convierto la hora de salida en segundos
segsInicial =  hora_partida*3600 + minu_partida*60 + segs_partida
#sumamos la hora de salida mas el tiempo de viaje
segsFinal = segsViaje + segsInicial
#Convertimos los segundos totales a hora, minutos y segundos
horaLlegada = segsFinal//3600
minsLlegada = (segsFinal%3600)//60
segsLlegada = (segsFinal%3600)%60
#muestra la hora de llegada
print("hora de llegada: ")
print(horaLlegada,":",minsLlegada,":",segsLlegada)
