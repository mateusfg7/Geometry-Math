from components.header import header
from components.menu.area_das_figuras_planas import AreaDasFigurasPlanas

def mainMenu():
    header()

    print("""
[1] Área das figuras planas
    """)

    escolha = input('➤ ')

    if escolha == '1':
        AreaDasFigurasPlanas()