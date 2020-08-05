from .sub_funcoes import gerador, verificador, cidade


def menus(estado):
    estado()

# GERAR DOIS ULTIMOS DIGITOS DO CPF A PARTIR
# DOS NUMEROS DE ENTRADA ESCOLHIDOS PELO USUARIO


def estado_1():
    print('')
    cpf_inicial = input('Digite o número do CPF sem os 2 últimos dígitos: \n')
    print('\n' + gerador.calc(cpf=cpf_inicial))


# VERIFICAR SE O CPF É VALIDO
# (COM BASE NOS REQUISITOS PROPOSTOS)


def estado_2():
    print('')
    cpf_completo = input('Digite o numero do CPF completo: \n')
    print(verificador.check(cpf=cpf_completo))


# VERIFICAR ESTADO(LOCAL) DE ORIGEM


def estado_3():
    print('')
    cpf_completo = input('Digite o numero do CPF completo:')
    digitos = verificador.check(cpf=cpf_completo)
    if digitos != 0:
        cidade.check_cidade(cpf=digitos)
    else:
        print('** CPF INVALIDO! **')
