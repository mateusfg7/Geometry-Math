from components.header import header
from functions.triangulo.area_do_triangulo import *

def areaBhMenu():
    header()

    print("A = (B.h)/2\n")

    base = int(input('Base [B] ➤ '))
    altura = int(input('Altura [h] ➤ '))
    resultado = int(areaDoTrianguloBhCalc(base, altura))

    print(f'\nÁrea [A] = {resultado}')

def areaSPMenu():
    header()

    print("p=(a+b+c)/2")
    print("A = √(p.(p-a).(p-b).(p-c))\n")

    ladoA = float(input('Lado A ➤ '))
    ladoB = float(input('Lado B ➤ '))
    ladoC = float(input('Lado C ➤ '))
    resultado = areaDoTrianguloSpCalc(ladoA, ladoB, ladoC)

    print(f'\nÁrea [A] = {resultado}')

def areaDoTrianguloMenu():
    header()
    print('Triangulo'.center(66))
    print("""
[1] Calcular com os valores da base e da altura
    A = (B.h)/2

[2] Calcular com os valores dos lados do triangul
    p=(a+b+c)/2
    A = √(p.(p-a).(p-b).(p-c))
    \n""")

    escolha = input('➤ ')

    if escolha == '1':
        areaBhMenu()
    elif escolha == '2':
        areaSPMenu()
        