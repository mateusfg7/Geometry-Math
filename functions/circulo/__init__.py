from components.header import header
from functions.circulo.area_do_circulo import areaDoCirculo

def areaDoCirculoMenu():
    header()

    print('A =π.r²\n')

    raio = float(input('Raio [r] ➤ '))
    print(f'\nArea [A] = {areaDoCirculo(raio)}')