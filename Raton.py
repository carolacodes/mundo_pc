from DispositivosEntrada import DispositivosEntrada
class Raton(DispositivosEntrada):

    contador_ratones = 0
    
    def __init__(self, id_raton):
        Raton.contador_ratones += 1
        self.__id_raton = Raton.contador_ratones


    @property
    def id_raton(self):
        return self.__id_raton
    
    @id_raton.setter
    def id_raton(self, id_raton):
        self.__id_raton = id_raton

    
    def __str__(self):
        return f'[Raton] ID: {self.id_raton} - Tipo de Entrada: {self.tipo_entrada} - Marca: {self.marca}'
