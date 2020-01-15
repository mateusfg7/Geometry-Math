from components.header import header

from functions.quadrado import areaDoQuadrado
from functions.triangulo import areaDoTrianguloMenu
from functions.trapezio import areaDoTrapezioMenu
from functions.lozango import areaDoLozangoMenu
from functions.circulo import areaDoCirculoMenu

def AreaDasFigurasPlanas():
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

    if escolha == '1':
        areaDoQuadrado()
    elif escolha =='2':
        areaDoTrianguloMenu()
    elif escolha =='3':
        areaDoTrapezioMenu()
    elif escolha =='4':
        areaDoLozangoMenu()
    elif escolha =='5':
        areaDoCirculoMenu()
        