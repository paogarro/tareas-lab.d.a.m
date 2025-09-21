'''ACTIVIDAD 01 - La empresa de transporte:
Una empresa de transporte necesita un sistema para gestionar distintos tipos de vehículos.
Todos los vehículos tienen marca, modelo y capacidad de pasajeros, pero según el tipo de
transporte tienen características adicionales:
Colectivo: tiene un atributo recorrido (ejemplo: “Línea 60”) y un método parar_en_parada()
que muestre un mensaje como "El colectivo de la línea 60 está parando en la parada."
Taxi: tiene un atributo tarifa (precio base de viaje) y un método cobrar_viaje(distancia) que
calcule el costo multiplicando la tarifa por los km.
Avión: tiene un atributo aerolinea y un método despegar() que muestre un mensaje como
"El avión de Aerolíneas Argentinas está despegando."
La empresa quiere poder:
➢ Registrar diferentes vehículos (colectivos, taxis, aviones).
➢ Guardarlos en una lista.
➢ Recorrer la lista y mostrar la información de cada vehículo junto con sus
comportamientos específicos.'''


class Vehiculo:
    def __init__(self, marca, modelo, capacidad):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad
    def mostrar_info(self):
        print(f"marca:{self.marca}, modelo:{self.modelo}, capacidad:{self.capacidad}")

class Colectivo(Vehiculo):
    def __init__(self, marca, modelo, capacidad, recorrido):
        super().init(marca, modelo, capacidad)
        self.recorrido = recorrido
    def parar_en_parada(self):
        print(f"el colectivo de la linea {self.recorrido} está parando en la parada")
    def mostrar_info(self):
        print(f"modelo: colectivo, recorrido: {self.recorrido}")
    
class Taxi(Vehiculo):
    def __init__(self, marca, modelo, capacidad, tarifa):
        super().init(marca, modelo, capacidad)
        self.tarifa = tarifa
    def pago_del_viaje(self, distancia):
        costo_viaje = self.tarifa * distancia
        print(f"el costo del viaje es ${costo_viaje}")
    def mostrar_info(self):
        print(f"modelo: taxi, tarifa: {self.tarifa}")

class Avion(Vehiculo):
    def __init__(self, marca, modelo, capacidad, aerolinea):
        super().init(marca, modelo, capacidad)
        self.aerolinea = aerolinea
    def despegar(self):
        print(f"el avión de {self.aerolinea} está despegando")
    def mostrar_info(self):
        print(f"modelo: avion, aerolinea: {self.aerolinea}")

colectivo1 = Colectivo("marca: marca", "modelo: modelo", 8 , "linea 60")
taxi1 = Taxi("marca:" )


