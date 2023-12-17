from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton
from Computadora import Computadora
from Orden import Orden

monitor1 = Monitor('Samsung', '27 pulgadas')

teclado1 = Teclado('Cable USB', 'Redragon')
raton1 = Raton('Inalambrico', 'Logitech')
computadora1 = Computadora('PC Gamer', monitor1, teclado1, raton1)

computadoras = [computadora1]

orden1 = Orden(computadoras)

#print(orden1)

orden1.agregarComputadora(computadora1)
print(orden1)