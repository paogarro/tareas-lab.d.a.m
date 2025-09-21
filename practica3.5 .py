#ACTIVIDAD 05:
#Calcular el total a pagar por la compra de camisas. Si se compran tres camisas o más se
#aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un
#descuento del 10%. El precio de cada camisa se ingresa junto a la cantidad de camisas vendidas.

cantidad = int(input("ingrese cuantas camisas quiere comprar: "))
precio = 2000*cantidad
descuento = precio*0.20
descuento1 = precio*0.10
total = precio-descuento
total1 = precio-descuento
if cantidad > 3:
    print(f"recibe un descuento del 20%, en total paga: {total}")

elif cantidad < 3:
     print(f"recibe un descuento del 10%, en toltal paga: {total1}")
else:
    print("error, ingrese nuevamnete la cantidad de camisas que desea comprar")