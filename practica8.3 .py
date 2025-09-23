#Practica 8
#ACTIVIDAD 03:
#Definir una tupla con los nombres de cinco países. Luego, realizar las siguientes tareas:
#➢ Imprimir el contenido completo de la tupla.
#➢ Imprimir el primer y el último país de la tupla.
#➢ Verificar si un país (por ejemplo, "Argentina") se encuentra en la tupla.
#★ Mostrar cuántos países hay en total.

pais = ("argentina", "brazil", "alemania", "japon", "chile") 

print("paises:")
print(pais[0])
print(pais[1])
print(pais[2])
print(pais[3])
print(pais[4])

print("primer pais:", pais[0])
print("segundo pais:", pais[4])

print("argentina" in pais)
print(len(pais))