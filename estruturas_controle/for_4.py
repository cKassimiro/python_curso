from random import randint


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue
    if i % 2 == 0 and i == sortear_dado():
        print('Acertou')
        break
else:
    print('Não acertou o numero!')
