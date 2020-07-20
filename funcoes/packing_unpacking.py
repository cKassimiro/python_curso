#!/usr/bin/python3
def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


# PACKING
if __name__ == "__main__":
    print(soma_2(8, 2))
    print(soma_3(98, 23, 1))
    print(soma_n(2, 22))

# UNPACKING
    lista_numeros = (1, 2, 5, 3)
    print(soma_n(*lista_numeros))
    tupla_numeros = (1, 2, 5, 3)
    print(soma_n(*tupla_numeros))
