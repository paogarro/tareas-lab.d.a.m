"""ACTIVIDAD 01 - Plataforma de Streaming:
Una empresa necesita un sistema para gestionar los contenidos multimedia que ofrece, los
cuales comparten ciertas características generales: cada contenido tiene un título, una
duración en minutos y un año de publicación, que servirán como base común para organizar
la información y diferenciar los distintos tipos de materiales."""

"abstraccion hace foco en que es, como es y que es lo que hace""atributos, metodos"

class Tipo_de_contenido():
    def __init__(self, titulo, duracion_minutos, año_publicacion):
        self.titulo = titulo
        self.duracion_minutos = duracion_minutos
        self.año_publicacion = año_publicacion

class Pelicula(Tipo_de_contenido):
    def __init__(self, director, genero):
        self.director = director
        self.genero = genero

        peli = input(str("ingrese que pelicula quiere ver: "))
        se_produce_peli = input(str(f"quiere reproducir la pelicula {peli}???? si/no"))
        if se_produce_peli == ("si"):
            print(f"la película {peli} está siendo proyectada junto con {self.director}")
        else:
            print(f"la peli {peli} no esta siendo proyectada")

class Serie(Tipo_de_contenido):
    def__init__(self, num_temporadas, num_episodios)
        self.num_temporadas = num_temporadas
        self.num_episodios = num_episodios

        serie = input(str("ingrese que serie quiere ver: "))
        se_produce_serie = input(str(f"quiere reproducir la serie {serie}???? si/no"))
        if se_produce_serie == ("si"):
            print(f"la serie está siendo proyectada en el episodio {self.episodio} en la temporada {self.temporada}")
        else:
            print(f"la serie {serie} no esta siendo proyectada")

class Documental(tipo_de_contenido):
      def __init__(self, tema, relator)
          self.tema = tema
          self.relator = relator

          documental = input(str("ingrese el documental que quiere ver: "))
          se_produce_documental = input(str(f"quiere reproducir el documental {documental}???? si/no"))
          if se_produce_documental == ("si"):
              print(f"el documental {documental} está siendo proyectado, se trata de {self.documental} sobre el tema {self.tema} y esta siendo relatado por {self.relator}")
          else:
              print(f"el documental {documental} no esta siendo proyectado")



        