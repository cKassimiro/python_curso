# OPERAÇÃO EMBUTIDA QUE GARANTE O FECHAMENTO DO ARQUIVO
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('arquivo foi fechado')

if saida.closed:
    print('arquivo de saida foi fechado')
