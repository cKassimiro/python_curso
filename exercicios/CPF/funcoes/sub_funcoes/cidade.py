#!/usr/bin/python3

def check_cidade(cpf):

    cidades = {'0': 'Rio Grande do Sul',
               '1': 'Distrito Federal, Goiás, Mato Grosso do Sul e Tocantins',
               '2': 'Pará, Amazonas, Acre, Amapá, Rondônia e Roraima',
               '3': 'Ceará, Maranhão e Piauí',
               '4': 'Pernambuco, Rio Grande do Norte, Paraíba e Alagoas',
               '5': 'Bahia e Sergipe',
               '6': 'Minas Gerais',
               '7': 'Rio de Janeiro e Espírito Santo',
               '8': 'São Paulo',
               '9': 'Paraná e Santa Catarina'}

    num_cidade = cpf[8]
    print('\n ESTADO DE ORIGEM: \n', cidades[num_cidade])
