#!/usr/bin/python3

class Potencia:

    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print('3² => {}'.format(quadrado(3)))
        print('2³ => {}'.format(cubo(2)))
        print(Potencia(8)(2))  # primeiro parametro: EXPOENTE; segundo: BASE
