from components.header import header
from functions.square.SquareArea import calculate_square_area

def square_area_menu():
    header()

    print("A=B.h\n")

    base = float(input('Base [B] ➤ '))
    height = float(input('Altura [h] ➤ '))
    result = float(calculate_square_area(base, height))

    print(f'\nÁrea [A] = {result}')
    