#Una persona tiene hasta 3 intentos para ingresar su nombre de usuario. Si excede estos 3
#intentos, el programa debe mostrar el mensaje "Has superado el límite de intentos" y
#finalizar. Si ingresa el nombre de usuario válido "aula" antes de los 3 intentos, 
#el programa mostrará el mensaje "Ingreso exitoso" y finalizará.

nombre_de_usuario = "aula"
intentos = 3

while intentos > 0:
    nombre = input("ingrese su nombre de usuario: ")
    if nombre == nombre_de_usuario:
        print("ingreso exitoso")
    else:
        intentos -= 1
        print(f"incorrecto solo te quedan {intentos} intentos, ingrese nuevamnete su nombre de usuario: ")

if intentos == 0:
    print("has superado el límite de intentos")