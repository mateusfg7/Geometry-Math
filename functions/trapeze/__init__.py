from components.header import header
from functions.trapeze.TrapezeArea import trapeze_area

def trapeze_area_menu():
    header()
    print('A=((B+b).h)/2\n')

    largerBase = float(input('Base Maior [B] ➤ '))
    smallerBase = float(input('Base Menor [b] ➤ '))
    height = float(input('Altura [h] ➤ '))

    print(f'\nÁrea [A] = {trapeze_area(largerBase, smallerBase, height)}')
