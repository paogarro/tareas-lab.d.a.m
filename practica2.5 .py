#Una tienda ofrece descuentos especiales a sus clientes según el monto de la compra y su
#historial de compras. Se desea desarrollar un programa que calcule el descuento que se
#aplicará a un cliente, basándose en las siguientes condiciones:
#➢ Si el monto de la compra es mayor a $15.000 y el cliente es frecuente, se aplica un
#descuento del 20%.
#➢ Si el monto de la compra es mayor a $15.000 pero el cliente no es frecuente, se
#aplica un descuento del 10%.
#➢ Si el monto de la compra es mayor a $10.000, se aplica un descuento del 5%.
#➢ Si el monto de la compra es $10.000 o menos, no se aplica ningún descuento.

monto = float(input("ingrese el monto de la compra: "))
cliente = input("ingrese si eres un cliente frecuente o un cliente no frecuente ")
frecuente = "soy frecuente"
no_frecuente = "no soy frecuente"
descuento1 = monto*0.20
descuento2 = monto*0.10
descuento3 = monto*0.05

if monto > 15.000 and cliente == frecuente:
    print(f"el cliente es frecuente, se le aplica un descuento del 20 porciento, en toltal seria {descuento1}")
elif monto > 15.000 and cliente == no_frecuente:
    print(f"el cliente no es frecuente, se le aplica un descuento del 10 porciento, en total seria {descuento2}")
elif monto > 10.000:
    print(f"se le aplica un descuento del 5 porciento, en total seria {descuento3}")
elif monto <= 10.000:
    print("no se le aplica ningun descuento")