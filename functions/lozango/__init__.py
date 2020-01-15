from components.header import header
from functions.lozango.area_do_lozango import areaDoLozango

def areaDoLozangoMenu():
    header()

    print('A=(D.d)/2\n')
    
    diagonalMaior = float(input('Diagonal Maior [D] ➤ '))
    diagonalMenor = float(input('Diagonal Menor [d] ➤ '))

    print(f'\nArea [A] = {areaDoLozango(diagonalMaior, diagonalMenor)}')
    