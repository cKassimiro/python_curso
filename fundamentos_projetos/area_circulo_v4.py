#!/usr/bin/python3

# Calcular Area de uma Circunferencia
# pi * r^2

from math import pi
# OU 'import math'.

if __name__ == '__main__':

    r = input('valor do raio: ')
    operacao = pi * float(r)**2

    print(operacao)
