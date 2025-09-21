#En una plataforma de streaming, se quiere mejorar la experiencia del usuario ofreciendo
#recomendaciones personalizadas según sus gustos. El sistema debe preguntar al usuario
#qué tipo de película le gusta (acción, comedia o drama) y, con base en su respuesta,
#recomendar una película dentro de esa categoría. Si el usuario proporciona una 
#respuesta no válida, el sistema debe mostrar un mensaje de error.

pelicula = input("que tipo de pelicula te gusta, accion, comedia o drama????: ")
accion = "avengers: infinity war"
comedia = "son como niños"
drama = "a dos metros de ti"

if pelicula == "accion":
    print(f"te recomiendo mirar {accion}")
elif pelicula == "comedia":
    print(f"ee recomiendo mirar {comedia}")
elif pelicula == "drama":
    print(f"ee recomiendo mirar {drama}")
else:
    print("error, ingrese nuevamente que tipo de pelicula te gustaria ver")