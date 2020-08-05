#!/usr/bin/python3

from funcoes.sub_funcoes import gerador


def check(cpf):
    saida = gerador.calc(cpf[:9])
    cpf =\
        f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    if saida == cpf:
        resultado = f'\n {cpf} \n CPF Válido!'
    else:
        resultado = f'\n {cpf} \n CPF Inválido!'

    return resultado
