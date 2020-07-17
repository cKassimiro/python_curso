#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

def fibonacci(limite):
    lista = [0, 1]
    while lista[-1] < limite:
        lista.append(sum(lista[-2:]))
    print(lista)


if __name__ == "__main__":
    entrada = int(input('insira um valor'))
    fibonacci(entrada)
