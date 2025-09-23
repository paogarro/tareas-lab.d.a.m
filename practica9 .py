#entrada
#cuantos estudiantes van a cargar?

#estudiante 1:
#nombre: ana
#nota en lab. apl. multiplataforma: 9 
#nota en programacion web: 8
#nota en diseño software: 7

#estudainte 2:
#nombre: bruno
#nota en lab. apl. multiplataforma: 5
#nota en programacion web: 4
#nota en diseño software: 6

#salida
#resumen

#estudiante: ana
#nota en lab. apl. multiplataforma: 9 
#nota en programacion web: 8
#nota en diseño software: 7
#promedio: 8.00
#estado: aprobado

#estudainte: bruno
#nota en lab. apl. multiplataforma: 5
#nota en programacion web: 4
#nota en diseño software: 6
#promedio: 5.00
#estado:desaprobado

num_estudiantes = int(input("Ingrese numero de estudiantes: "))
estudiantes = []

for i in range (0, num_estudiantes):
    print(f"ingresando datos del estudiante {i+1}:")
    nombre = input("ingrese el nombre del estudiante: ")
    nota_lab = float(input(f"ingrese la nota de lab. apl. multiplataforma del estudiante {nombre}: "))
    nota_web = float(input(f"ingrese la nota de programacion web del estudiante {nombre}: "))
    nota_diseño_software = float(input(f"ingrese la nota de diseño software del estudiante {nombre}: "))
    estudiantes.append(nombre)
    estudiantes.append(nota_lab)
    estudiantes.append(nota_web)
    estudiantes.append(nota_diseño_software)

    notas = (nota_lab, nota_web, nota_diseño_software)
    promedio = (sum(notas)/len(notas))
    
    if promedio >=6:
        estado = "aprobado"
    else:
        print("desaprobado")

estudiante = {"nombre": nombre, "notas": notas, "promedio": promedio, "estado": estado}

for estudiantes in estudiante:
    print(estudiante)