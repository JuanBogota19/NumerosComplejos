import math

def print_hi(name):
    print(f'Hi, {name}')

def suma_cplx(c1, c2):
    parteR = c1[0] + c2[0]
    parteI = c1[1] + c2[1]
    return (parteR,parteI)

def mult_cplx(c1,c2):
    parteA = c1[0] * c2[0]
    parteB = c1[1] * c2[1]
    parteC = c1[0] * c2[1]
    parteD = c1[1] * c2[0]
    parteE = parteA - parteB
    parteF = parteC + parteD
    return (parteE,parteF)

def rest_cplx(c1,c2):
    parteA = c1[0] - c2[0]
    parteB = c1[1] - c2[1]

    return (parteA,parteB)

def div_plx(c1,c2):
    parteA = (c1[0] * c2[0]) + (c1[1] * c2[1])
    parteB = (c2[0] ** 2) + (c2[1] ** 2)
    parteC = (c2[0] * c1[1]) - (c1[0]*c2[1])
    parteI = parteA / parteB
    parteD = parteC / parteB
    return (parteI,parteD)

def modul_cplx(c1):
    parteG = c1[0]**2
    parteH = c1[1]**2
    parteII = parteG + parteH
    parteJ = parteII**0.5
    return (parteJ)

def conj_cplx(c1):
    parteL = c1[0]
    parteA = -c1[1]
    return (parteL,parteA)

def polar_cplx(c1):
    parteA = modul_cplx(c1)
    parteB = fase_cplx(c1)
    parteC = parteA * math.cos(parteB) + parteA * math.sin(parteB)
    return (parteC)

def fase_cplx(c1):
    parteZ = c1[1] / c1[0]
    parteZZ = math.atan(parteZ)
    return (parteZZ)


if __name__ == '__main__':
    print("suma", suma_cplx((4,2),(4, 5)))
    print("multiplicación",mult_cplx((4,3),(5, 5.2)))
    print("resta", rest_cplx((4,2),(5, 5.2)))
    print("división",div_plx((2,-4), (-4,2)))
    print("modulo",modul_cplx((1,6)))
    print("conjugado",conj_cplx((4,5)))
    print("fase",fase_cplx((4,9)))
    print("polar a cartesiano",polar_cplx((5,5)))



