#ACTIVIDAD 02:
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for a in range(1,11):
    print("tabla dwe multiplicar del {a}:")
    for b in range(1,11):
        resultado = a*b
        print(f"{a}x{b}={resultado}")