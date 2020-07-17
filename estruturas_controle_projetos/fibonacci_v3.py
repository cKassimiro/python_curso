#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print('{}, {}'.format(penultimo, ultimo))
    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo,)


if __name__ == "__main__":
    fibonacci(10946)
