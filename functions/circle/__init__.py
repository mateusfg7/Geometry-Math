from components.header import header
from functions.circle.CircleArea import circle_area

def circle_area_menu():
    header()

    print('A =π.r²\n')

    radius = float(input('Raio [r] ➤ '))
    print(f'\nArea [A] = {circle_area(radius)}')
    