#!/usr/bin/python3

# Calcular Area de uma Circunferencia
# pi * r^2

from math import pi
import sys
# OU 'import math'.


def circulo(r):
    return pi * float(r)**2


if __name__ == '__main__':

    r = sys.argv[1]
    area = circulo(r)
    print('Area do Circulo', area)
