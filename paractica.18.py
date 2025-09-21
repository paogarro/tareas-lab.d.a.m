
#PRACTICA 

#class Auto:
#    def __init__(self, combustible):
#        self.combustible = combustible

#class Conductor:
#    def __init__(self, nombre):
#        self.nombre = nombre
#    def conducir(self, auto, litros):
#        if auto.combustible >= litros:
#            auto.combustible -= litros 
#            print(f"{self.nombre} gasto {litros} litros, y le quedaron {auto.combustible}")
#        else:
#            print(f"tu auto no tiene combustible suficiente: {auto.combustible}")
        
#conductor1 = Conductor("octavio")
#auto1 = Auto(1000)
#conductor1.conducir(auto1, 500)

#print(f"se muestra el nombre del conductor en pantalla: {conductor1.nombre}")
#print(f"se muestra la cantidad de combustible en pantalla: {auto1.combustible}")


'''
#practica 18 (grupo con: liam y more)
ACTIVIDAD 01 - Sistema de venta de entradas :
Un cantante famoso dará un show en la ciudad y se necesita un sistema para controlar la
venta de entradas.
➢ Actualmente no hay registro y se generan problemas:
➢ Algunos compran más entradas de las disponibles.
➢ No queda claro cuántas entradas tiene cada persona.
➢ No se sabe cuántas entradas quedan para vender.
Clases y objetos:
Show:
➢ Nombre del artista.
➢ Fecha del recital.
➢ Cantidad total de entradas disponibles.
➢ mostrar_info() que muestre los datos y cuántas entradas quedan.
Cliente:
➢ Nombre del cliente.
➢ Cantidad de entradas que compró.
➢ Un método comprar(show, cantidad) para comprar entradas (si hay disponibles).
➢ mostrar() que indique cuántas entradas tiene.
En el programa principal:
➢ Crear un show con 5 entradas disponibles.
➢ Crear 2 clientes.
➢ Simular la compra de entradas (uno compra 2 y el otro intenta comprar más de
lo que queda).
➢ Mostrar cuántas entradas quedan y qué compró cada cliente
'''

class Show:
    def __init__(self, nombre_artista, fecha_recital, cant_entradas):
        self.nombre_artista = nombre_artista
        self.fecha_recital = fecha_recital
        self.cant_entradas = cant_entradas
        self.entradas_vendidas = 0
        self.total_entradas = 5

    def entradas_disponibles(self):
       self.total_entradas - self.entradas_vendidas
    def mostrar_info(self):
        print(f"---show info---")
        print(f"artista: {self.nombre_artista}")
        print(f"fecha: {self.fecha_recital}")
        print(f"cantidad entradas: {self.cant_entradas}")
        print(f"entradas disponibles: {self.entradas_disponibles}")

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.entradas_compradas = 0
    def comprar (self, show, cantidad):
        if cantidad <= show.entradas_disponibles:
            show.total_entradas -= cantidad                                                          
            self.entradas_compradas += cantidad
            print(f"se pudo realizar la compra de {self.nombre}, la cant de entradas que compro fue de: {cantidad}")
        else:
            print(f"no se pudo realizar la compra de {self.nombre} ya que no hay suficientes entrdas disponibles, solo quedan {show.entradas_disponibles} entradas")
    def mostrar_info(self):
        print(f"{self.nombre} tiene {self.entradas_compradas} entradas")
        
concierto = Show("twenty one pilots", "11/07", 5)
pao = Cliente("pao", 3)
liam = Cliente("liam", 6)



