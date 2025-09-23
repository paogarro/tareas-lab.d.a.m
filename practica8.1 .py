#Practica 8 
#ACTIVIDAD 01:
#Definir una lista con los nombres de cinco de tus amigos. Luego, realizar las siguientes tareas:
#➢ Agregar un nuevo amigo al final de la lista.
#➢ Modificar el nombre de uno de los amigos en la lista.
#➢ Eliminar un amigo de la lista.
#➢ Imprimir la lista final.

#la estructura de datos es una forma de guardar info

amigos = ["caro", "more", "liam", "orion", "juanpi"]
amigos.append("messi")
modifica = 1
amigos[modifica] = "sere"
eliminar = "more"
amigos.remove(eliminar)
print(amigos)