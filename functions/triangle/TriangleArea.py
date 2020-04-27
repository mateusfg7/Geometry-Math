from math import sqrt

'''
a -> area
b -> base
h -> height
'''


def calculateTriangleAreaBH(b, h):
    a = (b*h)/2
    return a


'''
a -> side A
b -> side B
c -> side C
'''


def calculateTriangleAreaSP(a, b, c):
    semi_perimeter = (a+b+c)/2

    sp_calc = semi_perimeter*(semi_perimeter-a) * \
        (semi_perimeter-b)*(semi_perimeter-c)

    if sp_calc >= 0:
        area = sqrt(sp_calc)
    else:
        area = 'numero negativo'

    return area
