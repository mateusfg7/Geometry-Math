from typing import NoReturn

from components.header import header
from functions.trapeze.TrapezeArea import trapezeArea


def trapezeAreaMenu() -> NoReturn:
    '''
    Shows header and options for calculating the area of the trapeze.
    '''
    header()
    print('A=((B+b).h)/2\n')

    largerBase = float(input('Base Maior [B] ➤ '))
    smallerBase = float(input('Base Menor [b] ➤ '))
    height = float(input('Altura [h] ➤ '))

    print(f'\nÁrea [A] = {trapezeArea(largerBase, smallerBase, height)}')
