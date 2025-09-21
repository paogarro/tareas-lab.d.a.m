#Solicitar al usuario que ingrese un número límite (un número entero positivo). 
#Luego, utilizar un bucle while para imprimir todos los números desde 1 hasta el límite 
#especificado, incluyendo el número límite. El bucle debe detenerse una vez que se 
#haya alcanzado el número límite, verificar que el número ingresado sea positivo para 
#evitar un ciclo infinito.

i=1
numero_limite = int(input("ingrese un numero entero positivo: "))

while numero_limite <= 0:
    print("error, el numero limite debe ser positivo")
    numero_limite = int(input("ingrese el numero "))

while i <= numero_limite:
    print(i)
    i = i+1