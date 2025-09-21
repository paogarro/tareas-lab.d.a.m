#ACTIVIDAD 03:
#Si se adquiere un electrodoméstico en 48 cuotas. Indicar cuál será el valor de la cuota, si se
#añade sobre el valor total un 15% de interés.

valor_electrodomestico = float(input("ingrese precio del electrodomestico: "))
producto_recarga = valor_electrodomestico*1.15
cuota = producto_recarga/48
print(f"la cuota final es de: {cuota}")