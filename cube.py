import math, cmath

def main():
    a, b, c, d = input("Введите через запятую коэффициенты a, b, c, d кубического уравнения вида ax^3 + bx^2 + cx + d = 0: ").split(',')
    a, b, c, d = float(a), float(b), float(c), float(d)

    if a == 0:
        print("Уравнение квадратное, решать не будем.")
        return(-1)
    
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)

    Q = (p/3)**3 + (q/2)**2

    if Q > 0:
        print("Q > 0. Существует один R-корень и два сопряженных C-корня")
        alpha = (-q/2 + math.sqrt(Q))**(1/3)
        beta = (-q/2 - math.sqrt(Q))**(1/3)
    elif Q == 0:
        print("Q == 0. Существует один однократный вещественный корень и один двукратный, или, если p = q = 0, то один трёхкратный вещественный корень.")
        alpha = (-q/2)**(1/3)
        beta = alpha
    else:
        print("Q < 0. Существует три вещественных корня.")
        alpha = (-q/2 + cmath.sqrt(Q))**(1/3)
        beta = (-q/2 - cmath.sqrt(Q))**(1/3)

    y1 = alpha + beta
    y2 = -(alpha + beta)/2 + (math.sqrt(3)*(alpha - beta)/2)*1j
    y3 = -(alpha + beta)/2 - (math.sqrt(3)*(alpha - beta)/2)*1j

    x1 = y1 - b / (3*a)
    if x1.imag == 0*1j: x1 = x1.real
    x2 = y2 - b / (3*a)
    if x2.imag == 0*1j: x2 = x2.real
    x3 = y3 - b / (3*a)
    if x3.imag == 0*1j: x3 = x3.real

    print("Корни: \n", x1, "\n", x2, "\n", x3)


if __name__ == "__main__":
    main()