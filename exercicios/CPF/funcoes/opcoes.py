from .sub_funcoes import gerador


def menus(estado):
    estado()


def estado_1():
    cpf_inicial = input('Digite o número do CPF sem os 2 últimos dígitos: \n')
    gerador.calc(cpf=cpf_inicial)


def estado_2():
    print('estado2')


def estado_3():
    print('estado3')
