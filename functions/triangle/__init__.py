from components.header import header
from functions.triangle.TriangleArea import calculate_triangle_area_BH
from functions.triangle.TriangleArea import calculate_triangle_area_SP

def menu_area_BH():
    header()

    print("A = (B.h)/2\n")

    base = float(input('Base [B] ➤ '))
    height = float(input('Altura [h] ➤ '))
    result = float(calculate_triangle_area_BH(base, height))

    print(f'\nÁrea [A] = {result}')

def menu_area_SP():
    header()

    print("p=(a+b+c)/2")
    print("A = √(p.(p-a).(p-b).(p-c))\n")

    sideA = float(input('Lado A ➤ '))
    sideB = float(input('Lado B ➤ '))
    sideC = float(input('Lado C ➤ '))
    result = calculate_triangle_area_SP(sideA, sideB, sideC)

    print(f'\nÁrea [A] = {result}')

def triangle_area_menu():
    header()
    print('Triangulo'.center(66))
    print("""
[1] Calcular com os valores da base e da altura
    A = (B.h)/2

[2] Calcular com os valores dos lados do triangul
    p=(a+b+c)/2
    A = √(p.(p-a).(p-b).(p-c))
    \n""")

    choice = input('➤ ')

    if choice == '1':
        menu_area_BH()
    elif choice == '2':
        menu_area_SP()
