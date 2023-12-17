from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton




class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor : Monitor, teclado : Teclado, raton : Raton) :
        Computadora.contador_computadoras += 1
        self.__id_computadora = Computadora.contador_computadoras
        self.__nombre = nombre
        self.__monitor = monitor 
        self.__teclado = teclado
        self.__raton = raton

    @property
    def id_computadora(self):
        return self.__id_computadora
    
    @id_computadora.setter
    def id_computadora(self, id_computadora):
        self.__id_computadora = id_computadora

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def monitor(self):
        return self.__monitor
    
    @monitor.setter
    def monitor(self, monitor):
        self.__monitor = monitor

    @property
    def teclado (self):
        return self.__teclado
    
    @teclado.setter
    def teclado(self, teclado):
        self.__teclado = teclado

    @property
    def raton(self):
        return self.__raton
    
    @raton.setter
    def raton(self, raton):
        self.__raton = raton

    @property
    def orden(self):
        return self.__orden
    
    @orden.setter
    def orden(self, orden):
        self.__orden = orden

    def __str__(self):
        return f'Nombre: {self.nombre} ID: {self.id_computadora}\n\t{self.monitor}\n\t{self.teclado}\n\t{self.raton}'
        
    


