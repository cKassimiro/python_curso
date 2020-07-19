#!/usr/bin/python3
import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('nome: {}, idade: {}'.format(*pessoa))
