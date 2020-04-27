from components.header import header

from functions.square import squareAreaMenu
from functions.triangle import triangleAreaMenu
from functions.trapeze import trapezeAreaMenu
from functions.diamond import diamondAreaMenu
from functions.circle import circleAreaMenu


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
        '1': lambda: squareAreaMenu(),
        '2': lambda: triangleAreaMenu(),
        '3': lambda: trapezeAreaMenu(),
        '4': lambda: diamondAreaMenu(),
        '5': lambda: circleAreaMenu(),
    }
    selectFunction[escolha]()
