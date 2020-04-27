from components.header import header
from functions.square.SquareArea import calculateSquareArea


def square_area_menu():
    header()

    print("A=B.h\n")

    base = float(input('Base [B] ➤ '))
    height = float(input('Altura [h] ➤ '))
    result = float(calculateSquareArea(base, height))

    print(f'\nÁrea [A] = {result}')
