from Computadora import Computadora
class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__computadoras = list(computadoras)

    @property
    def id_orden(self):
        return self.__id_orden
    @id_orden.setter
    def id_orden(self, id_orden):
        self.__id_orden = id_orden

    @property
    def computadoras(self):
        return self.__computadoras
    @computadoras.setter
    def computadoras(self, computadoras):
        self.__computadoras = list(computadoras)

    def agregarComputadora(self, computadora: Computadora):
        self.computadoras.append(computadora)
