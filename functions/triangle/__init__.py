from typing import NoReturn

from components.header import header
from functions.triangle.TriangleArea import calculateTriangleAreaBH
from functions.triangle.TriangleArea import calculateTriangleAreaSP


def menuAreaBH() -> NoReturn:
    '''
    Shows header and options to calculate the triangle area based on base and height.\n
    '''
    header()

    print("A = (B.h)/2\n")

    base = float(input('Base [B] ➤ '))
    height = float(input('Altura [h] ➤ '))
    result = float(calculateTriangleAreaBH(base, height))

    print(f'\nÁrea [A] = {result}')


def menuAreaSP() -> NoReturn:
    '''
    Shows header and options for calculating the area of triangle based on the sides of triangle.\n
    '''
    header()

    print("p=(a+b+c)/2")
    print("A = √(p.(p-a).(p-b).(p-c))\n")

    sideA = float(input('Lado A ➤ '))
    sideB = float(input('Lado B ➤ '))
    sideC = float(input('Lado C ➤ '))
    result = calculateTriangleAreaSP(sideA, sideB, sideC)

    print(f'\nÁrea [A] = {result}')


def triangleAreaMenu():
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
        menuAreaBH()
    elif choice == '2':
        menuAreaSP()
