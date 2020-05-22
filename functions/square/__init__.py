from typing import NoReturn

from components.header import header
from functions.square.SquareArea import calculateSquareArea


def squareAreaMenu() -> NoReturn:
    '''
    This function get the base size and the heigth size, calculate this values, and displays the result.
    '''

    header()

    print("A=B.h\n")

    base = float(input('Base [B] ➤ '))
    height = float(input('Altura [h] ➤ '))
    result = float(calculateSquareArea(base, height))

    print(f'\nÁrea [A] = {result}')
