#tu propio libro
#crear una clase que represente un libro. piensen que informacion necesita guardar un libro y que acciones deberia 
#poder realizar, crear algunos objetos de la clase y probar los metodos que diseñaron, monstrando los resultados
#por pantalla.

class Libro:
    def __init__(self, titulo, autor, cant_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cant_paginas = cant_paginas
        self.leido = False
    def se_leyo(self):
        