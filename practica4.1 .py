#determinar si un estudiante aprueba o reprueba una materia, sabiendo que aprobara
#si su promedio de tres calificaciones es mayor o igual a 7,de lo contrario sera reprobado

calificacion1 = float(input("ingresa la primer calificacion: "))
calificacion2 = float(input("ingresa la segunda calificacion: "))
calificacion3 = float(input("ingresa la tercera calificacion: "))

promedio = (calificacion1 + calificacion2 + calificacion3)/3

if promedio >= 7:
    print(f"el estudiante aprueba con un promedio de: {promedio}")

else:
    print("el estudiante reprueba")