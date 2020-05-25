from typing import NoReturn

from components.header import header
from functions.diamond.DiamondArea import diamondArea


def diamondAreaMenu() -> NoReturn:
    '''
    Shows header and options for calculating the area of the diamond.
    '''
    header()

    print('A=(D.d)/2\n')

    largerDiagonal = float(input('Diagonal Maior [D] ➤ '))
    smallerDiagonal = float(input('Diagonal Menor [d] ➤ '))

    print(f'\nArea [A] = {diamondArea(largerDiagonal, smallerDiagonal)}')
