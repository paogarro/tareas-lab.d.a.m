#En una ciudad, el sistema de transporte público tiene tarifas diferenciadas según la edad de
#los pasajeros. Se desea desarrollar un programa que calcule el costo del pasaje de colectivo 
#para un usuario, basado en su edad. El programa debe seguir las siguientes reglas
#para determinar el costo del pasaje:
#➢ Si la persona tiene menos de 5 años, el viaje es gratis.
#➢ Si la persona tiene entre 5 y 17 años (inclusive), el costo del pasaje es $150.
#➢ Si la persona tiene entre 18 y 65 años (inclusive), el costo del pasaje es $250.
#➢ Si la persona tiene más de 65 años, el costo del pasaje es $200.

edad = int(input("Ingrese su edad: "))
if edad < 5:
    print("El viaje es gratis")
elif edad >= 5 and edad <= 17:
    print("El costo del viaje es $150")
elif edad >= 18 and edad <= 65:
    print("El costo del viaje es $250")
elif edad >= 65:
    print("El costo del viaje es $200")
else:
    print("Error, vuelva a ingresar su edad")