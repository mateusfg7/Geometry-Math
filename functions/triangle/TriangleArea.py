'''
a -> area
b -> base
h -> height
'''


def calculateTriangleAreaBH(b: float, h: float) -> float:
    a = (b*h)/2
    return a


'''
a -> side A
b -> side B
c -> side C
'''


def calculateTriangleAreaSP(a: float, b: float, c: float) -> float:
    semiPerimeter = (a+b+c)/2

    spCalc = semiPerimeter*(semiPerimeter-a) * \
        (semiPerimeter-b)*(semiPerimeter-c)

    if spCalc >= 0:
        area = spCalc ** 0.5
    else:
        area = 'numero negativo'

    return area
