from components.header import header
from functions.trapezio.area_do_trapezio import areaDoTrapezio

def areaDoTrapezioMenu():
    header()
    print('A=((B+b).h)/2\n')

    baseMaior = float(input('Base Maior [B] ➤ '))
    baseMenor = float(input('Base Menor [b] ➤ '))
    altura = float(input('Altura [h] ➤ '))

    print(f'\nÁrea [A] = {areaDoTrapezio(baseMaior, baseMenor, altura)}')
