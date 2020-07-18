#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

def soma(maximo, atual):
    if atual < maximo:
        print(atual)
        soma(maximo, atual + 1)


soma(10, 1)
