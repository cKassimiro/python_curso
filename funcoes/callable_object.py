#!/usr/bin/python3

class potencia:

    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    quadrado = potencia(2)
    cubo = potencia(3)

    if callable(quadrado) and callable(cubo):
