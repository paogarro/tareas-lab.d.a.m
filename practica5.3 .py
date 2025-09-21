#ACTIVIDAD 03:
#Escribir un programa que almacene la contraseña en una variable, pregunte al usuario por
#la contraseña hasta que introduzca la contraseña correcta.

contraseña_correcta = "si"
while True
    contraseña = input("introduce la contraseña: ")
    if contraseña == contraseña_correcta:
        print("contraseña correcta")
    else:
        print("contraseña incorrecta, intentalo de nuevo")