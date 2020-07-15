#!/usr/bin/python3

# PERCORRER STRING

palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=',')
print('fim')

# PERCORRER LISTA

aprovados = ['Ana', 'Rafael', 'João', 'Maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    # +1 para alinhar a posição de 0 ... infinito para 1 ... infinito
    print(f'{posicao + 1})', nome)

# PERCORRER TUPLA

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dias in dias_semana:
    print(f'Hoje é {dias}')

# PERCORRER CONJUNTO (SET)

for numero in set({1, 2, 3, 4, 5, 6}):
    print(numero
          )

conjunto = set({'a', 'b', 'c', dias})
for particula in conjunto:
    print(particula)
