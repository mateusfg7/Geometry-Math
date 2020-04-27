from components.header import header
from functions.circle.CircleArea import circleArea


def circleAreaMenu():
    header()

    print('A =π.r²\n')

    radius = float(input('Raio [r] ➤ '))
    print(f'\nArea [A] = {circleArea(radius)}')
