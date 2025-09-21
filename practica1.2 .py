#ACTIVIDAD 02:
#Escribir un programa que tome tres números como entrada del usuario y realizar las
#siguientes operaciones:
#● Sumar el primero y el segundo número.
#● Restar el segundo número del primero.
#● Multiplicar el primero por el tercero.
#● Dividir el primero por el segundo.
#● Realizar la división entera del tercero por el segundo.
#● Calcular el módulo del primero por el tercero.
#● Elevar el segundo al tercer número.
#★ Imprimir el resultado correspondiente utilizando f-string.

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))
suma = numero1 + numero2
resta = numero1 - numero2 
multiplicacion = numero1*numero3
division = numero1/numero2
division_entero = numero3/numero2

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicacion es: {multiplicacion}")
print(f"La division es: {division}")
print(f"La divion entera es: {division_entero}")