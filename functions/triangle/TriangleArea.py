from typing import Union


def calculateTriangleAreaBH(b: float, h: float) -> float:
    '''
    a -> area\n
    b -> base\n
    h -> height\n
    '''
    a: float = (b*h)/2
    return a


def calculateTriangleAreaSP(a: float, b: float, c: float) -> Union[float, str]:
    '''
    a -> side A\n
    b -> side B\n
    c -> side C\n
    '''
    semiPerimeter: float = (a+b+c)/2

    spCalc = semiPerimeter*(semiPerimeter-a) * \
        (semiPerimeter-b)*(semiPerimeter-c)

    if spCalc >= 0:
        area = spCalc ** 0.5
    else:
        area = 'numero negativo'

    return area
