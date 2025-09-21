#Crear una clase llamada Robot que tenga como atributos nombre, modelo y batería (en
#porcentaje), e implemente dos métodos: trabajar(horas), que reduzca la batería en un 10%
#por cada hora de trabajo y muestre un mensaje si la batería es insuficiente, y
#recargar(porcentaje), que aumente la batería en la cantidad indicada sin superar el 100% e
#informe el nivel actual. Luego, crear un objeto de esta clase con los datos que elijas, probar
#los métodos haciendo trabajar y recargar al robot, y por último mostrar los resultados por pantalla.

class robot:
    def __init__(self, nombre, modelo, bateria):
        self.nombre = nombre
        self.modelo = modelo
        self.bateria = bateria

    def trabajar(self, horas):
        gasto_de_bateria = horas*10
        
        if self.bateria < gasto_de_bateria:
            print(f"es poca la bateria de {self.nombre} no puede trabajar {horas} horas")

        else:
            self.bateria -= gasto_de_bateria
            print(f"{self.nombre} trabajo {horas} horas, la bateria es {self.bateria}%")

    def cargar(self, porcentaje):
        self.bateria += porcentaje 
        if self.bateria > 100:
            self.bateria = 100
            print(f"{self.nombre} esta cargado, la bateria es {self.bateria}%")

mi_robot = robot("robot3000", "cocinero", 65)
mi_robot.trabajar(7)

