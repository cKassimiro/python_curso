#!/usr/bin/python3
try:  # USADO PARA OPERAÇÕES ARRISCADAS
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
except IndexError:
    pass

finally:
    print('finally')
    arquivo.close()  # GARANTE O FECHAMENDO DO ARQUIVO

if arquivo.closed:
    print('arquivo foi fechado')
