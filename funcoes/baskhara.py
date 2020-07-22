from math import sqrt
# ax² bx c = 0

if __name__ == '__main__':

    a = 2
    b = 4
    c = -16

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('delta negativo {}'.format(delta))
    else:
        print('delta = {}'.format(delta))

        x1 = -b + sqrt(delta)
        x2 = -b - sqrt(delta)
        div1 = (x1) / (2 * a)
        div2 = (x2) / (2 * a)
        print('x¹ = {}'.format(div1))
        print('x² = {}'.format(div2))
