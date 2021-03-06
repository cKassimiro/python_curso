#!/usr/bin/python3

# Calcular Area de uma Circunferencia
# pi * r^2

from math import pi
import sys
# import errno
# OU 'import math'.


def circulo(r):
    return pi * float(r)**2


def help():
    return print(
        """É necessario informar o raio do circulo.\n
        Sintaxe: {} <raio>""".format(sys.argv[0][2:]))


if __name__ == '__main__':

    if len(sys.argv) < 2:
        help()
        # sys.exit(errno.EPERM)

    else:
        r = sys.argv[1]
        area = circulo(r)
        print('Area do Circulo', area)
