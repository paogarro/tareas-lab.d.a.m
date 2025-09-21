#En un sistema de acceso a una plataforma, se requiere verificar la validez de la 
#contraseña ingresada por el usuario. Si la contraseña es correcta, se concede el acceso.
# Si no es correcta, el sistema debe ofrecer la opción de restablecer la contraseña. 
#Si el usuario elige restablecerla, deberá ingresar una nueva contraseña, 
#la cual será almacenada y confirmada.

contraseña = "nose"
contraseña_ = input("Ingrese la contraseña: ")
intentos = 3

while intentos > 0:
    contraseña_ingresada=input("Ingrese la contraseña: ")
    if contraseña_ingresada == contraseña:
        print("Acceso concedido")
        break #break es para salir de bucle de while (para no olvidarme)
    else: 
        intentos -=1
        print(f"Contraseña incorrecta, solo te quedan {intentos} intentos: ")
        if intentos == 0:
            restablecer_contraseña = input("¿Quiere restablecer la contraseña? (si/no): ")
            if restablecer_contraseña == "si":
                while True:
                    nueva_contraseña = input("Ingrese una nueva contraseña: ")
                    confirmacion = input("Confirme la contraseña ingresada: ")
                    if nueva_contraseña == confirmacion:
                        contraseña_valida = nueva_contraseña
                        print("Contraseña restablecida")
                        break
                    else:
                        print("Las contraseñas no son iguales, ingresela denuevo: ")
else:
    print("Acceso denegado")
