#!/usr/bin/python3

# Calcular Area de uma Circunferencia
# pi * r^2

from math import pi
# OU 'import math'.


def circulo(r):
    print('Area do Circulo', pi * float(r)**2)


if __name__ == '__main__':

    r = input('valor do raio: ')
    circulo(r)
