from DispositivosEntrada import DispositivoEntrada
class Teclado(DispositivoEntrada):
    contador_teclados = 0
    def __init__(self, tipo_entrada, marca):
        super(tipo_entrada, marca)
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados

    @property
    def id_teclado(self):
        return self.__id_teclado
    @id_teclado.setter
    def id_teclado(self, id_teclado):
        self.__id_teclado = id_teclado

    def __str__(self):
        return f'[Teclado] ID: {self.id_teclado} - tipo de entrada: {self.tipo_entrada} - marca: {self.marca}'