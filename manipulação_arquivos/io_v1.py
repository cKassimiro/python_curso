#!/usr/bin/python3
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for regristo in dados.splitlines():
    print('nome: {}, idade: {}'.format(*regristo.split(',')))
