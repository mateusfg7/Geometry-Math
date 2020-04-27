from components.header import header

from functions.square import square_area_menu
from functions.triangle import triangle_area_menu
from functions.trapeze import trapeze_area_menu
from functions.diamond import diamond_area_menu
from functions.circle import circle_area_menu


def flatFiguresMenu():
    header()

    print('Áreas das figuras planas'.center(66))
    print("""
[1] Área de um quadrado, retângulo ou paralelogramo
[2] Área de um triangulo
[3] Área de um trapézio
[4] Área de um lozango
[5] Área de um círculo
    """)

    escolha = input('➤ ')

    selectFunction = {
        '1': lambda: square_area_menu(),
        '2': lambda: triangle_area_menu(),
        '3': lambda: trapeze_area_menu(),
        '4': lambda: diamond_area_menu(),
        '5': lambda: circle_area_menu(),
    }
    selectFunction[escolha]()