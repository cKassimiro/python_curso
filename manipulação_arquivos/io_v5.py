# OPERAÇÃO EMBUTIDA QUE GARANTE O FECHAMENTO DO ARQUIVO
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('arquivo foi fechado')
