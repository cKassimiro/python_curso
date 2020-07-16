# for i in range(1, 7):
#   if i == 6:
#        break
# else:
#    print('fim')

from random import randint


def sortear_dado():  # FUNÇÃO QUE GERA NUMERO ALEATORIO ENTRE 1 E 6
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:  # SEPARA OS NUMEROS IMPARES
        print(i)
        continue

    if i == sortear_dado():  # COMPARA OS NUMEROS PARES DE "i" COM A FUNÇÃO
        print('Acertou', i)
        break
else:
    print('Não acertou o numero!')
