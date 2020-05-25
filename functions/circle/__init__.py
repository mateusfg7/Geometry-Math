from typing import NoReturn

from math import pi

from components.header import header
from functions.circle.CircleArea import circleArea


def circleAreaMenu() -> NoReturn:
    '''
    Shows header and options to calculate the area of the circle.
    '''
    header()

    print('A =π.r²\n')

    radius = float(input('Raio [r] ➤ '))
    print(f'\nArea [A] = {circleArea(pi, radius)}')
