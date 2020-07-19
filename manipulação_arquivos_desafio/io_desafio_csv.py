#!/usr/bin/python3
# IMPORTA MODULO CSV

import csv
from urllib import request


def read(url):
    with request.urlopen(url) as data:
        print('Baixando CSV ...')
        storage_data = data.read().decode('latin1')
        print('Download completo!')
        for city in csv.reader(storage_data.splitlines()):
            print(f'{city[8]}: {city[3]}')


if __name__ == "__main__":
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
