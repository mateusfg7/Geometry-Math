from components.header import header
from functions.quadrado.area_do_quadrado import areaDoQuadradoCalc

def areaDoQuadrado():
    header()

    print("A=B.h\n")

    base = int(input('Base [B] ➤ '))
    altura = int(input('Altura [h] ➤ '))
    resultado = int(areaDoQuadradoCalc(base, altura))

    print(f'\nÁrea [A] = {resultado}')
    