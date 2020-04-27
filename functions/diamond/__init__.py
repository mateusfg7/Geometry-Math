from components.header import header
from functions.diamond.DiamondArea import diamondArea


def diamond_area_menu():
    header()

    print('A=(D.d)/2\n')

    largerDiagonal = float(input('Diagonal Maior [D] ➤ '))
    smallerDiagonal = float(input('Diagonal Menor [d] ➤ '))

    print(f'\nArea [A] = {diamondArea(largerDiagonal, smallerDiagonal)}')
