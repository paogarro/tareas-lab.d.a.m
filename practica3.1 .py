#Dado la cantidad de votos obtenidos por 3 partidos distintos, calcular los porcentajes
#de votos alcanzados por cada partido.

partido1 = int(input("Ingrese la cantidad de votos obtenidos em el partido1: "))
partido2 = int(input("Ingrese la cantidad de votos obtenidos em el partido2: "))
partido3 = int(input("Ingrese la cantidad de votos obtenidos em el partido3: "))

total = partido1 + partido2 + partido3
porcentaje1 = partido1/total*100
porcentaje2 = partido2/total*100
porcentaje3 = partido3/total*100

print (f"El porcentaje del primer partido es:{porcentaje1}%")
print (f"El porcentaje del segundo partido es:{porcentaje2}%")
print (f"El porcentaje del tercer partido es:{porcentaje3}%")