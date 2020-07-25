# IMPORTA MODULO CSV
# ABRE COM 'OPEN' ARQUIVO COM DADOS
# CRIA VARIAVEL QUE ARMAZENA OS DADOS
# BUSCA COLUNA(CIDADE) DENTRO DA VARIAVEL QUE ARMAZENOU OS DADOS
# DENTRO DA FUNÇÃO IMPORTADA DO MODULO, É PASSADA A VARIAVEL DE ARMAZENAMENTO
# SEGUIDA PELA DECLARAÇÃO DE DIVISAO DE LINHAS, PARA QUE SEJAM LIDAS COM INDEX
# EXIBE A COLUNA A PARTIR DO INDEX

import csv

with open('desafio-ibge.csv', encoding=('latin1')) as data:
    storage_data = data.read()
    for city in csv.reader(storage_data.splitlines()):
        print(f'{city[8]}: {city[3]}')
