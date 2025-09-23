#ACTIVIDAD 01:
#Solicitar al usuario que ingrese el monto total de una cuenta en un 
#restaurante y el porcentaje de propina que desea dejar. Luego, 
#el programa debe calcular cuánto es la propina y cuánto es el total a pagar.
#➢ Utilizar al menos una función para realizar el cálculo.
#➢ Imprimir los resultados.

monto_total = float(input("Ingrese el monto total de su compra: "))
propina = float(input("Cual es el porcentaje de propina desea dejar?: "))

def porcentaje(monto_total, propina):
    porcentaje = (propina/100) * monto_total
    precio_final = monto_total + porcentaje
    print(f"tendra que pagar: {precio_final}")

porcentaje(monto_total, propina)