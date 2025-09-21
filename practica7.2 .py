#Solicitar al usuario un número entero y, si el número es positivo, imprimir el mensaje 
#"El número es positivo", y si el número es negativo, imprimir "El número es negativo". 
#Si el número es igual a cero, imprimir "El número es cero".

numero = int(input("ingrese un numero entero: "))

if numero >0:
    print("el número es positivo") 
elif numero <0:
    print ("el número es negativo")
else:
    cero = 0 
    print(f"el número es {cero}")