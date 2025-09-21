#El programa le pedirá al usuario que adivine la palabra secreta, que es "python". 
#El usuario tiene 3 intentos para acertar la palabra. Si lo adivina correctamente
#el programa muestra "¡Correcto!". Si no lo adivina en 3 intentos, 
#muestra "Has superado el límite de intentos".

palabra_secreta = "python"
intentos = 3

while intentos > 0:
    palabra = input("adivina la palabra secreta: ")
    if palabra == palabra_secreta:
        print("adivinaste la palabra secreta")
    else:
        intentos -= 1
        print(f"incorrecto solo te quedan {intentos} intentos")

if intentos == 0:
    print("has superado el límite de intentos")