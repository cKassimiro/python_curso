#!/usr/bin/python3

# Calcular Area de uma Circunferencia
# pi * r^2

# *************************** #

# IMPORTES

from math import pi
import sys
import errno

# *************************** #

# CLASSES


class terminalcolor:
    VERMELHO = '\033[91m'
    BRANCO = '\033[0m'

# *************************** #

# FUNÇÕES


def circulo(r):
    return pi * float(r)**2


def help():
    print('É necessario informar o raio do circulo.')
    print('Sintaxe: {} <raio>'.format(sys.argv[0][2:]))

# *************************** #


if __name__ == '__main__':

    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(terminalcolor.VERMELHO +
              '\nO raio deve ser um valor númerico!'
              + terminalcolor.BRANCO
              )
        sys.exit(errno.EINVAL)

    r = sys.argv[1]
    area = circulo(r)
    print('Area do Circulo', area)
