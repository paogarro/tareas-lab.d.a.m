#ACTIVIDAD 01:
#Definir una función llamada calculadora que tome dos valores y devuelva el
#resultado de la operación matemática correspondiente (suma, resta, multiplicación y
#división).

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

def calculadora(a, b):
    suma = a + b
    print(f"La suma es: {suma}")

    resta = a-b
    print(f"La resta es: {resta}")

    multiplicacion = a*b
    print(f"La multiplicacion: {multiplicacion}")

    division = a/b
    print(f"La division: {division}")

calculadora(num1, num2)