from math import sqrt

def areaDoTrianguloBhCalc(base, altura):
    area = (base*altura)/2
    return area

def areaDoTrianguloSpCalc(a, b, c):
    semi_perimetro = (a+b+c)/2

    sp_calc = semi_perimetro*(semi_perimetro-a)*(semi_perimetro-b)*(semi_perimetro-c)

    if sp_calc >= 0:
        area = sqrt(sp_calc)
    else:
        area = 'numero negativo'

    return area