#Desafío del Asistente de Compras
#Desarrollar un asistente de compras en línea que permita al usuario ingresar hasta 5
#productos, mostrando el nombre, precio, cantidad y subtotal de cada uno.
#Requisitos:
#➢ El usuario puede ingresar hasta 5 productos. Para cada uno, se debe mostrar:
#○ Nombre del producto.
#○ Precio unitario.
#○ Cantidad comprada.
#○ Subtotal (precio * cantidad).
#○ El programa debe calcular el total de la compra sumando los subtotales de todos los productos.
#➢ Descuento del 10% si el total supera los $100.000
#➢ Si el usuario compra exactamente 5 productos, realizar un descuento del
#15% y mostrar un mensaje especial: "¡Felicidades, tenes una compra de 5 productos!".
#➢ Mostrar el total final después de aplicar descuento.
#➢ Agregar una mejora al programa

total_compra = 0
productos = int(input("ingrese cuantos productos desea comprar: "))

for i in range (productos):
    nombre = input(f"ingrese el nombre del producto {i}: ")
    precio = float(input(f"ingrese el precio del producto {i}: "))
    cantidad = int(input(f"ingrese la cantidad de productos que desea comprar {i}: "))
    sub_total = precio*cantidad
    total_compra = total_compra + sub_total
    print(f"producto {total_compra}")

if total_compra > 100000:
    descuento = total_compra-(total_compra*0.10)
    print("recibe un descuento del 10%")

elif cantidad == 5:
    descuento = total_compra-(total_compra*0.15)
    print("¡felicidades, tenes una compra de 5 productos!")
    
else:
     print("no recibe descuento")


print(descuento)