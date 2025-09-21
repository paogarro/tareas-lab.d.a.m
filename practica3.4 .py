#Tres personas invierten dinero para fundar una empresa (no necesariamente en partes
#iguales). Calcular qué porcentaje invirtió cada una.

inversion1 = float(input("ingrese el dinero que invirtio la persona1: "))
inversion2 = float(input("ingrese el dinero que invirtio la persona2: "))
inversion3 = float(input("ingrese el dinero que invirtio la persona3: "))

total = inversion1 + inversion2 + inversion3
porcentaje1 = inversion1/total*100
porcentaje2 = inversion2/total*100
porcentaje3 = inversion3/total*100

print (f"el porcentaje que invirtio la persona1 es: {porcentaje1}%")
print (f"el porcentaje que invirtio la persona2 es: {porcentaje2}%")
print (f"el porcentaje que invirtio la persona3 es: {porcentaje3}%")