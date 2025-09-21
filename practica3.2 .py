#Obtenga el importe de un viaje en remis, sabiendo que el valor del km es de $700. 
#Se debe ingresar los km de cada viaje.

valor_por_km = 700
km_recorridos = int(input("ingrese los km que ha recorrido en el remis: "))
importe = km_recorridos*valor_por_km
print (f"el importe del viaje en remis es: ${importe}")