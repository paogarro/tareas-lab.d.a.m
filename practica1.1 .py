#ACTIVIDAD 01:
#Registro de Información de Automóvil
#María Laura es una vendedora de automóviles que necesita mantener un registro de
#la información de los automóviles en su inventario. Cada vez que ingresa un nuevo
#automóvil al inventario, debe registrar la marca, el modelo, el año y el color.
#Escribir un programa que ayude a María Laura a ingresar los datos de un automóvil
#y luego imprima un mensaje que incluya esta información en el siguiente formato:
#"María Laura ha registrado un automóvil de marca [marca], modelo [modelo] del año
#[año]. Tiene un color [color]."

marca = input("Ingresar marca del auto: ")
modelo = input("Ingresar modelos del auto:")
año = int(input("Ingresar año del auto:"))
color = input("Ingresar color del auto:")

print(f"Maria Laura ha registrado un auto de la marca, {marca}, modelo {modelo}, del año {año}, del color {color}")