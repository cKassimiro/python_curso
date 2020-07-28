from funcoes import opcoes
from sys import exit


def inicio():
    print('\n|———- Menu de opções ——-—|\n')
    print('1 - Gerar dígitos verificadores\n'
          '2 - Verificar dígitos verificadores\n'
          '3 - Estado de origem\n'
          '4 - Sair\n')

    opcao = int(input('Escolha uma das opções acima: '))

    if opcao == 1:
        opcoes.menus(estado=opcoes.estado_1)
        inicio()
    elif opcao == 2:
        opcoes.menus(estado=opcoes.estado_2)
        inicio()
    elif opcao == 3:
        opcoes.menus(estado=opcoes.estado_3)
        inicio()
    elif opcao == 4:
        exit()


inicio()
